from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from .utils import average_rating

def book_list(request):
    "This code retrieves an set of the books inside our database based on their reviews."
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating= average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'reviews/books_list.html', context)


def book_details(request, pk):  
    "This code lists the book's details associated to each book."
    book = get_object_or_404(Book, pk=pk)
    reviews =  Review.objects.filter(book__pk=pk)
 
    book_rating = average_rating([review.rating for review in reviews])

    book_details = []
    review_list = []
    
    for review in reviews:
        review_list.append({'review': review,})
        
    book_details.append({'book': book, 'book_rating': book_rating})
    context = {'book_details': book_details, 'review_list': review_list}
    print(context)
    return render(request, 'reviews/book_details.html', context)







