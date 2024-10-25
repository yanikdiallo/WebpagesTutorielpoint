from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import (
                    GeneralInfo,Service,Testimonial,
                     frequentlyQuestion,ContactFormLog)
from django.core.mail import send_mail 
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone

# Create your views here.


def index(request):

    general_infos = GeneralInfo.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = frequentlyQuestion.objects.all()
    context={
        "location": general_infos.location,
        "email": general_infos.email,
        "phone": general_infos.phone,
        "open_hours": general_infos.open_hours,
        "video_url": general_infos.video_url,
        "twitter_url": general_infos.twitter_url,
        "facebook_url " : general_infos.facebook_url,
        "instagram_url": general_infos.instagram_url,
        "linkedin_url": general_infos.linkedin_url,

        'services': services,
        'testimonials':testimonials,
        'faqs':faqs



    }
    return render(request,'index.html',context)


def contact_form(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        context = {
            'name':name,
            'email':email,
            'subject': subject,
            'message':message,
        }
        html_content = render_to_string('email.html',context)

        is_succes= False
        is_error = False
        error_message= ""

        try:
            send_mail(
                subject=subject,  
                message=None,           # Subject of the email
                html_message= html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER] , 
                fail_silently=False         # Body of the email
                
        )  
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request,"Error sur l'envoi du formulaire ") 
        else:
           is_succes = True
           messages.success(request,"Email envoye avec succes ")


        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject, 
            message=message,
            action_time = timezone.now(),
            is_succes = is_succes,
            is_error = is_error,
            error_message=error_message,


        )
        
    return redirect('home')
    



