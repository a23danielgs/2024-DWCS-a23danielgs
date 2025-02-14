from django.db import models

# Create your models here.

class Review(models.Model):
    CHOICES_WEB=[('apache','Apache'),
                 ('nginx','Nginx'),
                 ('microsoft IIS','Microsoft IIS'),
                 ('litespeed','LiteSpeed')]
    CHOICES_ROLE =[('admin','Admin'),
                 ('engineer','Engineer'),
                 ('manager','Manager'),
                 ('guest','Guest')]
    CHOICES_SIGN=[('mail','Mail'),
                 ('payroll','Payroll'),
                 ('self-service','Self-service')]      

    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=20, blank=True, null=True,choices=CHOICES_WEB)
    role = models.CharField(max_length=20, blank=True, null=True,choices=CHOICES_ROLE)
    sign_on = models.JSONField(blank=True, null=True)


 
    # city = forms.CharField(required=False)
    # web = forms.ChoiceField(required=False,choices=CHOICES_WEB)
    # role = forms.ChoiceField(required=False,choices=CHOICES_ROLE)
    # sign_on = forms.MultipleChoiceField(required=False,choices=CHOICES_SIGN)