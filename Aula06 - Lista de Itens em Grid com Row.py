import os
import flet as ft

os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'


def main(page: ft.Page):
    linha = ft.Row(wrap=True, scroll='always', expand=True)
    page.add(linha)

    for i in range(10):
        linha.controls.append(
            ft.Container(
                ft.Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK,
                border=ft.border.all(2, ft.colors.WHITE),
                border_radius=ft.border_radius.all(8)
            )
        )
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)