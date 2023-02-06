from django.urls import path
from . import views
 

urlpatterns = [
    
    path('register',views.register,name='register'),
    path('',views.login,name='login'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('change_password/<token>',views.change_password,name='change_password'),
    path('ajax/load-batches/', views.load_batches, name='ajax_load_batches'),
    path('success', views.success, name="success"),

]