from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post

from django.core.paginator import Paginator


def index(request):
    uploaded_data = Post.objects.all()
    paginator = Paginator(uploaded_data, 2) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "microblog_app/index.html", {'uploaded_data': uploaded_data, 'page_obj': page_obj})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()

    return render(request, "microblog_app/new_post.html", {'form': form})
