from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *


class AuthorView(APIView):
    def get(self, request):
        authors = AuthorModel.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
