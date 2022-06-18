

from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    if request.method == 'POST':
        newbook=Books.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
        newbook.save()
    books= Books.objects.all()
    context = {
        "books" : books
    }
    return render(request,'index.html', context)

def authors(request):
    if request.method == 'POST':
        newauth = Authors.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            notes=request.POST['notes']
        )
        newauth.save()
    author = Authors.objects.all()
    context = {
        "author": author
    }
    return render(request, 'index2.html', context)




def book(request):
    if request.method == 'POST':
        if request.POST.get('select_authors'):
            bookid = request.GET.get('book')
            book = Books.objects.get(id=bookid)
            authorid = request.POST.get("select_authors")
            author= Authors.objects.get(id=authorid)
            author.book.add(book.id)
            author.save()
    bookid = request.GET.get('book')
    book = Books.objects.get(id=bookid)
    authors_list=Authors.objects.all()
    authors= book.Authors.all()
    context={
        'book': book,
        'authors_list': authors_list,
        'authors': authors
    }

    return render(request, 'index1.html', context)


def showAuthor(request):
    if request.method == 'POST':
        if request.POST.get('select_books'):
            authorid = request.GET.get('authorid')
            author =Authors.objects.get(id=authorid)
            bookid = request.POST.get("select_books")
            print(bookid)
            book= Books.objects.get(id=bookid)
            book.Authors.add(author.id)
            author.save()
    authorid= request.GET.get('authorid')
    author = Authors.objects.get(id=authorid)
    book_list= author.book.all()
    books= Books.objects.all()
    context={
        'author': author,
        'book_list': book_list,
        'books': books
    }
    return render(request, 'index3.html', context)