from django.forms import ModelForm, Textarea

from .models import Playbook

class PlaybookForm(ModelForm):
    class Meta:
        model = Playbook
        fields = ['name', 'details', 'script']
        widgets = {
            'details': Textarea(),
        }