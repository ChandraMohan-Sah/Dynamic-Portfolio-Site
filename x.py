def contactPOST(request):
    if request.method == "POST":
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
                sender_email = "csah9628@gmail.com"
                recipient_email = "csah9628@gmail.com"
                password = "ysoulyellpaihezg"

                # Create email headers and body
                email_message = f"Subject: {subject}\n"
                email_message += "Content-Type: text/html\n\n"
                email_message += html_message

                # Send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, email_message)

                print("HTML Email sent successfully!")

                # Save form and redirect
                form.save()
                return redirect("thank-you")
            except Exception as e:
                print(f"An error occurred: {e}")

    return render(request, "z_form_inbuilt/contact.html", {"form_data": ContactForm()})

