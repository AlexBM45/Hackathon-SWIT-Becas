from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls),
    path('institutions/', include('institutions.urls')),
    path('students/', include('students.urls')),
    path('scholarships/', include('scholarships.urls'))
]