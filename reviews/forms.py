from django import forms
from .models import Publisher, Review, Book

SEARCH_CHOICES = (("title", "Title"), ("contributor", "Contributor"))

class SearchForm(forms.Form):
    """This would help us render a list
    of Books that contain the same tittle or 
    first or last name of Contributor"""
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES, initial="title")
    

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    """Activity 7.02"""
    rating = forms.IntegerField(min_value=0, max_value=5)
    
    class Meta:
        model = Review
        exclude = ("book", "date_edited")
        

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("cover", "sample")
    