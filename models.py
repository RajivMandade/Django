from django.db import models
from django import forms
from django.contrib.auth.models import User

class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=50)
    incomeDate=models.DateField()
    description=models.TextField(max_length=400)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table="income"


class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'