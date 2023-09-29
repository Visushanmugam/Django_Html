from django.shortcuts import render

# Create your views here.
def home_page(requests):
    r = render(requests, 'WebApp1/home.html', {'home':'visha'})
    return r

