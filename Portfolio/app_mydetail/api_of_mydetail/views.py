from django.shortcuts import render, redirect 

from app_mydetail.forms import ContactForm
from django.contrib import messages
#smtp imports
import smtplib
from django.conf import settings
  

  
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


#Nice Database Setup : List of dictionaries
project_list = [
    {
        "title": "Public Transport Assistant",
        "image": "app_mydetail/images/gps.png",
        "serial": "One",
        "year": 2024,
        "description": "The Public Transport Assistant for Estimated Time of Arrival (ETA) project aims to revolutionize the way people navigate public transport systems by providing real-time, accurate information about arrival times, delays, and optimal routes.",
        "link": "https://github.com/ChandraMohan-Sah/Public_Transport_Assistent"
    },
    {
        "title": "Course Selling Website",
        "image": "app_mydetail/images/teaching.png",
        "serial": "Two",
        "year": 2023,
        "description": "Our mission is to empower individuals with the knowledge and skills they need to achieve their personal and professional goals.",
        "link": "#"
    },
    {
        "title": "CNN Architecture implemented using Pytorch",
        "image": "app_mydetail/images/cnn.png",
        "serial": "Three",
        "year": 2024,
        "description": "Designed a CNN architecture for image classification that processed 28x28 images, sequentially applied convolutional layers with batch normalization, ReLU activation, and max pooling, then flattened features through fully connected layers, achieving classification into 10 digit classes using softmax",
        "link": "https://colab.research.google.com/drive/13vTqkwE9-gm4gjVB_gInMROr69mCXOui"
    },
    {
        "title": "DBMS Simple Project : CRUD Operation",
        "image": "app_mydetail/images/Database.jpg",
        "serial": "four",
        "year": 2023,
        "description": "Database management project that applies CRUD operation and instantly the actions can be seen on the dashboard",
        "link": "https://github.com/ChandraMohan-Sah/Website-ElephantSQL-Project"
    },
        {
        "title": "Everlasting Portfolio",
        "image": "app_mydetail/images/portfolio.png",
        "serial": "five",
        "year": 2023,
        "description": "Explore an Everlasting Portfolio – a showcase of innovation, skill, and growth that evolves with every project.",
        "link": "https://github.com/ChandraMohan-Sah/StaticPortfolioWeb/tree/main/Portfolio"
    },
    {
        "title": "Hardware Integration for GPS Tracker",
        "image": "app_mydetail/images/hardware.png",
        "serial": "six",
        "year": 2023,
        "description": "Experienced in hardware integration for GPS trackers, ensuring seamless connectivity, accurate positioning, and reliable data transmission through optimized component configuration.",
        "link": "https://www.linkedin.com/posts/activity-7171561640054636544-6Bwk?utm_source=share&utm_medium=member_desktop"
    }
]



experiences = [
    {
        "tech":"CPP",
        "percentage":"95%",
        "color":"w3-blue"
    },
    {
        "tech":"Arduino Programming",
        "percentage":"35%",
        "color":"w3-grey"
    },
    {
        "tech":"Python",
        "percentage":"85%",
        "color":"w3-red"
    },

    {
        "tech":"HTML, CSS, Javascript",
        "percentage":"20%",
        "color":"w3-pink"
    },
    {
        "tech":"Django",
        "percentage":"85%",
        "color": " w3-teal"
    },
    {
        "tech":"Django Rest Framework",
        "percentage":"85%",
        "color": " w3-teal"
    },
    {
        "tech":"Database with MySQL",
        "percentage":"75%",
        "color":"w3-blue"
    },
    {
        "tech":"git and Github",
        "percentage":"35%",
        "color":"w3-grey"
    },

    {
        "tech":"Kicad",
        "percentage":"35%",
        "color":"w3-brown"
    },
    {
        "tech":"Linux Familiarity",
        "percentage":"30%",
        "color":"w3-green"
    },
    {
        "tech":"Pytorch",
        "percentage":"20%",
        "color":"w3-pink"
    }
]


def home(request):
    if request.method == "POST":
        return ContactPOST(request)
    else:
        form = ContactForm()

    context = {
        "projects": project_list,
        "experiences": experiences,
        "form_data": form
    }

    return render(request, 'base.html', context)


def ContactPOST(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        try:
            # Extract form data
            cleaned_data = form.cleaned_data
            subject = "New Contact Form Submission"
            html_message = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #4CAF50;">New Submission</h2>
                <p><strong>Full Name:</strong> {cleaned_data['fullname']}</p>
                <p><strong>Contact Email:</strong> {cleaned_data['email']}</p>
                <p><strong>Description:</strong></p>
                <p style="white-space: pre-line; background-color: #f9f9f9; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
                    {cleaned_data['description']}
                </p>
            </body>
            </html>
            """

            # Email setup
            sender_email = f"{EMAIL_HOST_USER}"
            recipient_email = "csah9628@gmail.com"
            password = f"{EMAIL_HOST_PASSWORD}"

            # Create email headers and body
            email_message = f"Subject: {subject}\n"
            email_message += "Content-Type: text/html\n\n"
            email_message += html_message

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, email_message)

            # Add a success message
            messages.success(request, "Thanks For Approaching Me!")

            # Save form and redirect
            # form.save()
            return redirect("home")
        except Exception as e:
            # Add an error message
            messages.error(request, f"An error occurred: {e}")
            return redirect("home")

    # If form is invalid, show validation errors
    return render(request, 'base.html', {"form_data": form})
