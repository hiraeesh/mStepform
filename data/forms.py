from django import forms

class StepOneForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class StepTwoForm(forms.Form):
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)

class StepThreeForm(forms.Form):
    age = forms.IntegerField()
    occupation = forms.CharField(max_length=100)
