from django.urls import path
from . import views
 

urlpatterns = [
    
    path('register',views.register,name='register'),
    path('',views.login,name='login'),
    path('ajax/load-batches/', views.load_batches, name='ajax_load_batches'),
    path('success', views.success, name="success"),

]