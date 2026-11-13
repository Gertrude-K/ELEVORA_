from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import ContactMessage

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


from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"ok": True, "message": "Your message has been sent. Thank you!"})
        messages.success(request, "Your message has been sent. Thank you!")
    return redirect("/#contact")