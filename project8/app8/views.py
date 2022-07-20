from django.shortcuts import render
from app8.forms import form_class_name
# Create your views here.

def func_view_name(request):
    form=form_class_name()
    if request.method=='POST':
        name=request.POST['name']
        qty=request.POST['quantity']

        #we can store the data like dict
        request.session[name]=qty

    return render(request,'html/html1.html',{'form':form})

def display_name_qty(request):
    return render(request,'html/html2.html')