from django.contrib import admin
from django.urls import path
from library.views import *

urlpatterns = [
    path('', bosh_sahifa),
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('talaba/', hamma_talabalar),
    path('talaba_delete/<int:son>/', talaba_ochir),
    path('talaba/<int:son>/', bitta_talaba),
    path('kitoblar/', kitoblar),
    path('kitob_delete/<int:son>/', kitob_ochir),
    path('mualliflar/', muallif),
    path('muallif/<int:son>/', bitta_muallif),
    path('muallif_delete/<int:son>/', muallif_ochir),
    path('talaba_edit/<int:son>/', talaba_edit),
    path('kitob_edit/<int:son>/', kitob_edit),
    path('adminlar/', adminlar),
    path('admin_delete/<int:son>/', admin_delete),
    path('bitta_admin/<int:son>/', bitta_admin),
    path('admin_edit/<int:son>/', admin_edit)
]


