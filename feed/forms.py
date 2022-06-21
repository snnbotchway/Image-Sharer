from django import forms

class AddNewImage(forms.Form):
    image = forms.ImageField()
    description = forms.CharField()

    