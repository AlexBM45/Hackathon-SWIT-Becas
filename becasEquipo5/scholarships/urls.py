from django.urls import path
from scholarships import views

urlpatterns = [
    path('', views.ScholarshipView.as_view()),
    path('requirements/', views.RequirementView.as_view()),
    path('<int:id>', views.ScholarshipSingleView.as_view()),
    path('requirements/<int:id>', views.RequirementSingleView.as_view()),
]