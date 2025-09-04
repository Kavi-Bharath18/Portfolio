from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project
from .forms import ContactForm
from .models import Resume, Images
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    latest_projects = Project.objects.all()[:3]
    top_skills = Skill.objects.all()[:10]
    profile = Images.objects.first()
    return render(request, "portfolio/home.html", {"latest_projects": latest_projects, "top_skills": top_skills, 'profile':profile})

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    return render(request, "portfolio/projects.html", {"projects": Project.objects.all()})

def skills(request):
    return render(request, "portfolio/skills.html", {"skills": Skill.objects.all()})

def resume(request):
    resume = Resume.objects.last()
    return render(request, "portfolio/resume.html", {'resume':resume})

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             messages.success(request, "Thanks! Your message has been sent.")
#             return redirect("contact")
#     else:
#         form = ContactForm()
#     return render(request, "portfolio/contact.html", {"form": form})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  # from email
            ['kavibharath5487@gmail.com'], # to email (your email address)
        )

        return redirect('success')  # redirect to success page
    
    return render(request, 'portfolio/contact.html')

