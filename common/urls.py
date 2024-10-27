from django.urls import path

from app_author.views import *
from app_book.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookListView.as_view(), name='book-detail'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorView.as_view(), name='author-detail'),
]
