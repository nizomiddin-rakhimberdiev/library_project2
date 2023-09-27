from django.urls import path
from rest_framework.routers import SimpleRouter

from books.views import (
    BookListApiView,
    BookCreateApiView,
    BookDetailApiView,
    BookDeleteApiView,
    BookUpdateApiView, BookViewSet
)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls
