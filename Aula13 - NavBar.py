from flet import *

def main(page: Page):
    page.title = 'NAVEGAÇÃO'


    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME, label='Início'),
            NavigationDestination(icon=icons.EXPLORE, label='Navegar'),
            NavigationDestination(icon=icons.COMMUTE, label='Destino')
        ]
    )

    page.add(Text('Corpo da Aplicação'))






app(target=main)