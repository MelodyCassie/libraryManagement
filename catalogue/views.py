
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author, Review
from .pagination import DefaultPagination
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
import segno


# Create your views here.


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class BookList(APIView):
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)


class BookList(ListCreateAPIView):
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Book.objects.all()

    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filter_set_fields = ["title", "genre", "summary"]
    # def get_serializer_context(self):
    #     return {"request": self.request}


# @api_view(["GET", "PUT", "DELETE"])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == "GET":
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, pk):
#         book = get_object_or_404(Book, id=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# @api_view(['GET', 'POST'])
# def author_list(request, ):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#

# class AuthorList(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    searchFields = ["firstname", "lastname"]
    ordering_fields = ["first_name"]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr("Welcome to django")
#         author_qrcode.save('welcome.png')
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class AuthorDetail(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, id=pk)
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr("Welcome to django")
#         author_qrcode.save('welcome.png')
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, id=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#     def delete(self, pk):
#         author = get_object_or_404(Author, id=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     author_qrcode = segno.make_qr("Welcome to django")
#     author_qrcode.save('welcome.png')
# # try:
#     book = Book.objects.get(id=id)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)
# except Book.DoesNotExist:
#     Response(status=status.HTTP_404_NOT_FOUND)
