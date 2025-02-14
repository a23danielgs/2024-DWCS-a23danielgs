from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView 
from .forms import ReviewForm,StudentForm
from .models import Review,Student

# Create your views here.


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)
    
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["message"]="This works!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     review = Review.objects.get(pk=review_id)
    #     context["review"] = review
    #     return context

class StudentView(CreateView):
    template_name = "students/student.html"
    model = Student
    form_class = StudentForm
    success_url = "/thank-you"

class StudentsListView(ListView):
    template_name = "students/student_list.html"
    model = Student
    context_object_name = "students"
    
class SingleStudentView(DetailView):
    template_name = "students/student_review.html"
    model = Student

class UpdateStudentView(UpdateView):
    template_name = "students/student_update.html"
    model = Student
    fields = [ 
        "name", 
        "degree"
    ] 
    success_url ="/students"

class DeleteStudentView(DeleteView):
    model = Student
    success_url ="/students" 
    template_name = "students/student_delete.html"