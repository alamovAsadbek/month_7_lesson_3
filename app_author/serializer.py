from rest_framework import serializers

from .models import *


class AuthorModelSerializer(serializers.Serializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'
