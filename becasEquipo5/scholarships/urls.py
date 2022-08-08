from django.urls import path
from scholarships import views

urlpatterns = [
    path('', views.ScholarshipView.as_view()),
    path('requirement/', views.RequirementView.as_view()),
]