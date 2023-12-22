from flet import *


def main(page: Page):

    #Funções para confirmar e cancelar ações
    def confirmar(e):
        alerta_dialogo.open = False
        print('O item foi eliminado.')
        page.update()


    
    def cancelar(e):
        alerta_dialogo.open = False
        print('A ação foi cancelada')
        page.update()

    
    # Criar a Função para Abrir o Alerta
    def abri_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open = True
        page.update()

    
    
    # Criar Alerta de Diálogo
    alerta_dialogo = AlertDialog(
        modal=True,
        title=Text('Confirme a Ação.'),
        content=Text('Deseja apagar os itens selecionados?\nA ação não pode ser desfeita.'),
        actions=[
            TextButton('Apagar', on_click=confirmar),
            TextButton('Cancelar', on_click=cancelar)
        ],
        actions_alignment=MainAxisAlignment.END
    )

    # Criar Botão para Abrir Alerta


    # Criar Função para fechar o Alerta


    page.add(
        Text('Olá, mundo!'),
        ElevatedButton(
            'Apagar Item',
            on_click=abri_modal,
            icon=icons.DELETE,
            icon_color='red'
        )
    )


app(target=main)