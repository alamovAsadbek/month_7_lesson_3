from django.urls import path

from app_author.views import *
from app_book.views import *

urlpatterns = [
    path('books/', BookView, name='books'),
    path('books/<int:pk>/', BookDetailView, name='book-detail'),
    path('authors/', AuthorView, name='authors'),
    path('authors/<int:pk>/', AuthorDetailView, name='author-detail'),
]
