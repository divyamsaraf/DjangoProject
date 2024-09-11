from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]