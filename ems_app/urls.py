from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delate/<int:id>', views.delate, name='delate'), 
]