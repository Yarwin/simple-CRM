from django.forms import ModelForm

from .models import Company


class NewCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name']

