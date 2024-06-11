# forms.py
from django import forms
from .models import ReachOut


class ReachOutForm(forms.ModelForm):
    class Meta:
        model = ReachOut
        fields = (
            "name",
            "email",
            "phone_number",
            "order_number",
            "about",
            "message",
        )
        widgets = {
            "about": forms.Select(choices=ReachOut.ABOUT_CHOICES),
        }
