from flet import *

def main(page: Page):

    def atualizar(e):
        page.banner.open = False
        print('Atualizando!')
        page.update()


    def mais_tarde(e):
        page.banner.open = False
        print('Lembrar mais tarde.')
        page.update()


    def cancelar(e):
        page.banner.open = False
        print('Cancelado')
        page.update()

    # 1 - Banner de Informação
    page.banner = Banner(
        bgcolor=colors.GREY,
        leading=Icon(icons.WARNING),
        content=Text('Olá! Temos uma nova atualização para a sua aplicação.'),
        actions=[
            TextButton(
                'Atualizar Agora',
                on_click=atualizar
            ),
            TextButton(
                'Lembrar mais tarde',
                on_click=mais_tarde
            ),
            TextButton(
                'Fechar',
                on_click=cancelar
            )
        ]
    )

    # Função para abrir alerta
    def abrir_banner(e):
        page.banner.open = True
        page.update()

    page.add(
        Text('Olá, mundo!'),
        ElevatedButton(
            'EXECUTAR',
            on_click=abrir_banner
        )
    )

app(target=main)
