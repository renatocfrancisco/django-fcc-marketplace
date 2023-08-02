# django-fcc-marketplace

[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8](https://img.shields.io/badge/flake8-221e57?style=flat&logo=python&logoColor=17acc0)](https://flake8.pycqa.org/en/latest/)

Django project created by FreeCodeCamp in [Learn Django by Building an Online Marketplace](https://youtu.be/ZxMB6Njs3ck)

## Commands

### pip

Remember to run `pip install -r requirements.txt` to install dependencies.<br>
Also ``py -m venv venv`` to create a virtual environment. Then activate it with ``.\venv\Scripts\activate``.

### django

Project started with `django-admin startproject puddle` after `pip install django`

Generated `/core` with `py .\manage.py startapp core`<br>
Generated `/item` with `py .\manage.py startapp item`<br>

To create migrations, run `py .\manage.py makemigrations`<br>
To apply migrations, run `py .\manage.py migrate`<br>
To run server, run `py .\manage.py runserver`<br>

To create user for admin page, run `py .\manage.py createsuperuser` and enter your credentials. <br>
To access admin page, go to `/admin`

### formatting

You can use `flake8` to check for PEP8 compliance.<br>
You can use `black` (*ex: `black .\puddle\`*) to format your code.<br>

<details>
<summary>Dev Commentary</summary>

<br>
First time messing with Django. 😐<br>
The tutorial's title says "Python Tutorial for Beginners". That's funny.<br>
Video timestamp: **1:28:24**

</details>
