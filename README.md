# 💼 Portfolio Dynamic Site

A dynamic and responsive portfolio website built using Django and Jinja templating, designed to showcase your projects, skills, and achievements in a clean and interactive way.

---

## 🌟 Features

- 🌐 Responsive Design — Built with **W3.CSS** to ensure mobile-friendly, clean UI across all devices.
- 🔄 Dynamic Content — Projects and skills are rendered dynamically using **Jinja templates**.
- 📬 Contact Form — Integrated **SMTP** to send direct emails from the website.
- 🛢️ Backend Database — Uses **MySQL** to manage all portfolio data including projects and messages.
- ☁️ Online Hosting — Seamless deployment on **PythonAnywhere** for 24/7 accessibility.

---

## ⚙️ Installation & Setup

To run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/portfolio-site.git
cd portfolio-site

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run the development server
python manage.py runserver
