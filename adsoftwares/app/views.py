from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # Message to AD Softwares
        subject_admin = "New Contact Form Submission"
        message_admin = f"""
        You have received a new contact form submission:

        Name: {name} {surname}
        Email: {email}
        Phone: {phone}
        """
        
        # Send email to Admin
        send_mail(
            subject_admin,
            message_admin,
            "enquiryadsoftware@gmail.com",
            ["enquiryadsoftware@gmail.com"],
            fail_silently=False,
        )

        # Acknowledgment email to the sender
        subject_user = "Contacting AD Softwares"
        message_user = f"""
        Cilent name : {name},
    Email: {email}
        Phone: {phone}
        Thank you for reaching out to AD Softwares! We have received your details and will get back to you shortly.

        Regards,
        AD Softwares Team
        """

        # Send email to user
        send_mail(
            subject_user,
            message_user,
            "enquiryadsoftware@gmail.com",
            [email],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("index")  # Change this to your actual contact page URL name

    return render(request, "index.html")
