
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import KidCanOnlyViewUnder18Books
from .models import Book
from .serializers import BookSerializer
# Create your views here.

# Admin can view, add, delete all books


class BookViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            permission_classes = (IsAdminUser, )
        else:
            permission_classes = (KidCanOnlyViewUnder18Books, )
        return [permission() for permission in permission_classes]

    def get_object(self, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return book

    def get_queryset(self):
        if self.request.user.is_kid:
            user_age = self.request.user.age
            return Book.objects.filter(pg=user_age)
        return Book.objects.all()

    @action(detail=False)  # detail=False; return a list of object
    def list(self, request):
        books = self.get_queryset()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # @action; creates a custom action for urls
    @action(detail=False, permission_classes=(KidCanOnlyViewUnder18Books, ))
    def retrieve(self, request, pk=None):
        book = self.get_object(pk=pk)
        self.check_object_permissions(request, book)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(data=request.data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        book = self.get_object(pk=pk)
        serializer = BookSerializer(data=request.data, instance=book, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        book = self.get_object(pk=pk)
        book.delete()
        return Response({"Results": "Successfully deleted"}, status=status.HTTP_200_OK)
