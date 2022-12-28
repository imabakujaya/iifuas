from django.contrib import admin
from django.urls import path, include
from belajar.views import bisa, one
from iflahah.views import iif, dua
from ipe.views import cantik, tiga



from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.bisa),
    path('belajar/', include('belajar.urls')),
    path('ipe/', include('ipe.urls')),
    path('iflahah/', include('iflahah.urls')),
    path('one/', one),
    path('dua/', dua),
    path('tiga/', tiga),
]

