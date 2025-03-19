from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,"index.html")



from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import JsonResponse
from django.core.mail import send_mail

import json
 

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Remove this in production!
def send_email(request):
    print("Received request!")  # Debugging
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON data
            name = data.get("name")
            surname = data.get("surname")
            email = data.get("email")
            phone = data.get("phone")
            print("Parsed Data:", name, surname, email, phone)  # Debugging

            if not all([name, surname, email, phone]):
                return JsonResponse({"success": False, "message": "All fields are required."})

            # Email Messages
            subject_admin = "New Contact Form Submission"
            message_admin = f"""
            You have received a new contact form submission:

            Name: {name} {surname}
            Email: {email}
            Phone: {phone}
            """

            subject_user = "Contacting AD Softwares"
            message_user = f"""
            Client Name: {name}
            Email: {email}
            Phone: {phone}

            Thank you for reaching out to AD Softwares! We will get back to you shortly.

            Regards,
            AD Softwares Team
            """

            send_mail(subject_admin, message_admin, settings.EMAIL_HOST_USER, ["enquiryadsoftware@gmail.com"])
            send_mail(subject_user, message_user, settings.EMAIL_HOST_USER, [email])

            return JsonResponse({"success": True, "message": "Your message has been sent successfully!"})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data received."})

    return JsonResponse({"success": False, "message": "Invalid request method."})
