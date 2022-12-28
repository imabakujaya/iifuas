from django.forms import ModelForm
from belajar.models import Managemen

class FormManagemen(ModelForm):
    class Meta:
        model = Managemen
        fields = '__all__'