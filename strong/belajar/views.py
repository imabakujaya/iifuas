from django.shortcuts import render
from belajar.models import Managemen
from belajar.forms import FormManagemen

def bisa(request):
    managemen = Managemen.objects.all()

    konteks = {
        'managemen' : managemen,
    }
    return render(request, 'belajar/bisa.html', konteks) 

def one(request):
    form = FormManagemen()

    konteks = {
        'form' : form,
    }

    return render(request, 'belajar/one.html', konteks)
