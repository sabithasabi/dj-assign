from django import forms
from demo.models import Signup
from demo.models import Signup2
class SignupForm(forms.ModelForm):
     class Meta:
        model=Signup
        fields="__all__"

class SignupForm2(forms.ModelForm):
     class Meta:
        model=Signup2
        fields="__all__"