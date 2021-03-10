from django.shortcuts import HttpResponse,render


def home(request):
    return render(request , 'pages/home.html')

def about(request):
    return render(request , 'pages/about.html')

def contact(request):
    return render(request , 'pages/contact.html')

def handler404(request,exception):
    return render(request , 'errors/404.html' , {'error' : exception} , status = 404)

def handler500(request):
    return render(request , 'errors/500.html' , {} , status = 500)