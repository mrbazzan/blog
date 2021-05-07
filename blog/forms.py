
from django import forms


class EmailForm(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return Email
