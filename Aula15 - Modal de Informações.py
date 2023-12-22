from flet import *

def main(page: Page):

    #Primeira Parte - Criar Alerta
    alerta = AlertDialog(
        title=Text('Informação Importante!'),
        content= Text('Olá! Obrigação por confiar em nós.'),
        on_dismiss=lambda e: print('Alerta fechado.')
    )


    #Terceira Parte - Função para executar o Alerta
    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.update()


    #Segunda Parte - Botão para abrir o Alerta
    page.add(
        Text('Olá, Mundo!'),
        ElevatedButton('Informação', on_click=abrir_alerta)
    )


app(target=main)