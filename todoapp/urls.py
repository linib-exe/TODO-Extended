from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('register/',register,name='register'),
    path('create/',create,name='create'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('details/<int:id>',details,name='details'),
]