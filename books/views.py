from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Book

from books.serializers import BookSerializer


# Create your views here.
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer_data = BookSerializer(queryset, many=True).data
        data = {
            'status': f'Returned {len(queryset)} books',
            'data': serializer_data
        }
        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book)
            data = {
                'status': f'Returned {book.id}-book',
                'book': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            data = {
                'status': False,
                'message': 'Book is not found'
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': 'Books is saved to database',
                'book': data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'status': 'Data is not valid',
                'message': 'Book is not created'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serilizer = BookSerializer(instance=book, data=data, partial=True)
        if serilizer.is_valid(raise_exception=True):
            book_saved = serilizer.save()
        return Response(
            {
                'status': True,
                'message': f"Book {book_saved} updated successfully"
            }

        )


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
