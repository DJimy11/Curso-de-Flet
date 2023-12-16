from flet import *


def main(page: Page):
    page.title = 'Sistema de Roteamento'


    def nova_rota(route):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Flet App'), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton('Visite a Loja', on_click=lambda _: page.go("/loja"))
                ]
            )
        )

        if page.route == "/loja":
            page.views.append(
                View(
                    "/loja",
                    [
                        AppBar(title=Text("Loja"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Página Inicial", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    
    
    page.on_route_change = nova_rota
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main, view=WEB_BROWSER)