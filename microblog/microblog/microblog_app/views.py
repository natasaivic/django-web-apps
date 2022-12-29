from django.shortcuts import render

def index(request):
    return render(request, "microblog_app/index.html")
