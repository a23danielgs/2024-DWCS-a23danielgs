from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

def review (request):
    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                password=form.cleaned_data['password'],
                city=form.cleaned_data['city'],
                web=form.cleaned_data['web'],
                role=form.cleaned_data['role'],
                sign_on=",".join(form.cleaned_data['sign_on'])
                )
            review.save()

            # return HttpResponseRedirect("/thank_you")
            return render(request,"reviews/thank_you.html",{
                "form": form
            })
    else:
        form = ReviewForm()
    return render(request,"reviews/review.html",{
        "form": form
    })

# def thank_you (request):
#     return render(request,"reviews/thank_you.html")



