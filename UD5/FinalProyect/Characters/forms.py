from django import forms

from .models import Universe,Character

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ["slug"]
        labels = {
            "name": "Name of the character",
            "description": "Description",
            "image": "Image",
            "alternateImage":"Alternate image (Optional)",
            "universe":"Universe of the character"
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10})
        }


class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        exclude = ["slug"]
        labels = {
            "name": "Name of the universe",
            "description": "Description",
            "image":"Image",
            "date_of_creation":"Date of creation",
            "creator":"Creator of the universe"
        }
        widgets = {
            "date_of_creation": forms.DateInput(attrs={"type": "date"}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10})
        }

