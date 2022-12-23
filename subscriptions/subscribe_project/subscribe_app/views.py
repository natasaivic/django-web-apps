from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models
from .forms import SubscriptionForm


def index(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('You have been successfully subscribed!')
    else:
        form = SubscriptionForm()

    return render(request, "subscribe_app/index.html", {'form': form})