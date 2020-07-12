from django import forms


class CommonForm(forms.Form):
    name = forms.CharField(max_length=50)
    contact_no = forms.IntegerField()
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
