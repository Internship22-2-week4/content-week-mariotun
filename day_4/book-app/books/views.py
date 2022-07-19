#from django.shortcuts import render
# Create your views here.
#from django.http import HttpResponse

#Django rest framework
from rest_framework.views import Response
from rest_framework import viewsets

#models
from .models import Book,Author,Category

#serializers
from .serializers import BookSerializer,AuthorSerializer,CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



"""
def index(request):
    #return HttpResponse('app book')
    books=Book.objects.all()
    print('----> ',books)
    return render(request,'books/index.html',{
        'books_list':books
    })

def author(request,author_id):
    author = Author.objects.get(id=author_id)
    return render(request,'books/author.html',{
        'author':author
    })
    # return HttpResponse('author id: {}'.format(author_id))

def category(request,category_id):
    return HttpResponse('category id: {} '.format(category_id))
"""