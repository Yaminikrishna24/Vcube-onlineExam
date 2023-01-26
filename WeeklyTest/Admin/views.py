from django.shortcuts import render
from Registereddetails.models import userdetails




# Create your views here.
def UserRequest(request):
    context={}
    Userrequest=userdetails.objects.all()
    context['users']= Userrequest
    context['header']=['First_name','Gender','Email',' Phone','Course','Batch']
    return render(request,'Admin/home.html',context)
    

        