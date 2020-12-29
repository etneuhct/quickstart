set user_name=%1
set folder=%2
set project_name=%3

cd %folder%
git init
git add .
git commit -m "Creation du projet"
git branch -M main
git remote add origin https://github.com/%user_name%/%project_name%.git
git push -u origin main
