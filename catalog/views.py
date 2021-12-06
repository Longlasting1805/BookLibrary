from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog.book_detail.html', context={'book': book})


def index(request):
    #  view function for home page view

    # generate counts for some of the main objects
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'new_books': num_books,
        'new instance': num_instance,
        'new instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


