from django.shortcuts import redirect, render
from .forms import SubscribeForm

def home(request):
    return render(request, "resume_app/home.html")

def experience(request):
    return  render(request, "resume_app/experience.html")

def qa(request):
    return render(request, "resume_app/qa.html")

def subscribe_form(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/confirmation/')
    else:
        form = SubscribeForm()
    return render(request, "resume_app/form.html", {'form': form}) 

def confirmation(request):
    return render(request, "resume_app/confirmation.html")

def contact(request):
    return render(request, "resume_app/contact.html")
