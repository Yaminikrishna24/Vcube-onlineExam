from django.urls import path
from . import views
 

urlpatterns = [
    
    path('userRequest',views.UserRequest,name='userRequest'),
    

]