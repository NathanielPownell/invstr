from django.shortcuts import render

def home(request):
    return render(request, 'web_app/index.html')

def aboutapp(request):
    return render(request, 'web_app/aboutapp.html')

def aboutme(request):
    return render(request, 'web_app/aboutme.html')

def dashboard(request):
    return render(request, 'web_app/dashboard.html')

def trade(request):
    return render(request, 'web_app/trade.html')