from django import forms
from django.forms import TextInput, Select, RadioSelect, CheckboxSelectMultiple
from .models import Review

class ReviewForm(forms.ModelForm):
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter city'}))
    web = forms.ChoiceField(choices=Review.CHOICES_WEB, required=False)
    role = forms.ChoiceField(choices=Review.CHOICES_ROLE, widget=forms.RadioSelect, required=False)
    sign_on = forms.MultipleChoiceField(choices=Review.CHOICES_SIGN, widget=forms.CheckboxSelectMultiple, required=False)
    
    class Meta():
        model = Review
        fields = ["user_name","password","city","web","role","sign_on"]
        # fields = "__all__"
        labels = {
            "user_name":"Your Name",
            "password":"Your Password",            
            "city":"City of employment",
            "web":"Web Server",
            "role":"Please select a role",
            "sign_on":"Please Sign-on to the following"
        }
        widgets = {
            "user_name": TextInput(attrs={"placeholder": "Enter username"}),
            "password": TextInput(attrs={"placeholder": "Enter password"}),
        }
