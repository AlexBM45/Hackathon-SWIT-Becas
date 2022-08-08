from django.urls import path
from institutions import views

urlpatterns = [
    path('', views.InstitutionView.as_view()),
    path('<int:id>', views.InstitutionSingleView.as_view()),
    path('contacts/', views.ContactView.as_view()),
]