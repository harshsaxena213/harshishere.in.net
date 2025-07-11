from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .forms import ContactForm 
import datetime
from django.core.mail import send_mail
import uuid

def connect(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ref = str(uuid.uuid4())[:8].upper()
            with open("data.txt","a+") as temp:
                temp.write(f"{name}, {email}, {message}, {datetime.datetime.now()},{ref}\n")
            try:
                send_mail("New Contact Recieved!",f"The Name Of Person Is:- {name} And His Email Acc To Him Is:-{email} And His Message Is\n{message} \n\n And His Refrance Is {ref}","xxxxx",["xxxxxx"])
                send_mail("Successfully Recieved!",f"Hey {name} \n I Have Successfully Recieved You Message And Will Contact You Soon This Is An Auto Genrated Email Please Do't Reply To This Email Your Refrance Number Is \n{ref}\n Please Keep This Refrance Number Safely We Might Need This To Confirm Your Legitimacy \n\nThankYou For Visiting\nRegards\nHarshit Saxena","xxxx",[f"{email}"])
            except Exception as Error:
                send_mail(f"We Have An Error And It Goes Like This \n\n{Error}")
                with open("error.txt","a+") as er:
                    er.write(f"The Error Is \n\n{Error} And Time And Date Is {datetime.datetime.now()}")
                return render(request,"error.html")
           
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'connect.html', {'form': form})
