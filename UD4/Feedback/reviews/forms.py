from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter username"}))
    password = forms.CharField(label="Password", max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter password"}))
    city = forms.CharField(label="City of employment", required=False ,max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter city"}))
    web = forms.SelectMultiple

    review_text = forms.CharField(label="Your feedback 👇",widget=forms.Textarea,max_length=100)



