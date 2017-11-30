import django.forms as forms
from .models import Company


class NewCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'subtitle', 'notes']
        widgets = {
          'notes': forms.Textarea(attrs={'rows':4, 'cols':22}),
        }