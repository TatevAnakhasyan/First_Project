from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Any
from django.views.generic import ListView, DeleteView
from .models import *
from .forms import ContactUsForm
from django.core.mail import send_mail
from Shop.settings import EMAIL_HOST_USER


class HomeListView(ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():
        blogs = Blog.objects.all()
        home = HomeBG.objects.get()
        service = OurService.objects.get()
        galleries = OurGallery.objects.all()
        about = AboutUs.objects.get()
        contacttxt = ContactTxt.objects.get()
        icons = ServiceIcons.objects.all()

        context = {
            'blogs':blogs,
            'home':home,
            'service':service,
            'galleries':galleries,
            'about':about,
            'contacttxt':contacttxt,
            'icons':icons
        }

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        context = self.__extract_all_data()

        return render(request, self.template_name, context=context)
    
    def post(self, request):
        context = self.__extract_all_data()

        form = ContactUsForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            send_mail(
                subject= 'Shop FeedBack',
                message= 'Thanks For Review',
                from_email= EMAIL_HOST_USER,
                recipient_list= [email],
                fail_silently=False
            )

            form.save()
        else:
            form = ContactUsForm()

        context.update({'form':form})

        return render(request, self.template_name, context= context)




    
