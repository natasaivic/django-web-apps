from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import models
from .forms import SubscriptionForm


def index(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/confirmation/")
    else:
        form = SubscriptionForm()

    return render(request, "subscribe_app/index.html", {'form': form})

def confirmation(request):
    return render(request, "subscribe_app/confirmation.html")