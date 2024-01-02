from django.shortcuts import render , redirect, get_list_or_404
from .models import *
from django.db.models import Sum
from .forms import BookForm
from django.http import response

def index(request  ):

    if request.method == 'POST':

        form = BookForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('success_page/')
    
    else:
        form = BookForm()


    context = {

        'AllBooks': Books.objects.all(),

        'AvailableBooks': Books.objects.filter(status="متاح"),

        'SoldBooks': Books.objects.filter(status="تم بيعه"),

        'RentedBooks': Books.objects.filter(status="مستعار"),

        'pricesBooks': Books.objects.aggregate(total_price_sum=Sum('price'))['total_price_sum'],

        'borrowedpricesum' : Books.objects.filter(status='مستعار').aggregate(total_borrowed_price=Sum('price'))['total_borrowed_price'],

        'Soldsum' : Books.objects.filter(status="تم بيعه").aggregate(total_borrowed_price=Sum('price'))['total_borrowed_price'],

        'Tasnif' : Tasnif.objects.all(),

        'form' : form
                   

    }

    return render(request, 'index.html' , context)


def index_cat(request , id  ):

    context = {

        'AllBooks': Books.objects.all(),

        'AvailableBooks': Books.objects.filter(status="متاح"),

        'SoldBooks': Books.objects.filter(status="تم بيعه"),

        'RentedBooks': Books.objects.filter(status="مستعار"),

        'pricesBooks': Books.objects.aggregate(total_price_sum=Sum('price'))['total_price_sum'],

        'borrowedpricesum' : Books.objects.filter(status='مستعار').aggregate(total_borrowed_price=Sum('price'))['total_borrowed_price'],

        'Soldsum' : Books.objects.filter(status="تم بيعه").aggregate(total_borrowed_price=Sum('price'))['total_borrowed_price'],

        'Tasnif' : Tasnif.objects.all(),

        'Tas' : Books.objects.filter(category = id),
                       

    }

    return render(request, 'index_cat.html' , context)




def home(request):

    search=Books.objects.all()

    name = None

    if 'search_name' in request.GET:

        name = request.GET['search_name']

        if name :

            search = search.filter(name__icontains=name)



    context = {

        'AllBooks': search

    }



    return render(request ,'books.html' , context )



def success(request):

    return render(request ,'success_page.html')




def delete(request , id):


    book_delet = Books.objects.get( id = id)

    if request.method == 'POST':

        book_delet.delete()

        return redirect('http://127.0.0.1:8000/Books/')


    return render(request ,'delete.html')


def update(request , id ):

    book_id= Books.objects.get(id=id)

    if request.method == 'POST':

        book_save = BookForm (request.POST, request.FILES, instance=book_id)

        if book_save.is_valid():

            book_save.save()
    else:
        book_save = BookForm (instance=book_id)

    context = {

    'form' :book_save,

    }

    return render(request , 'update.html', context )  # 



def Book_buy(request , id):

    context = {

        'Book_buy' : Books.objects.get(id = id),
    }



    return render(request , 'buy_book.html' , context )