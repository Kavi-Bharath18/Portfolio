from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('success/', lambda request: render(request, 'portfolio/success.html'), name='success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)