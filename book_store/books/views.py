
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        book = Book.objects.filter(pk=pk)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book = Book.objects.filter(pk=pk).first()
        serializer = BookSerializer(data=request.data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        book = Book.objects.filter(pk=pk).first()
        serializer = BookSerializer(data=request.data, instance=book, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        book = Book.objects.filter(pk=pk).first()
        book.delete()
        return Response({"Results": "Successfully deleted"}, status=status.HTTP_200_OK)
