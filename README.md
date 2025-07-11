# 🌐 Django Backend Personal Website

The **source code** for my **personal website**, which was constructed with the Django web development framework, is contained in this repository.  
The logic for submitting contact forms is mostly handled by the backend.

---

## Important Features

- ✅ Contact form with **Name**, **Email**, and **Message**
- 📶 uses CSRF protection to securely handle POST requests
-  ✉️ Sends contact messages via email using Django's `send_mail()`
- 🆔 For every form submission, a unique reference number is generated using `uuid.uuid4()`
- 🎨 Clean and contemporary custom HTML + CSS user interface that validates input and displays error/success templates
- 🌐 Ready for deployment (tested using **Render**)

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django 4.x**
- HTML5 / CSS3
- `uuid` module for reference generation
- Django email backend (`django.core.mail`)

---

## 🗂 Project Structure
<pre> project/ ├── mysite/ │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── contact/ │ ├── views.py │ ├── forms.py │ └── templates/ │ ├── contact_form.html │ ├── thankyou.html │ └── error.html ├── static/ │ └── style.css ├── manage.py └── requirements.txt </pre>


---

## 🧠 How It Works

1. The user visits the contact page and fills out their:
   - **Name**
   - **Email**
   - **Message**

2. Upon form submission:
   - Data is sent securely via a `POST` request to the Django backend.
   - Input is validated and a **unique reference number** is generated using:
     ```python
     import uuid
     reference_id = str(uuid.uuid4())
     ```

3. Two email notifications are sent using Django’s `send_mail()`:
   - ✅ **To the site owner** – with the user's details and reference ID
   - 📩 **To the user** – a confirmation message including their reference ID

4. The submission is also **logged to `data.txt`** with:
   - Date and time of submission
   - Name
   - Email
   - Message
   - Reference ID
   ```python
   import datetime
   with open("data.txt", "a+") as file:
       file.write(f"{datetime.datetime.now()} | {name} | {email} | {message} | {reference_id}\n")


## 💌 Contact Form Fields

- 📛 `name`: Full name of the user
- 📧 `email`: Valid email address
- 📝 `message`: User’s message or query

The form uses minimal styling and includes backend validation to ensure input quality.

---



