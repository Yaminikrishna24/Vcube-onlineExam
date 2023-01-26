from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Batch
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def login(request):
    return render(request,'Registereddetails/Login.html')


def register(request):
    context={}
    rform=RegisterForm
    context['form']=rform
    if request.method == 'POST':
        obj = RegisterForm(request.POST)
        if obj.is_valid():
            obj.save()
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


