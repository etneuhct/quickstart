set program_folder=%1
cd %program_folder%
ng new angular-client --commit=false --style=css --routing=true --skipGit=true
ng add @angular/material --theme=custom --typography=true --animations=true
