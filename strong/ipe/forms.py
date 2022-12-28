from django.forms import ModelForm
from ipe.models import Pengurus

class FormPengurus(ModelForm):
    class Meta:
        model = Pengurus
        fields = '__all__'