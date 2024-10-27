from rest_framework import serializers

from app_book.models import BookModel


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
