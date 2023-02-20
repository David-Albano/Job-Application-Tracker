from django.forms import ModelForm, DateInput, Textarea
from .models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = [
            'company',
            'role',
            'stage',
            'platform',
            'app_date',
            'last_contact',
            'job_description',
            'commentary',
            'contact'
        ]
        widgets = {
            'app_date': DateInput(attrs={'type': 'date', 'id': 'date_form'}),
            'last_contact': DateInput(attrs={'type': 'date', 'id': 'date_form'}),
            'job_description': Textarea(attrs={'type': 'text', 'id':'job_desc'})
        }
