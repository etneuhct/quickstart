import argparse
import os
from dotenv import load_dotenv
from github import Github
from shutil import copy

load_dotenv()
github_agent = Github(os.getenv("GITHUB_ACCESS"))
user = github_agent.get_user()
username = user.login


class DjangoOption:
    DJANGO, DJANGOAPI = "django", "djangoApi"


class AngularOption:
    Angular, = "angular",


def set_parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--name', required=False, help="Nom du projet à créer")
    parser.add_argument('--project_folder', default=None, help="Chemin vers le dossier où creer le projet")

    # Arguments pour Git
    parser.add_argument('--github', default=False,
                        help="Décrit si le projet doit etre créé également sur Github", type=bool)
    parser.add_argument('--public', '--p', default=None,
                        help="Décrit si le projet sera public", type=bool)

    # Arguments pour django
    parser.add_argument('--django', choices=(DjangoOption.DJANGO, DjangoOption.DJANGOAPI), help="Type de projet Django")
    parser.add_argument('--angular', choices=(AngularOption.Angular,), help="Type de projet Angular")

    return parser.parse_args()


def get_project_folder(parse_args):
    folder = getattr(parse_args, 'project_folder')
    if not folder:
        folder = os.getenv('PROJECT_FOLDER')
    if not folder:
        while True:
            folder = input("Renseigner le chemin vers le dossier de projets")
            if os.path.exists(folder):
                return folder
            else:
                print("Ce répertoire n'existe pas")
    return folder


def get_project_name(parse_args, folder):
    name = getattr(parse_args, 'name')
    while not name:
        name = input("Renseigner le nom du projet\n")
    exist = os.path.exists(os.path.join(folder, name))
    if not name or exist:
        while True:
            if exist:
                print("Ce projet existe dejà")
            name = input("Renseignez le nom du projet")
            if not os.path.exists(os.path.join(folder, name)):
                return name
    return name


def get_github_args(parse_args):
    submit = getattr(parse_args, 'github')
    public = getattr(parse_args, 'public')
    if public is True or public is False:
        submit = True
    return submit, public


def check_project_on_github(name):
    return name in [repo.name for repo in github_agent.get_user().get_repos()]


if __name__ == '__main__':
    args = set_parse_args()

    project_folder = get_project_folder(args)
    project_name = get_project_name(args, project_folder)
    project_path = os.path.join(project_folder, project_name)
    exist_on_desktop = os.path.exists(project_path)
    submit_on_github, make_public = get_github_args(args)
    exist_on_github = check_project_on_github(project_name)
    django_option = getattr(args, 'django')
    angular_option = getattr(args, 'angular')
    base_folder = os.path.abspath(os.path.dirname(__file__))

    if exist_on_github:
        # Clone le repos
        pass
    else:
        # Creation du dossier
        program_folder = os.path.join(project_path, "programmes")
        os.makedirs(program_folder)

        if django_option:
            # Creation d'un projet django
            print("Creation d'un projet Django")
            django_script = os.path.join(base_folder, 'scripts', 'django.bat')
            os.system(f'"{django_script}" {program_folder}')
            copy(
                os.path.join(base_folder, "files", ".gitignore_python"),
                os.path.join(program_folder, "django_server", ".gitignore")
            )

            if django_option == DjangoOption.DJANGOAPI:
                django_api_script = os.path.join(base_folder, 'scripts', 'django_api.bat')
                os.system(f'"{django_api_script}" {program_folder}')

            with open(os.path.join(base_folder, "files", "readme_django.txt"), encoding="utf-8") as f:
                readme = f.read().format(project_name=project_name, username=username)
            with open(os.path.join(program_folder, "django_server", "readme.MD"), "w", encoding="utf-8") as w:
                w.write(readme)

        if angular_option:
            # Creation d'un projet django
            print("Creation d'un projet Angular")
            angular_script = os.path.join(base_folder, 'scripts', 'angular.bat')
            os.system(f'"{angular_script}" {program_folder}')

        if submit_on_github:
            # Creation d'un repos
            print("Creation d'un repos Github")
            repo = user.create_repo(project_name, private=not make_public)
            github_script = os.path.join(base_folder, 'scripts', 'github.bat')
            os.system(f'"{github_script}" {username} {program_folder} {project_name}')

