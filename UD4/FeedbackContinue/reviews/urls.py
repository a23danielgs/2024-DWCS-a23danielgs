from django.urls import path

from . import views

app_name='reviews'

urlpatterns = [
     path("", views.ReviewView.as_view()),
     path("thank-you", views.ThankYouView.as_view()),
     path("reviews", views.ReviewsListView.as_view()),
     path("reviews/<int:pk>", views.SingleReviewView.as_view()),

     path("student",views.StudentView.as_view(),name='create'),
     path("students",views.StudentsListView.as_view()),
     path("student/<int:pk>",views.SingleStudentView.as_view()),
     path("students/update/<int:pk>",views.UpdateStudentView.as_view(),name='update'),
     path('students/delete/<int:pk>', views.DeleteStudentView.as_view(),name='delete'),
]