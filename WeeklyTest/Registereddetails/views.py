from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Batch
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login
import uuid
from .forget_password_mail import send_forget_password_mail


# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request,username=user_name,password=password)
        if user is not None:
            #login(request,user)
            if user.is_superuser:
                messages.info(request, f"You are now logged in as {user_name}.")
                return redirect('Admin/userRequest')

                
            else:
                messages.info(request, f"You are now logged in as {user_name}.")
                return render(request,'student/home.html')
        else:
            messages.info(request,'Enter Valid Username and Password')
    return render(request,'Registereddetails/Login.html')

def forget_password(request):
    if request.method == "POST":
        username = request.POST['username']
        if not User.objects.filter(username=username).first():
            messages.success(request,"No user found with this username")
            return redirect('forget_password')
        user_obj = User.objects.get(username=username)
        print(user_obj.email)
        recipient_list = [user_obj.email,]
        
        token = str(uuid.uuid4())
        email = EmailMessage(
                            'Your Forget Password Link',
                            f'Hi,click on the link to reset your Password http://127.0.0.1:8000/change_password/{token}',
                            settings.EMAIL_HOST_USER,
                            recipient_list)
        email.fail_silently = False
        email.send()
        #send_forget_password_mail(user_obj.email,token)
        messages.success(request,"An Email sent")
        return redirect('forget_password')
    return render(request,'Registereddetails/forget_password.html')


def change_password(request,token):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        update_password = User.objects.get(username=username)
        update_password.set_password(password)
        update_password.save()
        messages.success(request,"Password Updated,Please Login")
        return redirect('login')
    return render(request,"Registereddetails/change_password.html")

def register(request):
    context={}
    rform=RegisterForm
    context['form']=rform
    if request.method == 'POST':
        #request.POST['Batch'] = int(request.POST['Batch'])
        obj = RegisterForm(request.POST)
        #print(request.POST)
        if obj.is_valid():
            obj.save()
        #print(obj.errors)

        template = render_to_string('Admin/admin_email_template.html',{'name':request.POST['First_name']})
        email = EmailMessage(
            'Student request to Account Approval',
            template,
            settings.EMAIL_HOST_USER,
            ['yaminikrishna24@gmail.com']
        )
        email.fail_silently = False
        email.send()
        return redirect("success")
            #return redirect('Admin/userRequest')



    return render(request,'Registereddetails/register.html',context)

def success(request):
    return HttpResponse('Mail sent Successfully')

def load_batches(request):
    context={}
    course_id=request.GET.get('Course')
    batches=Batch.objects.filter(course_id=course_id).order_by('Batch_name')
    context['batches'] = batches
    return render(request,'Registereddetails/branch_dropdown_list.html',context)


