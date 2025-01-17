from django import forms
from .models import Book ,Category

class CategoryForm(forms.ModelForm) :
    class Meta :
        model =Category
        fields = ['name']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}) 
        }
        

class BookForme(forms.ModelForm) :
    class Meta :
        model = Book
        fields = ['title' 
                , 'author' 
                , 'photo_book'
                , 'photo_author'
                , 'pages' ,'price'
                , 'retal_price_day'
                , 'retal_period' 
                ,'total_rental'
                , 'status'
                , 'Category'
                
                ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}) ,
            'author': forms.TextInput(attrs={'class': 'form-control'}) ,
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}) ,
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}) ,
            'pages': forms.NumberInput(attrs={'class': 'form-control'}) ,
            'price': forms.NumberInput(attrs={'class': 'form-control'}) ,
            'retal_price_day': forms.NumberInput(attrs={'class': 'form-control' , 'id':'rentalPrice'}) ,
            'retal_period': forms.NumberInput(attrs={'class': 'form-control', 'id':'rentalDay'}) ,
            'total_rental': forms.NumberInput(attrs={'class': 'form-control' , 'id':'totalRental'}) ,
            'status': forms.Select(attrs={'class': 'form-control'}) ,
            'Category': forms.Select(attrs={'class': 'form-control'}) ,

}

