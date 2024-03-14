from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()
    num_book_instances_available = BookInstance.objects.filter(status__exact='Available').count()

    return render(request, 'index.html', {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_book_instances": num_book_instances,
        "num_book_instances_available": num_book_instances_available

    })


class AuthorListView(ListView):
    model = Author
    template_name = 'authors_list.html'
    context_object_name = 'authors_list'


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class BookListView(ListView):
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books_list'


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookInstanceDetailView(DetailView):
    model = BookInstance
    template_name = 'book_instance_detail.html'


@login_required
def reserve_book(request, book_instance_id):
    book_instance = get_object_or_404(BookInstance, id=book_instance_id)
    user_past_loans = BookInstance.objects.filter(borrower=request.user, status='On Loan',
                                                  due_book__lt=timezone.now().date())

    if user_past_loans.exists():
        return render(request, 'reserve_error.html', {'error': 'You have overdue books.'})
    elif book_instance.status == 'Available':
        if BookInstance.objects.filter(borrower=request.user, status='On Loan').exists():
            return render(request, 'reserve_error.html', {'error': 'You already have a '
                                                                   'book on loan.'})

        try:
            book_instance.status = 'On Loan'
            book_instance.due_book = timezone.now().date() + timedelta(weeks=2)
            book_instance.borrower = request.user
            book_instance.save()
            return redirect('reserved_books')
        except Exception as e:
            return render(request, 'reserve_book.html', {'error': str(e)})
    else:
        return render(request, 'reserve_error.html', {'error': 'The book instance is not '
                                                               'available for reservation.'})