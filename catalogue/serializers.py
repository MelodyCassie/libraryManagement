from rest_framework import serializers

from .models import Book, Author, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_detail'
    # )

    class Meta:
        author = serializers.StringRelatedField
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']

    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=1000)
    # isbn = serializers.CharField(max_length=20)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'message', 'date']

    def created(self, validated_data):
        book_id = self.context['book_pk']
        Review.objects.create(book_id=book_id, **validated_data)
