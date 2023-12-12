import flet as ft


def app(pg: ft.Page):

    def tecla(e: ft.KeyboardEvent):
        pg.clean()
        pg.add(
            ft.Text(f'Tecla pressionada: {e.key} \nSHIFT: {e.shift} \nCONTROL: {e.control} \nALT: {e.alt} \nMETA: {e.meta}')
        )
    pg.on_keyboard_event = tecla

    pg.add(
        ft.Text('Pressione qualquer tecla ou uma combinação de teclas. [ CTRL, SHIFT, ALT, META ]')
    )



ft.app(target=app)