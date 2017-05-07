from django.forms import ModelForm

from collection.models import Loonatic

class LoonaticForm(ModelForm):
    class Meta:
        model = Loonatic
        fields = ('name', 'description',)
