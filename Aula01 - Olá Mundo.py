import flet as ft

# Primairo programa com Flet, escrevendo Olá mundo na tela
# - Função main para inicialiar uma página
def main(page: ft.Page):
    # - Inicializando um variável que vai recever o nosso texto
    ola = ft.Text(value='Olá, mundo!', size=30)
    # - Adicionando a varável nos controls da aplicação
    page.controls.append(ola)
    # - Atualizando a nossa página
    page.update()

# Comando para executar a nossa aplicação
ft.app(target=main)