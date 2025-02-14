from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

def reviewWithModel (request):
    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                password=form.cleaned_data['password'],
                city=form.cleaned_data['city'],
                web=form.cleaned_data['web'],
                role=form.cleaned_data['role'],
                sign_on=form.cleaned_data['sign_on']
                )
            review.save()

            return render(request,"reviewsWithModel/thank_you.html",{
                "form": form
            })
    else:
        form = ReviewForm()
    return render(request,"reviewsWithModel/review.html",{
        "form": form
    })
