from django import forms
from .models import Review

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter username"}))
    password = forms.CharField(label="Password", max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter password"}))
    city = forms.CharField(required=False ,label="City of employment", max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter city"}))
    
    CHOICES_WEB=[('Apache','Apache'),
                 ('Nginx','Nginx'),
                 ('Microsoft IIS','Microsoft IIS'),
                 ('Litespeed','LiteSpeed')]
    web = forms.ChoiceField(
        choices=CHOICES_WEB, 
        widget=forms.Select,
        required=False,
        label="Web Server"
    )

    CHOICES_ROLE =[('admin','Admin'),
                 ('engineer','Engineer'),
                 ('manager','Manager'),
                 ('guest','Guest')]
    role = forms.ChoiceField(
        choices=CHOICES_ROLE,
        widget=forms.RadioSelect,
        required=False,
        label="Please specify your role"
    )

    CHOICES_SIGN=[('mail','Mail'),
                 ('payroll','Payroll'),
                 ('self-service','Self-service')]
    sign_on = forms.MultipleChoiceField(
        choices=CHOICES_SIGN,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Please Sign-on to the following:"
    )



