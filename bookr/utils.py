import datetime

from django.db.models import Count
from reviews.models import Review

def get_books_read_by_month(username):
    """Generate the books read by the user in per montg basis.

    :param: str The username for which the books needs to be returned
    :return: dic of month wise books read.
    """
    current_year = datetime.datetime.now().year
    books = Review.objects.filter(creator__username__contains=username, date_created__year=current_year).values('date_created__month').annotate(book_count=Count('book__title'))
    return books


def get_books_read(username):
    books = Review.objects.filter(creator__username__contains=username).all()
    return [{'title': book_read.book.title, 'completed_on': book_read.date_created} for book_read in books]
    