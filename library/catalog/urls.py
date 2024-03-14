from django.urls import path, re_path
from catalog.views import (index, AuthorListView, AuthorDetailView, BookListView, BookDetailView,
                           BookInstanceDetailView, reserve_book)

urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('books/', BookListView.as_view(), name='books'),
    path('reserve-book/<int:book_instance_id>/', reserve_book, name='reserve_book'),


    re_path(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^book_instance/(?P<pk>\d+)/$', BookInstanceDetailView.as_view(), name='book_instance-detail'),
]