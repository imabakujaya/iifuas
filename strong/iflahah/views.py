from django.shortcuts import render
from iflahah.models import Rutinitas
from iflahah.forms import FormRutinitas 

def iif(request):
    rutinitas = Rutinitas.objects.all()

    konteks = {
        'rutinitas' : rutinitas,
    }
    return render(request, 'iif/iif.html', konteks)

def dua(request):
    form = FormRutinitas()

    konteks = {
        'form' : form,
    }

    return render(request, 'iif/dua.html', konteks)
 

