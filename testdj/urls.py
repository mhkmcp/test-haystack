
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('filter.urls')),
    url(r'^search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
]
