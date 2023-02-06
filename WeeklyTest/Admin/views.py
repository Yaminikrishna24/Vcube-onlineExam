from django.shortcuts import render,redirect
from Registereddetails.models import userdetails
from django.http import HttpResponse
from Registereddetails import models
import string
import secrets
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string




# Create your views here.
def UserRequest(request):
    context={}
    
    if models.userdetails.objects.filter(Status='pending'):

        '''UserRequest = serialize ('json',userdetails.objects.filter(Status ='pending'))
        #jdata =json.dumps(UserRequest)
        #print(user_dict)
        context['jdata']=UserRequest
        #print(UserRequest)
        #print(jdata)'''
        
        Userrequest = userdetails.objects.all()
        
        context['users']= Userrequest
        context['header']=['First_name','Gender','Email',' Phone','Course','Batch']

        if request.method == 'POST':
            context_msg ={}
            print(request.POST)
            if 'Approve' in request.POST:
                print(request.POST)
                userdetails.objects.filter(id=request.POST['mycheck']).update(Status = 'Approved')
                letters=string.ascii_letters
                numbers = string.digits
                alpha = letters+numbers
                pwd=''
                for i in range(8):
                    pwd += ''.join(secrets.choice(alpha))
                    #print(pwd)

                obj=userdetails.objects.get(id=request.POST['mycheck'])

                user = User.objects.create_user(username=obj.Username,email=obj.Email,password=pwd)
                user.save()
                context_msg['name'] = obj.First_name
                context_msg['pwd'] = pwd
                recipient_list = [user.email,]
                template = render_to_string('student/student_approve_mail.html',context_msg)
                email = EmailMessage(
                            'Your application is Approved',
                                template,
                                settings.EMAIL_HOST_USER,
                                recipient_list)
                email.fail_silently = False
                email.send()
                #return redirect("home")
                return HttpResponse("You are approved")

            elif 'reject' in request.POST:
                userdetails.objects.filter(id=request.POST['mycheck']).update(Status = 'Rejected')




                return HttpResponse("You are rejected")
    return render(request,'Admin/home.html',context)
    
    

        