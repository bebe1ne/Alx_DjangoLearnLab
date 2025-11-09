from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Library
from .models import Library
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
def index(request):
    return HttpResponse("Hello, this is the Relationship App page.")


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('library_detail')  # Redirect to a meaningful URL
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
