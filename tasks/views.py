from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Subcategory, Subsub

def home(request):
    cat = Category.objects.all()
    sub = Subcategory.objects.all()
    susub = Subsub.objects.all()
    for i in cat:
        for j in sub: 
            for k in susub:
                if k.subsub == j:
                    print(k.subsubname)
            print(end='/n')
    return render(request, 'home.html', {'cat': cat, 'sub': sub, 'susub': susub})
