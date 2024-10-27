from rest_framework.response import Response
from rest_framework.views import APIView

from app_book.models import BookModel
from app_book.serializer import BookModelSerializer


class BookListView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
