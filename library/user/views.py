from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from catalog.models import BookInstance
from datetime import datetime, timedelta
from django.utils import timezone



class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


@login_required
def user_reserved_books(request):
    user = request.user
    reserved_books = BookInstance.objects.filter(borrower=user)
    current_time = timezone.localtime(timezone.now())
    maximum_duration = timedelta(weeks=2)

    for book_instance in reserved_books:
        due_book_local = timezone.localtime(book_instance.due_book)
        time_elapsed = current_time - due_book_local
        remaining_time = maximum_duration - time_elapsed
        book_instance.remaining_duration = max(remaining_time, timedelta())

    return render(request, 'user_reserved_books.html', {'reserved_books': reserved_books})