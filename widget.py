import flet as ft
from flet import AlertDialog
from flet import Container, Column, TextField, Row, Text, PopupMenuButton, PopupMenuItem
import command

class InfoDisplay(AlertDialog): 
    def __init__(self, message: str):
        super().__init__()
        self.title = Text("Liste des commandes:", 
                          color=ft.colors.GREEN_500,
                          style=ft.TextStyle(
                              weight=ft.FontWeight.BOLD,
                              shadow=ft.BoxShadow(1, 1, ft.colors.BLACK38, ft.Offset(1, 1))
                          ))
        self.modal = True
        self.content = Text(value=message, weight=ft.FontWeight.BOLD)
        self.open = True
        self.actions = [ft.TextButton(content=Text(value="ok", color=ft.colors.GREEN_300), on_click=self.closing)]

    def closing(self, e: ft.ControlEvent): 
        self.open = False
        self.update()
   
class Parameters(PopupMenuButton):
    def __init__(self):
        super().__init__()
        self.items = [
            PopupMenuItem(on_click=self.clearChat, content=Row([ft.Icon(name=ft.icons.CLEAR_ALL, color=ft.colors.GREEN_200), Text(value="Nettoyer")])),
            PopupMenuItem(),
            PopupMenuItem(on_click=self.helpCommand, content=Row([ft.Icon(name=ft.icons.LIST, color=ft.colors.GREEN_200), Text(value="Listes des commandes")])),
            PopupMenuItem(content=Row([ft.Icon(ft.icons.ALBUM_OUTLINED, ft.colors.GREEN_200), Text("A propos du developpeur")]))
        ]
        self.icon_color = ft.colors.WHITE
    
    def helpCommand(self, e: ft.ControlEvent):
        info = command.command_list
        del info[0]
        info[0] = "- help"
        info = "".join(info)
        e.page.add(InfoDisplay(info))
    
    def clearChat(self, e: ft.ControlEvent):
        e.page.app.content.chatContainer.content.controls[2].content.controls = []

class SendButton(ft.IconButton):
    def __init__(self, func):
        super().__init__()
        self.icon = ft.icons.SEND
        self.icon_color = ft.colors.WHITE
        self.bgcolor = ft.colors.GREEN_500
        self.icon_size = 30
        self.on_click = func

class InfoBar(Container):
    def __init__(self, userId: str = "Alexandra"):
        super().__init__()
        self.opacity = 1
        self.profilePic = ft.Icon(name=ft.icons.FACE_4, color=ft.colors.WHITE)
        self.profileId = Text(value=userId, weight=ft.FontWeight.BOLD, size=20, font_family="Arial",
                              style=ft.TextStyle(color=ft.colors.WHITE))
        self.parameters = Parameters()
        self.infoBar = Row(
            controls=[
                Row(controls=[self.profilePic, self.profileId]),
                self.parameters
            ],
            spacing=190
        )
        self.padding = 10
        self.bgcolor = ft.colors.GREEN_600
        self.border_radius = 20
        self.shadow = ft.BoxShadow(10, 50, ft.colors.BLACK26, ft.Offset(x=0, y=10))
        self.content = self.infoBar

class Message(Container):
    def __init__(self, message: str, user: str):
        super().__init__()
        self.opacity = 1
        self.bgcolor = ft.colors.LIGHT_BLUE_ACCENT_700
        self.padding = 10
        self.border = ft.border.all(1.5, ft.colors.BLACK)
        self.userId =  Text(value=user.capitalize(), color=ft.colors.BLACK, size=15, italic=True, weight=ft.FontWeight.BOLD)
        self.border_radius = 10
        self.message = Text(
            value=message.capitalize(), 
            color=ft.colors.WHITE, size=15,
            style=ft.TextStyle(
                weight=ft.FontWeight.W_300,
                color=ft.colors.WHITE,
                shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1))))
        self.content = Column(
            controls=[
                self.userId,
                self.message
            ],
            spacing=0,
        )

class ResponceMessage(Container):
    def __init__(self, responce: str):
        super().__init__()
        self.opacity = 1
        self.border = ft.border.all(1.5, ft.colors.BLACK)
        self.padding = 10
        self.userId = Text(value="Alexandra", color=ft.colors.BLACK, size=15, italic=True, weight=ft.FontWeight.BOLD)
        self.responce = Text(
            value=responce.capitalize(), 
            color=ft.colors.WHITE, size=15,
            style=ft.TextStyle(
                weight=ft.FontWeight.W_300,
                color=ft.colors.WHITE,
                shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1))))
        self.bgcolor = ft.colors.GREEN_400
        self.border_radius = 20
        self.content = Column(
            controls=[
                self.userId,
                self.responce
            ],
            spacing=0
        )

class CommandMessage(Container):
    def __init__(self, output: str) -> None:
        super().__init__()
        self.opacity = 1
        self.border = ft.border.all(1.5, ft.colors.BLACK)
        self.padding = 10
        self.userId = Text(value="Alexandra", color=ft.colors.BLACK, size=15, italic=True, weight=ft.FontWeight.BOLD)
        self.bgcolor = "#868f96"
        self.border_radius = 20
        self.responce = Text(
            value=output, 
            style=ft.TextStyle(
                weight=ft.FontWeight.W_500,
                color=ft.colors.WHITE,
                shadow=ft.BoxShadow(100, 1, ft.colors.BLACK38, ft.Offset(1, 1))))
        self.content = Column(
            controls=[
                self.userId,
                ft.Divider(color="black"),
                self.responce
            ],
            spacing=0
        )

class MessageDisplay(Column):
    def __init__(self):
        super().__init__()
        self.spacing = 20
        self.message: TextField = TextField(
            hint_text='Message...',
            color=ft.colors.BLACK54,
            suffix_icon=ft.icons.EMOJI_EMOTIONS,
            hint_style=ft.TextStyle(color=ft.colors.GREEN_200),
            cursor_color=ft.colors.GREEN_500,
            selection_color=ft.colors.GREEN_50,  
            multiline=True, 
            max_lines=2,
            border_color=ft.colors.GREEN_400,
            border_radius=20)
        self.messageSend = SendButton(func=self.addMessage)
        self.messageInput = Container(
            content=Row(
                controls=[self.message, self.messageSend],
                alignment="center",
                ),
            bgcolor=ft.colors.WHITE, #"#fdfcfb"
            border_radius=20,
            padding=7,
            shadow=ft.BoxShadow(color="smookblack", spread_radius=10, blur_radius=50, offset=ft.Offset(5,5))
            )
        
        self.chat = Column(controls=[Container(width=200, height=100)]) 
        self.chatContainer = Container(
            content=Column(scroll="auto", auto_scroll=True,
                controls=[
                Container(content=InfoBar()),
                ft.Divider(),
                Container(content=ft.Column(auto_scroll=True, scroll=ft.ScrollMode.AUTO))]),
            height=590,
            width=400,
            padding=10,
            bgcolor=ft.colors.WHITE38,
            border_radius=20,
            shadow=ft.BoxShadow(color="smookblack", spread_radius=10, blur_radius=50, offset=ft.Offset(5,5))
        )

        self.controls = [self.chatContainer, self.messageInput]

    def addMessage(self, e):
        if self.message.value:
            if self.message.value.split(" ")[0].lower() == "$command:":
                # Supression de "$command:" et classification (nom command) et (argument)
                input_text: str = self.message.value.strip(' \n')
                input_text: list[str] = self.message.value.split(" ")
                del input_text[0]
                commande: str = input_text[0]
                arg: tuple[str] = tuple(input_text[1:])

                # Envoi des instruction et attente des resultats au module (command.py)
                match commande:
                    case 'content':
                        result = command.command_input(commande, arg)
                        self.chatContainer.content.controls.append(result)
                    case ('cd', 'cd..', 'cd\\', 'mkdir'):
                        result: str = command.command_input(commande, arg)
                        self.chatContainer.content.controls.append(CommandMessage(output=result))
                    case _:
                        result: str = command.command_input(commande, arg)
                        self.chatContainer.content.controls.append(CommandMessage(output=result))
                self.message.value = ""
            else:
                self.chatContainer.content.controls.append(Message(message=self.message.value.strip(), user="Elie"))
                self.chatContainer.content.controls.append(ResponceMessage(responce="Bien recu et traitement ..."))
                self.message.value = ""
        self.update()