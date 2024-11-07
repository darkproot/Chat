import os
import flet as ft
from flet import Container, Column

command_list: list[str] = ['\n- where_am_i', '\n- help', '\n- content', '\n- cd..', '\n- cd <Nom-Dossier>', '\n- cd\\ [Pour aller au repertoire racine]', '\n- mkdir <Nom-Dossier>']
liste = ["Liste des commandes:"]
for i in range(len(command_list)):
    liste.append(command_list[i])

# CONSTANT
HELP: str = "Execution d'une commande:\n\tSyntax: $command: <nom-commande> <liste-arg>\nTaper la commande 'help' pour la liste des commandes"
COMMAND_LIST: str = "".join(liste)
del liste

def command_exe(commande: str) -> None:
    os.system(commande)

def back_path(path: str) -> str:
    path_list: list[str] = path.split('\\')
    del path_list[-1]
    return "\\".join(path_list)

def where_am_i() -> str:
    """
    Pour connaitre le chemin vers le reperetoire ou on se trouve
    :return: chemin vers le repertoire courant
    """
    return os.getcwd()

def content_display() -> list[str]:
    """
    Contenu du repertoire courant
    :return: Liste du contenu du repertoire courant
    """
    return os.listdir()

def change_directory(directory: str) -> None:
    if directory in content_display(): os.chdir(directory)

def make_directory(name: str | list[str]) -> list[str] | None:
    if name in content_display(): return None
# Objet de retour
class ContentDisplay(Container):
    def __init__(self, dir: list[str], file: list[str]):
       super().__init__()
       self.bgcolor = "#868f96"
       self.file = file
       self.border_radius = 20
       self.dir = dir
       self.padding = 20
       self.border = ft.border.all(1.5, ft.colors.BLACK)
       self.directories = Column(
        scroll="auto",
        controls=[]
       )
       self.files = Column(
        scroll="auto",
        controls=[]
       )
       self.content = Column(
            [
                ft.Text(
                    value=f"Liste des Dossiers et des Fichiers:\n{where_am_i()}",
                    color="White",
                    style=ft.TextStyle(
                            shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1)),
                            weight=ft.FontWeight.W_900)
                ),
                ft.Divider(color=ft.colors.BLACK38),
                self.directories, 
                self.files
            ]
        )
       for dir in self.dir:
            self.directories.controls.append(
                Container(
                    content=ft.Text(
                        value=dir,
                        color="white", 
                        style=ft.TextStyle(
                            weight=ft.FontWeight.W_500,
                            shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1)))),
                    bgcolor=ft.colors.LIGHT_GREEN_300,
                    padding=10,
                    border_radius=5,
                    width=340,
                    alignment=ft.alignment.center
                )
            )
       for file in self.file:
            self.files.controls.append(
                Container(
                    content=ft.Text(
                        value=file,
                        color="white", 
                        style=ft.TextStyle(
                            weight=ft.FontWeight.W_500,
                            shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1)))),
                    bgcolor=ft.colors.BLUE_200,
                    padding=10,
                    border_radius=20,
                    width=340,
                    alignment=ft.alignment.center
                )
            )

# Main function
def command_input(command: str, arg: tuple[str] = None):
    match command:
        case 'where_am_i': return where_am_i()
        case 'help': return COMMAND_LIST
        case 'content': 
            files: list[str] = [x for x in content_display() if '.' in x]
            directories: list[str] = [x for x in content_display() if x not in files]
            return ContentDisplay(directories, files)
        case 'cd':
            if len(arg) == 1 and arg[0] in content_display(): 
                change_directory(arg[0])
                return where_am_i()
            return "PAS DE DOSSIER DE CE NOM"
        case 'cd..':
            os.chdir(back_path(where_am_i()))
            return where_am_i()
        case 'cd\\':
            os.chdir("C:\\")
            return where_am_i()
        case 'mkdir':
            if len(arg) == 1:
                os.mkdir(arg[0])
                path = where_am_i() + f'\\{arg[0]}'
                os.chdir(path)
                return where_am_i()
            return "$command: mkdir <Nom-Dossier>"
        case _: return HELP


if __name__ == "__main__":
    print(f"{where_am_i() = }")
    print(f"{content_display() = }")
    os.chdir("c:\\Document de elie")
    print(f"{where_am_i() = }")
    print(f"{content_display() = }")