from django.urls import path, include
from . import views
# from .views import BookList, BookDetail, AuthorList, AuthorDetail/
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

# router = routers.NestedDefaultRouter()
# router.register("books", views.BookViewSet, "books")
# print(router.urls)
#
# router.register("authors", views.AuthorViewSet, "authors")
# print(router.urls)
#
# router.register("reviews", views.ReviewViewSet, "reviews")
router = routers.DefaultRouter()
router.register("books", views.BookViewSet, 'book')
router.register("author", views.AuthorViewSet, "author")

review_router = routers.NestedDefaultRouter(router, "books", lookup="book")
review_router.register("reviews", views.ReviewViewSet, "review")

urlpatterns = router.urls + review_router.urls

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# path('books/', BookList.as_view(), name='books'),
# path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
# path('authors/', AuthorList.as_view(), name='authors'),
# path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
