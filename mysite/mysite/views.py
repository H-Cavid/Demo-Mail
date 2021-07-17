from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request, 'home.html')

# class Home(TemplateView):
#     template_name= 'home.html'

def send_gmail(request):
    if request.method == "POST":
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message = request.POST.get('message')
        print(name,subject,message)

        #send an email
        send_mail(
            subject,#subject
            message,#messages
            'pragmatechbuild@gmail.com',#from email
            ['cavid.hasanov2@bk.ru'],#To email
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse("Invalid request")