import flet as ft
from flet import Container
from flet import Page
from widget import MessageDisplay


def main(page: Page) -> None:
    page.title = "Chat Example"
    page.window.height = 800
    page.window.width = 500
    page.window.resizable = False
    page.theme_mode = "light"
    page.bgcolor = ft.colors.BLACK

    app = Container(content=MessageDisplay(), 
                    padding=30, 
                    border_radius=20,
                    gradient=ft.LinearGradient(colors=["#11998e", "#38ef7d"], begin=ft.alignment.bottom_left, end=ft.alignment.top_right))
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)