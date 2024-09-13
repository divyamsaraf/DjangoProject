from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('user/update/<int:id>/', views.update_user, name='update_user'),
    path('user/partail_update/<int:id>/', views.partial_update_user, name='partial_update_user'),
    path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
]