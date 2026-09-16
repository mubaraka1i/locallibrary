from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    
    num_authors = Author.objects.count()

    num_genres_politic = Genre.objects.filter(name__icontains='politic').count()
    num_books_politic = Book.objects.filter(title__icontains='politic').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_politic': num_genres_politic,
        'num_books_politic': num_books_politic,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)