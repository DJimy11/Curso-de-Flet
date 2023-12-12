import flet as ft


def main(page: ft.Page):
    for i in range(1, 500):
        page.controls.append(ft.Text(f'Estamos na linha: {i}'))
    page.scroll = 'always'
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)