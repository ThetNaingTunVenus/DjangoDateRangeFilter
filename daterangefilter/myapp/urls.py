from django.urls import path
from .views import *

from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.result, name='test'),
    path('create', CreateView.as_view(), name='CreateView'),

]