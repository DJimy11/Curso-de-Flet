from flet import *

def main(page: Page):

    page.appbar = AppBar(
        leading=Icon(icons.CODE),
        leading_width=40,
        bgcolor = '#003377',
        title = Text('Minha Loja'),
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='Logar'),
                    PopupMenuItem(),
                    PopupMenuItem(text='Sair')
                ]
            )
        ]
    )

    page.add(Text('Corpo!'))


app(target=main)