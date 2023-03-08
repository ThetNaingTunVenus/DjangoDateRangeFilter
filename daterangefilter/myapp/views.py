from django.shortcuts import render
from .models import *

# Create your views here.
def result(request):
    if request.method == 'POST':
        fromdate = request.POST.get('from')
        todate = request.POST.get('to')
        searchresult = Testtable1.objects.raw('select name,date from test1 where date between "'+fromdate+'"and "'+todate+'"')
        return render(request,'index.html',{'data':searchresult})
    else:
        displaydata = Testtable1.objects.all()
        return render(request, 'index.html', {'data': displaydata})
