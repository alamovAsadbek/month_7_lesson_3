from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *


@api_view(['GET', 'POST'])
def AuthorView(request):
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        print(authors)
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def AuthorDetailView(request, pk):
    if request.method == 'GET':
        author = AuthorModel.objects.get(pk=pk)
        serializer = AuthorModelSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PUT':
        author = AuthorModel.objects.get(pk=pk)
        serializer = AuthorModelSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        author = AuthorModel.objects.get(pk=pk)
        author.delete()
        return Response(status=204)
