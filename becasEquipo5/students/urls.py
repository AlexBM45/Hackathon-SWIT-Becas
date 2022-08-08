from django.urls import path
from students import views

urlpatterns = [
    path('', views.StudentView.as_view()),
    path('<int:id>', views.StudentSingleView.as_view()),
]