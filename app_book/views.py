from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_book.models import BookModel
from app_book.serializer import BookModelSerializer


@api_view(['GET', 'POST'])
def BookView(request):
    if request.method == 'GET':
        books = BookModel.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def BookDetailView(request, pk):
    if request.method == 'GET':
        book = BookModel.objects.get(pk=pk)
        serializer = BookModelSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        book = BookModel.objects.get(pk=pk)
        serializer = BookModelSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        book = BookModel.objects.get(pk=pk)
        book.delete()
        return Response(status=204)
