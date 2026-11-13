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


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import ContactMessage


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        text = request.POST.get("message")

        ContactMessage.objects.create(name=name, email=email, subject=subject, message=text)

        send_mail(
            subject="We received your message - Elevora",
            message=(
                f"Hi {name},\n\n"
                f"Thank you for contacting Elevora. We have received your message about \"{subject}\" "
                "and will reply within 1 to 2 working days.\n\n"
                "Kind regards,\nThe Elevora Team"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        print(">>> CONFIRMATION EMAIL SENT TO:", email)

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"ok": True, "message": "Your message has been sent. Thank you!"})
        messages.success(request, "Your message has been sent. Thank you!")
    return redirect("/#contact")