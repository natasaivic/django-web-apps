from django.shortcuts import redirect, render
from .forms import PostForm


def index(request):
    return render(request, "microblog_app/index.html")


def post(request):
    return render(request, "microblog_app/post.html")


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, "microblog_app/post.html", {'form': form}) 
