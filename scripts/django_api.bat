set program_folder=%1
cd %program_folder%
cd django_server
pip install djangorestframework
pip freeze > requirements.txt
