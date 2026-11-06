from django.http import request
from django.shortcuts import render


from django.shortcuts import render

def index(request):
       return render(request, 'core/index.html')

def blog(request):
       return render(request, 'core/blog.html')

def blog_details(request):
       return render(request, 'core/blog-details.html')

def portfolio_details(request):
       return render(request, 'core/portfolio-details.html')

def service_details(request):
       return render(request, 'core/service-details.html')

def starter_page(request):
       return render(request, 'core/starter-page.html')