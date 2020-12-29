set program_folder=%1
cd %program_folder%
mkdir django_server
cd django_server
python -m venv venv
.\venv\scripts\pip install django
.\venv\scripts\django-admin startproject django_server .
.\venv\scripts\pip freeze > requirements.txt
