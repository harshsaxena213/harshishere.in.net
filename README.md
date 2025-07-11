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

### 🧠 How It Works

1. The user visits the contact page and fills out their:
   - **Name**
   - **Email**
   - **Message**

2. Upon form submission:
   - The data is sent securely via a `POST` request to the Django backend.
   - The backend validates the data and generates a **unique reference number** using:
     ```python
     import uuid
     reference_id = str(uuid.uuid4())
     ```

3. Two email notifications are sent using Django’s `send_mail()`:
   - ✅ **To the site owner** – containing the user’s message, email, and reference number.
   - 📩 **To the user** – a confirmation email with a thank-you message and the same reference number.

4. The user is redirected to:
   - ✅ A **thank-you page** if successful (`thankyou.html`)
   - ❌ An **error page** if the email fails or the input is invalid (`error.html`)


## 💌 Contact Form Fields

- 📛 `name`: Full name of the user
- 📧 `email`: Valid email address
- 📝 `message`: User’s message or query

The form uses minimal styling and includes backend validation to ensure input quality.

---



