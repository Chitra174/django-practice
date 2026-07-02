from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1><a href='test'>Hello world</a></h1>")

def test(request):
    return HttpResponse("<h1>This is my test page</h1>")