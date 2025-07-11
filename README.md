# 🌐 Personal Website – Django Backend

This repository contains the **source code** for my **personal website**, built using the Django web development framework.  
The backend primarily handles the contact form submission logic.

---

## 📌 Key Features

- ✅ Contact form with **Name**, **Email**, and **Message**
- 📮 Handles POST requests securely with CSRF protection
- ✉️ Uses Django's `send_mail()` to send contact messages via email
- 🆔 Generates a unique reference number using `uuid.uuid4()` for each form submission
- 🎨 Custom HTML + CSS UI with clean and modern design
- 🛡️ Validates input and shows error/success templates
- 🌐 Deployment-ready (tested with **Render** )

---

## 🛠 Tech Stack

- **Python 3.x**
- **Django 4.x**
- HTML5 / CSS3
- `uuid` module for reference generation
- Django email backend (`django.core.mail`)

---

## 🗂 Project Structure
