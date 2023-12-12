import os
import flet as ft


os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'

def main(page: ft.Page):
    # Título da Página
    page.title = 'Aplicação da Aula'
    # Tema da Página
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    page.update()
    


ft.app(target=main, view=ft.WEB_BROWSER)