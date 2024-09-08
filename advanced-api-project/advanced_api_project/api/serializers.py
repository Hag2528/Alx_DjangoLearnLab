from rest_framework import serializers
from .models import Author, Book
from django.utils import date

class BookSerializer(serializers.ModelSerializer):
    # Serializer for the Book model, including validation for publication year.
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication year is not in the future.
        """
        from datetime import date
        if value > date.today().year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model, including nested BookSerializer.
    """
    books = BookSerializer(source='book_set', many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('name', 'books')

    def to_representation(self, instance):
        """
        Override the default behavior to include only published books
        (publication year is not in the future) in the nested list.
        """
        response = super().to_representation(instance)
        response['books'] = [book for book in response['books'] if book['publication_year'] <= date.today().year]
        return response