# QuickStart

Ce script permet de créer rapidement des projets utilisant Django/Angular. 
Les projets peuvent également être renseignés sur Github


## Premiers pas
a) Récupérer le dépôt
```bash
git clone https://github.com/etneuhct/quickstart
cd quickstart
```

b) Installer les dépendances
```bash
pip install -r requirements.txt
```

c) Congigurer l'environnement
```bash
type NUL > .env
```
Avec les informations suivantes:


PROJECT_FOLDER = # CHEMIN DU DOSSIER OU CREER LES PROJETS

GITHUB_ACCESS = # TOKEN D'ACCES GITHUB

d) Executer le programme
```bash
python main.py --name=nomDuProjet --github=False --django=django
```
