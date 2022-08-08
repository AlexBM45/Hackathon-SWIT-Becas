from django.urls import path
from applications import views

urlpatterns = [
    path('', views.ApplicationView.as_view()),
    path('<int:id>', views.ApplicationSingleView.as_view()),
]