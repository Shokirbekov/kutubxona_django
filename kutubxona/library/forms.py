from django import forms
from .models import *
class TalabaForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=30)
    course = forms.IntegerField(min_value=1, max_value=7)
    books = forms.IntegerField(min_value=0)
    graduate = forms.BooleanField(required=False)

class MuallifForm(forms.Form):
    name = forms.CharField(max_length=50)
    books = forms.IntegerField()
    age = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=50)
    alive = forms.BooleanField()

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ("nom", "sahifa", "muallif")

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'