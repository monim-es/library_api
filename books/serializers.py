from rest_framework import serializers
from .models import Book, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



# from django.contrib.auth.models import User

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date', 'returned']
