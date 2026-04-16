from django.urls import path
from .views import list_books, book_detail, create_book, scrape_and_save
from .views import list_books, book_detail, create_book, scrape_and_save, book_insights
from .views import list_books, book_detail, create_book, scrape_and_save, book_insights, ask_question
urlpatterns = [
    path('books/', list_books),
    path('books/<int:id>/', book_detail),
    path('books/create/', create_book),
    path('scrape/', scrape_and_save),
    path('books/<int:id>/insights/', book_insights),
    path('ask/', ask_question),
]
