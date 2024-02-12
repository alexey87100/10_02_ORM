from django.urls import path

from .views import index, profiles_by_skill


app_name = 'main'

urlpatterns = [
    path('', index, name='main_page'),
    path('skill/<slug:slug>/', profiles_by_skill, name='skill_page')
]
