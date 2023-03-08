
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,View, CreateView, FormView, DetailView, ListView
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

class CreateView(CreateView):
    template_name = 'index1.html'
    form_class = FormCreate
    success_url = reverse_lazy('myapp:CreateView')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
