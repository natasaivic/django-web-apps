from django.shortcuts import render

from .forms import DocumentForm
from .models import Document


def index(request):
    # handle file upload
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'app/index.html', {'documents': documents, 'form': form})
    
