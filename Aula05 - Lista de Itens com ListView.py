import flet as ft


def main(page: ft.Page):
    lista = ft.ListView(spacing=2, expand=True)

    for i in range(5000):
        lista.controls.append(ft.Text(f'Estamos na linha: {i}'))
    page.add(lista)


ft.app(target=main, view=ft.WEB_BROWSER)