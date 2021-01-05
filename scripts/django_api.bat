set program_folder=%1
cd %program_folder%
cd django_server
.\venv\scripts\pip install djangorestframework
.\venv\scripts\pip freeze > requirements.txt
