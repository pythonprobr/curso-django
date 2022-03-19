from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('<html><body>Hello, Django!</body></html>')
