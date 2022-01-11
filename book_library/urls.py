"""book_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from catalog.views import BookListView, LoanedBooksByUserListView, renew_book_librarian, BookDetailView

from catalog import views

router = routers.DefaultRouter()
router.register(r'Books', BookListView, basename='books')
router.register(r'LoanedBook', LoanedBooksByUserListView, basename='My-borrowed')
router.register(r'renew_book_liberian', renew_book_librarian, basename='renew_book_liberian')
router.register(r'Book-Detail', BookDetailView, basename='Book-Detail')
urlpatterns = router.urls
# urlpatterns = [
#                   path('admin/', admin.site.urls),
#                   path('catalog/', include('catalog.urls')),
#                   path('books/', views.BookListView.as_view(), name='books'),
#                   path('accounts/', include('django.contrib.auth.urls')),
#                   path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#                   path('', RedirectView.as_view(url='catalog/', permanent=True)),
#                   path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
#                   path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
#
#
#               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#


# urlpatterns = [
#                   path('admin/', admin.site.urls),
#                   path('catalog/', include('catalog.urls')),
#                   path('books/', views.BookListView.as_view(), name='books'),
#                   path('accounts/', include('django.contrib.auth.urls')),
#                   path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#                   path('', RedirectView.as_view(url='catalog/', permanent=True)),
#                   path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
#                   path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
#
#               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
