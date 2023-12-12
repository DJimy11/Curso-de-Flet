from flet import *


def main(page: Page):
    page.title = 'Sistema de Roteamento'


    def nova_rota(route):
        View(
            '/',
            [
                AppBar(title=Text('Flet App'), bgcolor=colors.SURFACE)
            ]
        )
    page.update()
    
    
    page.on_route_change = nova_rota 


app(target=main, view=WEB_BROWSER)