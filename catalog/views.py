from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    #  view function for home page view

    # generate counts for some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'new_books': num_books,
        'new instance': num_instance,
        'new instances_available': num_instances_available,
        'num_authors': num_authors,
    }

# Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
