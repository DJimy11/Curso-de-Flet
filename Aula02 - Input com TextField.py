import flet as ft

def main(page):

    def login(e):
        if not nome.value:
            nome.error_text = 'Por favor, insira o seu nome!'
            page.update()
        if not senha.value:
            senha.error_text = 'Por favor, insira a senha!'
            page.update()
        else:
            entrada_nome = nome.value
            entrada_senha = senha.value
            print(f"Nome: {nome} \nSenha: {senha}")

            page.clean() #Função para limpar a página!
            page.add(ft.Text(f'Olá, {entrada_nome} \nSeja bem-vindo!'))


    nome = ft.TextField(label="Insira o seu nome")
    senha = ft.TextField(label="Insira a sua senha")
    
    page.add(
        nome,
        senha,
        ft.ElevatedButton("Clique em mim", on_click=login)
    )



ft.app(target=main)