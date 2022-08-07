from django.urls import path
from institutions import views

urlpatterns = [
    path('', views.InstitutionView.as_view()),
    path('contact/', views.ContacPersonView.as_view()),
]