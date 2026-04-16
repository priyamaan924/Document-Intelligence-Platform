from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from scraper.scraper import scrape_books
from ai.ai_utils import generate_summary, classify_genre, recommend
from rag.retrieval import add_documents, search
from rag.generator import generate_answer

@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question")

    books = Book.objects.all()
    docs = [b.description for b in books]

    # ✅ Fix: only add if docs exist
    if docs:
        add_documents(docs)

    context = search(question)
    answer = generate_answer(question, context)

    return Response({
        "question": question,
        "answer": answer,
        "context": context
    })

@api_view(['GET'])
def book_insights(request, id):
    book = Book.objects.get(id=id)

    summary = generate_summary(book.description)
    genre = classify_genre(book.description)
    recommendations = recommend(book.title)

    return Response({
        "title": book.title,
        "summary": summary,
        "genre": genre,
        "recommendations": recommendations
    })

@api_view(['POST'])
def scrape_and_save(request):
    data = scrape_books()

    for book in data:
        Book.objects.create(**book)

    return Response({"message": "Books scraped and saved"})

# GET all books
@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# GET single book
@api_view(['GET'])
def book_detail(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

# POST create book
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)