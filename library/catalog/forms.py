from django import forms
from catalog.models import BookInstance


class BookReservationForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'due_book']

    def save(self, user, commit=True):
        book_instance = super().save(commit=False)
        book_instance.borrower = user
        book_instance.status = 'On Loan'
        if commit:
            book_instance.save()
        return book_instance