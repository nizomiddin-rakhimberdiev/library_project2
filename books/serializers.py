from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')


    def validate(self, attrs):
        title = attrs.get('title', None)
        author = attrs.get('author', None)

        if not isinstance(title, str):
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob nomi str formatda bo'lishi kerak"
                }
            )
        return attrs

    def validate_price(self, price):
        if price < 0 or price > 9999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob narxi noto'g'ri kiritilgan"
                }
            )
