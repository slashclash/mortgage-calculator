from django.db import models
from django.core.exceptions import ValidationError


def positive_number(value):
    if value <= 0:
        raise ValidationError("Число должно быть положительным")


def max_rate(value):
    if value > 100:
        raise ValidationError("Ставка должна быть ниже 100%")


def max_period(value):
    if value > 30:
        raise ValidationError("Срок кредита не может быть больше 30 лет")


class Mortgage(models.Model):
    """Результат расчета ипотеки"""
    full_price = models.IntegerField(validators=[positive_number])
    initial_payment = models.IntegerField(validators=[positive_number])
    period = models.IntegerField(validators=[positive_number, max_period])
    interest_rate = models.FloatField(validators=[positive_number, max_rate])
    credit = models.IntegerField()
    monthly_payment = models.IntegerField()
    user = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
