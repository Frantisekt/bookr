from django.urls import path
from . import views


urlpatterns = [
    path('test/greet_user', views.greeting_view_user, name='greeting_view_user'),
    path('test/greeting', views.greeting_view, name='greeting_view')]

