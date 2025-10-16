from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly  # new permission


class BookViewSet(viewsets.ModelViewSet):
    """
    Admins: full CRUD on books
    Members: read-only access
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
