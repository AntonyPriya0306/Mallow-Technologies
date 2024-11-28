from django.shortcuts import render,redirect
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request,'index.html')    
    
def bill(request):
    email=request.GET["email"]
    product=request.GET["product"]
    quantity=int(request.GET["quantity"])
    unitprice=200
    tax=5/100
    totalprice=quantity*unitprice
    taxpay=tax*totalprice
    total=totalprice+taxpay
    cash=int(request.GET["cash"])
    remaining=cash-total
    return render(request,'show.html',{'Email':email,'Product':product,
                                       'Quantity':quantity,'Unitprice':unitprice,'Tax':tax,'Totalprice':totalprice,
                                       'Taxpay':taxpay,'Total':total,'Cash':cash,'Balance':remaining})


