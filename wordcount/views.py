from django.http import HttpResponse
from django.shortcuts import render # then go same page change return

def homepage(request):
    return render(request, 'home.html',)
def count  (request):
    return render(request, 'count.html')