from django.contrib import admin
from catalog.models import Author, Genre, Language, Book, BookInstance, Country


class BookInLine(admin.TabularInline):
    model = Book


class BookInstanceInLine(admin.StackedInline):
    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'pseudonym']
    search_fields = ['pseudonym', 'first_name', 'last_name']
    inlines = [BookInLine]


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    search_fields = ['title', 'author__first_name', 'author__last_name', 'author__pseudonym', 'genre__name']
    inlines = [BookInstanceInLine]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'isbn', 'status']
    fieldsets = (
        ('Group 1', {
            'fields': ('book', 'isbn', 'language')
        }),
        ('Group 2', {
            'fields': ('borrower', 'due_book', 'status')

        })
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
