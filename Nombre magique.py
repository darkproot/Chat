import flet as ft
from flet import Container, Column, Row
from flet import TextField, ElevatedButton, Text
from flet import Page
from random import randint

essaie: int = 1
num_magique: int = randint(1, 10)
GRAND: str = "Un peu trop grand!👇🏾👇🏾"
PETIT: str = "Un peu trop petit!👆🏾👆🏾"
TROUVE: str = f"Bravo✨✨ Le numero magique est bien {num_magique}"

def evaluation(n: int) -> bool | str:
    global num_magique
    if n == num_magique: return True
    elif n > num_magique: return GRAND
    return PETIT

class App(Container):
    def __init__(self):
        super().__init__()
        global num_magique
        self.padding = 20
        self.border_radius = 20
        # self.alignment = 
        self.gradient = ft.LinearGradient(
            colors=[ft.colors.LIGHT_BLUE_400, ft.colors.GREEN],
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right
        )
        self.height = 300
        self.entry = TextField(
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                shadow=ft.BoxShadow(1, 1, ft.colors.BLACK54, ft.Offset(3, 3))
            ),
            label="Entrer",
            selection_color=ft.colors.LIGHT_BLUE_500,
            border_radius=20,
            cursor_radius=20,
            text_align=ft.TextAlign.CENTER,
            cursor_color=ft.colors.LIGHT_GREEN_200,
            border_color=ft.colors.LIGHT_GREEN_200,
            label_style=ft.TextStyle(color=ft.colors.LIGHT_GREEN_200)
        )
        self.button = Row(
            [
                ElevatedButton(
                    text="Envoyer",
                    expand=True,
                    on_click=self.attempt
                )
            ]
        )
        self.output = TextField(
            label="OUTPUT",
            border_radius=20,
            value=f"Un nombre entre 0 et 100{num_magique}",
            max_lines=2,
            multiline=True,
            read_only=True,
            label_style=ft.TextStyle(color=ft.colors.LIGHT_BLUE_200),
            text_align=ft.TextAlign.CENTER,
            border_color=ft.colors.LIGHT_BLUE_200,
            text_style=ft.TextStyle(
                shadow=ft.BoxShadow(1, 1, ft.colors.BLACK26, ft.Offset(2,2))
            )
        )
        self.renitialise = ft.TextButton(
            text="Reinitialisation",
            on_click=self.initer
        )
        self.content=Container(
            Column(
                controls=[
                    self.entry,
                    self.button,
                    self.output
                ],
                spacing=20
            ),
            bgcolor=ft.colors.WHITE24,
            padding=ft.Padding(left=20, right=20, top=45, bottom=10),
            border_radius=20,
            blur=.4,
            alignment=ft.Alignment(0, 0),
            shadow=ft.BoxShadow(10, 10, ft.colors.BLACK12, ft.Offset(15, 20))
        )

    def attempt(self, e:ft.ControlEvent):
        global GRAND, PETIT, TROUVE, essaie
        user_input: str = self.entry.value
        try:
            user_input = int(user_input)
            response = evaluation(user_input)
            match response:
                case True: 
                    self.output.value = TROUVE + f" apres {essaie} essaie(s))"
                    self.output.border_color = ft.colors.GREEN_500
                    self.output.label_style.color = ft.colors.GREEN_500
                    self.output.text_style.color = ft.colors.GREEN_500
                    self.output.text_style.weight = ft.FontWeight.BOLD
                    # self.content.content.controls.append(self.renitialise)
                case str(GRAND): 
                    essaie += 1
                    self.output.value = GRAND
                case str(PETIT):
                    essaie += 1 
                    self.output.value = PETIT
        except ValueError:
            essaie += 1
            self.output.value = 'Essayer un entier'
            self.output.border_color = ft.colors.RED_800
            self.output.label_style.color = ft.colors.RED_800
            self.output.text_style.color = ft.colors.RED_800
        self.update()

    def initer(self, e: ft.ControlEvent):
        global num_magique, essaie
        num_magique = randint(1, 10)
        self.output.value = "Un nombre entre 0 et 100"
        self.entry.value = ""
        essaie = 1
        self.update()
        

def main(page: Page) -> None:
    page.title = "Nombre magique"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.alignment.center
    page.padding = 10
    page.window.height = 50,
    page.window.width = 400
    page.window.resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(App())
    
if __name__ == "__main__":
    ft.app(main)