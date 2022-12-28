from django.shortcuts import render
from ipe.models import Pengurus
from ipe.forms import FormPengurus 



def cantik(request):
    kegiatan = Pengurus.objects.all()

    konteks = {
        'kegiatan': kegiatan,
    }
    return render(request, 'ipe/cantik.html', konteks) 

def tiga(request):
    form = FormPengurus()

    konteks = {
        'form' : form,
    }

    return render(request, 'cantik/tiga.html', konteks)
 

    