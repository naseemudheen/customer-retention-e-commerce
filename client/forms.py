from django import forms
from .models import Enquiry

class EnquiryCreateForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['phone', 'name', 'email', 'message']