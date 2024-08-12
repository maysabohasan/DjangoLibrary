from django.shortcuts import render ,redirect 
from .models import *
from .forms import BookForme ,CategoryForm

# Create your views here.



def index(request):
    if request.method =='POST':
        add_book = BookForme(request.POST , request.FILES)
        if add_book.is_valid() :
            add_book.save()

        add_category =CategoryForm( request.POST)
        if add_category.is_valid() :
            add_category.save()
    context ={
        'category' : Category.objects.all(),
        'book' : Book.objects.all(),
        'form' : BookForme() ,
        'formCat' :CategoryForm() ,
        'allBooks' :Book.objects.filter(active=True).count ,
        'bookSold' :Book.objects.filter(status='sold').count ,
        'bookRental' :Book.objects.filter(status='rental').count ,
        'bookAvailable' :Book.objects.filter(status='available').count ,

    }
    return render(request, 'pages/index.html' ,context)

def books(request):
    context ={
        'category' : Category.objects.all(),
        'book' : Book.objects.all(), 
        }
    
    return render(request, 'pages/books.html' ,context)

def update(request , id) :
    book_id=Book.objects.get(id=id)
    if request.method =='POST' :
        book_save =BookForme(request.POST ,request.FILES , instance=book_id)
        if book_save.is_valid() :
            book_save.save()
            return redirect('/')
    else:
        book_save =BookForme(instance=book_id)

    context = {
        'form' :book_save
    }  
    return render(request,'pages/update.html', context)  

def delate(request ,id) :
    book_delate= Book.objects.get(id=id) 
    if request.method =='POST' :
        book_delate.delete()
        return redirect()
    return render (request ,'pages/delate.html' )