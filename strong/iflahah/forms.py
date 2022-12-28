from django.forms import ModelForm
from iflahah.models import Rutinitas

class FormRutinitas(ModelForm):
    class Meta:
        model = Rutinitas
        fields = '__all__'