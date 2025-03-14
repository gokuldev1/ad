from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")



from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import JsonResponse
from django.core.mail import send_mail



from django.views.decorators.csrf import csrf_exempt

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if not all([name, surname, email, phone]):
            return JsonResponse({"success": False, "message": "All fields are required."})

        # Message to Admin
        subject_admin = "New Contact Form Submission"
        message_admin = f"""
        You have received a new contact form submission:

        Name: {name} {surname}
        Email: {email}
        Phone: {phone}
        """

        # Acknowledgment Email to User
        subject_user = "Contacting AD Softwares"
        message_user = f"""
        Client Name: {name}
        Email: {email}
        Phone: {phone}

        Thank you for reaching out to AD Softwares! We have received your details and will get back to you shortly.

        Regards,
        AD Softwares Team
        """

        try:
            # Send email to Admin
            send_mail(
                subject_admin,
                message_admin,
                "your_email@gmail.com",  # Ensure this matches EMAIL_HOST_USER
                ["enquiryadsoftware@gmail.com"],
                fail_silently=False,
            )

            # Send email to User
            send_mail(
                subject_user,
                message_user,
                "your_email@gmail.com",  # Ensure this matches EMAIL_HOST_USER
                [email],
                fail_silently=False,
            )

            return JsonResponse({"success": True, "message": "Your message has been sent successfully!"})

        except Exception as e:
            return JsonResponse({"success": False, "message": f"Error: {str(e)}"})

    return JsonResponse({"success": False, "message": "Invalid request method."})
