from django import forms
# from django.forms import ModelForm

from collection.models import Loonatic

class LoonaticForm(forms.ModelForm):
    class Meta:
        model = Loonatic
        fields = ('name', 'description',)

class ContactForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
