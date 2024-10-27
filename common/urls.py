from django.urls import path

from app_book.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookListView.as_view(), name='book-detail'),
]
