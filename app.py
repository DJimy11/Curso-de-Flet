from flet import *

def main(page: Page):
    page.add(
        Text('Olá, mundo!', size=30, color='red'),
        Container(
            width=200,
            height=200,
            bgcolor=colors.AMBER
            
        ),
        TextField()
    )


app(target=main)