from django.forms import forms

from contacts.models import Contacts


class ContactForm(forms.Form):
    class Meta:
        model = Contacts
