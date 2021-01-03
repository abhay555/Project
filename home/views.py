from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'welcome.html')


def information(request):
    return render(request, 'information.html')


def data_source(request):
    return render(request, 'data_source.html')

def about(request):
    return render(request, 'about.html')
