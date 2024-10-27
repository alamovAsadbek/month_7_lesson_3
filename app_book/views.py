from rest_framework.views import APIView

from app_book.models import BookModel
from app_book.serializer import BookModelSerializer


class BookListView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookModelSerializer(books, many=True)
