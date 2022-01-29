from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import MortgageForm
from .models import Mortgage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required()
def get_history(request):
    history = Mortgage.objects.filter(user=request.user.username).order_by('-date')

    page = request.GET.get('page')
    paginator = Paginator(history, 5)

    try:
        history_items = paginator.get_page(page)
    except PageNotAnInteger:
        history_items = paginator.get_page(1)
    except EmptyPage:
        history_items = paginator.get_page(paginator.num_pages)

    return history_items


@login_required()
def index(request):
    if request.method != 'POST':
        initial_data = {'full_price': 7500000,
                        'initial_payment': 1125000,
                        'period': 15,
                        'interest_rate': 7.5,
                        }
        history_items = get_history(request)
        form = MortgageForm(initial=initial_data)
        context = {'credit': '6375000', 'monthly_payment': '59097', 'form': form, 'history_items': history_items}
        return render(request, 'index.html', context)
    else:
        form = MortgageForm(data=request.POST)
        if form.is_valid():
            credit = int(request.POST['full_price']) - int(request.POST['initial_payment'])
            month_rate = float(request.POST['interest_rate']) / (100 * 12)
            period_in_months = int(request.POST['period']) * 12
            monthly_payment = round((credit * month_rate) / (1 - ((1 + month_rate) ** (-period_in_months))))
            mortgage = form.save(commit=False)
            mortgage.credit = credit
            mortgage.monthly_payment = monthly_payment
            mortgage.user = request.user
            mortgage.save()
            history_items = get_history(request)
            context = {'form': form, 'credit': credit, 'monthly_payment': monthly_payment,
                       'history_items': history_items}
            return render(request, 'index.html', context)

        else:
            context = {'form': form}
            return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)
