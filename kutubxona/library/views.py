from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

def hello(request):
    return HttpResponse("Salom Dunyo")

def salomlash(request):
    data = {
        "ism": "Ali",
        "ismlar": ["Avaz", "Kamron", "Javohir", "Tohir", "Said"]
    }
    return render(request, 'salom.html', data)

def bosh_sahifa(request):
    return render(request, 'bosh-sahifa.html')

def hamma_talabalar(request):
    if request.method == 'POST':
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get('name'),
                kurs = forma.cleaned_data.get('course'),
                kitoblar_soni = forma.cleaned_data.get('books'),
                bitiruvchi = forma.cleaned_data.get('graduate'),
            )
        return redirect('/talaba/')
    soz = request.GET.get('qidirish')
    if soz is None or soz == '':
        st = Talaba.objects.all()
    else:
        st = Talaba.objects.filter(ism__contains=soz)

    data = {
        "forma": TalabaForm(),
        "talabalar": st
    }
    return render(request, 'talabalar.html', data)

def bitta_talaba(request, son):
    data = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'bitta-talaba.html', data)

def kitoblar(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitoblar/')
    soz = request.GET.get('qidirish')
    if soz is None or soz == '':
        st = Kitob.objects.all()
    else:
        st = Kitob.objects.filter(nom__contains=soz)
    data = {
        "forma": KitobForm,
        "kitob": st,
        "mualliflar": Muallif.objects.all()
    }
    return render(request, 'muallif.html', data)

def muallif(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            Muallif.objects.create(
                ism = forma.cleaned_data.get('name'),
                tirik = forma.cleaned_data.get('alive'),
                kitob_soni = forma.cleaned_data.get('books'),
                yosh = forma.cleaned_data.get('age'),
                jins = forma.cleaned_data.get('gender'),
            )
        return redirect('/mualliflar/')
    soz = request.GET.get('qidirish')
    if soz is None or soz == '':
        st = Muallif.objects.all()
    else:
        st = Muallif.objects.filter(ism__contains=soz)
    data = {
        "forma": MuallifForm(),
        "muallif": st
    }
    return render(request, 'Kitob.html', data)

def talaba_edit(request, son):
    if request.method == "POST":
        if request.POST.get('b') == 'on':
            bitiruvchi = True
        else:
            bitiruvchi = False
        Talaba.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            kurs = request.POST.get('k'),
            kitoblar_soni = request.POST.get('k_s'),
            bitiruvchi = bitiruvchi
        )
        return redirect('/talaba/')

    data = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'talabaedit.html', data)

def bitta_muallif(request, son):
    data = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, 'bitta-muallif.html', data)

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect('/talaba/')

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitoblar/')

def muallif_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar/')

def admin_delete(request, son):
    Admin.objects.get(id=son).delete()
    return redirect('/adminlar/')

def kitob_edit(request, son):
    if request.method == 'POST':
        Kitob.objects.filter(id=son).update(
            nom = request.POST.get('n'),
            sahifa = request.POST.get('s'),
            muallif = Muallif.objects.get(id = request.POST.get('m')),
        )
        return redirect('/kitoblar/')
    data = {
        "kitob": Kitob.objects.get(id=son),
        "mualliflar": Muallif.objects.all()
    }
    return render(request, 'kitobedit.html', data)

def admin_edit(request, son):
    if request.method == 'POST':
        Admin.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            ish_vaqti = request.POST.get('i_v')
        )
        return redirect('/adminlar/')
    data = {
        "admin": Admin.objects.get(id=son)
    }
    return render(request, 'adminedit.html', data)

def adminlar(request):
    if request.method == 'POST':
        forma = AdminForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("/adminlar/")
    data = {
        "forma": AdminForm(),
        "admin": Admin.objects.all()
    }
    return render(request, 'adminlar.html', data)

def bitta_admin(request, son):
    data = {
        "admin": Admin.objects.get(id=son)
    }
    return render(request, 'bitta_admin.html', data)