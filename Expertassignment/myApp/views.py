from django.shortcuts import render, redirect
from .forms import AssignmentForm
from .models import Myapp
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')  

def gauranteedmarks(request):
    return render(request, 'gauranteedMarks.html')

def whyus(request):
    return render(request, 'whyus.html')


def contact_success(request):
    return render(request, 'contact_success.html')

def result(request):
    return render(request, 'result.html')

def about(request):
    return render(request, 'about.html')

def success(request):
    return render(request, 'success.html')

def megaoffer(request):
    return render(request, 'megaoffer.html')

def list_result(request):
    return render(request, 'list.html')



def success_email(request):
    return render(request, 'success_email.html')



@csrf_exempt
def order(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = AssignmentForm()
    
    return render(request, 'order.html', {'form': form})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page or render a message
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

    





#  for Pop up Form for sending email 
def send_email(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['title'],
                message=form.cleaned_data['name'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your@email.com'],
            )
            return redirect('success_email')
    else:
        form = AssignmentForm()
    return render(request, 'assignment_form.html', {'form': form})
