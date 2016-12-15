from django import forms

class PeopleForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)