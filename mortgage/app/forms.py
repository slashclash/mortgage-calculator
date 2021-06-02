from django import forms
from .models import Mortgage


class MortgageForm(forms.ModelForm):
    class Meta:
        model = Mortgage
        fields = ['full_price', 'initial_payment', 'period', 'interest_rate']
        labels = {
            'full_price': "Стоимость недвижимости",
            'initial_payment': 'Первоначальный взнос',
            'period': 'Срок',
            'interest_rate': 'Процентная ставка',
                  }

        widgets = {'full_price': forms.TextInput(attrs={'placeholder': '6500000 ₽', 'initial': '5555'}),
                   'initial_payment': forms.TextInput,
                   'period': forms.TextInput,
                   'interest_rate': forms.TextInput
                   }

    def clean(self):
        cleaned_data = super().clean()
        full_price = cleaned_data.get("full_price")
        initial_payment = cleaned_data.get("initial_payment")

        if full_price and initial_payment:
            if initial_payment >= full_price:
                raise forms.ValidationError(
                    "Первоначальный взнос не может быть больше стоимости недвижимости")

            minimum_payment = round(0.15 * full_price)
            if initial_payment < minimum_payment:
                raise forms.ValidationError(
                    "Первоначальный взнос должен быть не ниже {} руб.".format(minimum_payment))
