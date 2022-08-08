from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin', admin.site.urls),
    path('institutions/', include('institutions.urls')),
    path('students/', include('students.urls')),
    path('scholarships/', include('scholarships.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)