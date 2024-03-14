from django.urls import path
from user import views
from user.views import user_reserved_books



urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('user/reserved-books/', user_reserved_books, name='user_reserved_books'),
]
