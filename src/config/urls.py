
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app.router import app_url
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name=""),
    path('admin/', admin.site.urls),
    path("api/", include(app_url))
]
