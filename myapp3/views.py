from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            author = formdata['author']
            Book.objects.create(title=title, author=author)
            return redirect('home')  # Changed from HttpResponseRedirect('/success')
    else:
        form = CreateBookForm()
    books = Book.objects.all()
    return render(request, 'myapp3/createbook.html', {'form': form, 'books': books})


def success(request):
    return render(request, 'myapp3/success.html')

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('home')
    return render(request, 'myapp3/update_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'myapp3/delete_book.html', {'book': book})
