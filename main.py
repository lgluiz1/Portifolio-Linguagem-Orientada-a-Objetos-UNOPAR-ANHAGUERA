import flet as ft
from time import sleep

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Sistema Bancário"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Definição da classe Cliente
    class Cliente:
        def __init__(self, nome: str, sobrenome: str, cpf: int):
            self.nome = nome
            self.sobrenome = sobrenome
            self.cpf = cpf
    
    # Definição da classe ContaBancaria
    class ContaBancaria:
        def __init__(self, cliente: Cliente):
            self.cliente = cliente
            self.saldo = 0

        def deposito(self, valor: float):
            # Método para realizar um depósito na conta
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R${valor:.2f} realizado.")
                # Mostra mensagem de depósito realizado em um diálogo
                dlg1.title.value = f"Depósito de R${valor:.2f} realizado."
                page.dialog = dlg1
                dlg1.open = True
                saldo_atual.value = f": R${conta.saldo:.2f}"
                page.update()
            else:
                print("Valor de depósito inválido.")
                # Mostra mensagem de valor inválido em um diálogo
                dlg1.title.value = f"Valor de depósito inválido."
                page.dialog = dlg1
                dlg1.open = True
                saldo_atual.value = f": R${conta.saldo:.2f}"
                page.update()

        def saque(self, valor: float):
            # Método para realizar um saque na conta
            valor = float(valor)
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado.")
                # Mostra mensagem de saque realizado em um diálogo
                dlg1.title.value = f"Saque de R${valor:.2f} realizado."
                page.dialog = dlg1
                dlg1.open = True
                saldo_atual.value = f": R${conta.saldo:.2f}"
                page.update()
            else:
                print("Saldo insuficiente ou valor de saque inválido.")
                # Mostra mensagem de erro em um diálogo
                dlg1.title.value = f"Saldo insuficiente ou valor de saque inválido."
                page.dialog = dlg1
                dlg1.open = True
                saldo_atual.value = f": R${conta.saldo:.2f}"
                page.update()

        def consulta_saldo(self):
            # Método para consultar o saldo da conta
            print(f"Seu saldo atual é R${self.saldo:.2f}")
            # Mostra o saldo atual em um diálogo
            dlg1.open = False
            page.update()   
            dlg1.title.value = f"Ola {self.cliente.nome}!\nSeu saldo atual é R${self.saldo:.2f}"
            page.dialog = dlg1
            dlg1.open = True
            saldo_atual.value = f": R${conta.saldo:.2f}"
            page.update()

    # Variáveis para armazenar cliente e conta bancária
    cliente = None
    conta: ContaBancaria = None 
    cliente_conectado = None

    # Função para cadastrar um novo cliente
    def cadastrar(e):
        nonlocal conta, cliente_conectado, cliente
        # Verifica se todos os campos foram preenchidos 
        nome_val = nome.value.strip() 
        sobrenome_val = sobrenome.value.strip() 
        cpf_val = cpf.value.strip() 

        if nome_val == "" :
            nome.error_text="Nome inválido."
            dlg.title.value = "Digite seu primeiro nome!" 
            page.dialog = dlg
            dlg.open = True
            page.update()
        elif sobrenome_val == "" :
            sobrenome.error_text="Sobrenome inválido."
            dlg.title.value = "Digite seu sobrenome!" 
            page.dialog = dlg
            dlg.open = True
            page.update()
        elif len(cpf_val) != 11:
            cpf.error_text="CPF inválido.(necessario 11 números)"
            dlg.title.value = "Digite o seu CPF Corretamente! (apenas números)!"
            page.dialog = dlg
            dlg.open = True
            page.update()

        # Verifica se todos os campos foram preenchidos
        else:
            # Cria um novo cliente
            cliente = Cliente(nome_val, sobrenome_val, int(cpf_val))
            cliente_conectado = cliente.nome
            conta = ContaBancaria(cliente)
            dlg.title.value = f"Conta criada com sucesso!" 
            page.dialog = dlg
            dlg.open = True        
            opcoes()
            page.update()

    # Função para consultar o saldo da conta
    def saldo_consulta(e):
        if conta:
            conta.consulta_saldo()
        else:
            # Mostra mensagem de erro em um diálogo se nenhum cliente está cadastrado
            dlg.title.value = "Nenhum cliente cadastrado."
            page.dialog = dlg
            dlg.open = True
            page.update()

    # Função para lidar com o fechamento do diálogo de depósito
    def close_dlg(e):
        valor = float(e.content.value)
        dlg.open = False
        page.update()
        print(f"O valor digitado foi {valor}")
        
        if valor == "":
            # Mostra mensagem de valor inválido em um diálogo
            dlg.title.value = "Valor de depósito inválido." 
            page.dialog = dlg
            dlg.open = True
            page.update()
        
        # Realiza o depósito se a conta existe
        if conta is not None:
            conta.deposito(e.content.value)

    # Função para lidar com o diálogo de saque
    def saque_dlg(e):
        valor = float(e.content.value)
        dlg.open = False
        page.update()
        print(f"O valor digitado foi {valor}")
        
        if valor == "":
            # Mostra mensagem de valor inválido em um diálogo
            dlg.title.value = "Valor de saque inválido." 
            page.dialog = dlg
            dlg.open = True
            page.update()
        
        # Realiza o saque se a conta existe
        if conta is not None:
            conta.saque(e.content.value)

    # Função para exibir um diálogo para digitar o valor do depósito
    def alert_deposito():
        print("alert Deposito")
        dlg.title.value = "Digite Valor do Depósito"
        dlg.modal = True
        dlg.content = ft.TextField(label="Digite valor")
        dlg.actions = [ft.TextButton("Confirmar", on_click=lambda e: close_dlg(dlg))]
        page.dialog = dlg
        dlg.open = True
        page.update()
        
    # Função para iniciar o processo de depósito
    def realizar_deposito(e):
        print("realizar deposito")
        alert_deposito()

    # Função para iniciar o processo de saque
    def realizar_saques(e):
        print("Iniciando saque")
        dlg.title.value = "Digite valor do saque"
        dlg.modal = True
        dlg.content = ft.TextField(label="Digite valor (apenas números)")
        dlg.actions = [ft.TextButton("Sacar", on_click=lambda e: saque_dlg(dlg))]
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Função para finalizar a sessão
    def finalizar_sessao(e):
        # Mensagem de despedida 
        dlg1.title.value = f"Obrigado por confia na gente {cliente_conectado}\nVolte Sempre :D" 
        page.dialog = dlg1
        dlg1.open = True
        page.update()
        sleep(5)
        # Limpa a página e retorna à página inicial
        page.clean()
        sleep(2)
        main(page)

    # Função para exibir as opções disponíveis após o cadastro
    def opcoes():
        principal.width = 0
        principal.height = 0
        page.update()
        secundario.width = 300
        secundario.height = 450
        titulo_cliente.value = f"Seja bem-vindo(a) {cliente_conectado}!"
        saldo_atual.value = f": R${conta.saldo:.2f}"
        page.update()
        # Exibe informações do cliente (nome, sobrenome, CPF)
        print(cliente.nome, cliente.sobrenome, cliente.cpf) 

    

    # Diálogos para mostrar mensagens ao usuário
    dlg1 = ft.AlertDialog(
        title=ft.Text(value="Depósito realizado.",text_align=ft.TextAlign.CENTER),  
        on_dismiss=lambda e: print("Diálogo fechado!")
    )
    dlg = ft.AlertDialog(
        title=ft.Text(value="Cadastro realizado."),
        on_dismiss=lambda e: print("Diálogo fechado!")
    )

    # Elementos iniciais da página
    logo = ft.Image(src="img/unopar-anhanguera.jpg", width=300)
    develop = ft.Text("Desenvolvido por: Luiz Gustavo RA: 3534190203", size=12, color="grey")
    curso = ft.Text("Analise e desenvolvimento de sistemas", size=12, color="grey")
    version = ft.Text("Versão: 1.0.0", size=12, color="grey")
    projeto = ft.Text("Projeto: Linguagem Orientada a Objetos", size=12, color="grey")
    titulo = ft.Text("Bem-vindo ao Sistema Bancário UNOPAR",weight=900, size=20,) 
    nome = ft.TextField(label="Digite seu nome", icon=ft.icons.PERSON ,border_radius=10)
    sobrenome = ft.TextField(label="Digite seu sobrenome",icon=ft.icons.PERSON_ADD ,border_radius=10)
    cpf = ft.TextField(label="Digite seu CPF (apenas números)",icon=ft.icons.FINGERPRINT ,border_radius=10)
    cadastra = ft.ElevatedButton(text="Cadastrar", icon=ft.icons.CHECK,bgcolor="#fa780a",color=ft.colors.WHITE,width=150,height=50, on_click=cadastrar)
    coluna_principal = ft.Column(
        controls=[
                  ft.Row(controls=[logo],alignment="center"), 
                  ft.Row(controls=[titulo],alignment="center"), 
                  ft.Row(controls=[nome],alignment="center"),
                  ft.Row(controls=[sobrenome],alignment="center"), 
                  ft.Row(controls=[cpf],alignment="center"), 
                  ft.Row(controls=[cadastra],alignment="center"),
                  ft.Row(controls=[develop],alignment="center"),
                  ft.Row(controls=[curso],alignment="center"), 
                  ft.Row(controls=[projeto],alignment="center"),
                  ft.Row(controls=[version],alignment="center")],
                  alignment="center" 
    )

    # Elementos da interface de usuário
    titulo_cliente = ft.Text(f"Olá {cliente_conectado}!",weight=900, size=20,) 
    saldo_atual = ft.Text("",weight=500,size=12,)
    consulta = ft.ElevatedButton("Consulta Saldo",icon=ft.icons.ATTACH_MONEY,bgcolor="#fa780a",color=ft.colors.WHITE,width=200,height=50, on_click=saldo_consulta)
    deposito = ft.ElevatedButton("Realizar Depósito",icon=ft.icons.CURRENCY_EXCHANGE,bgcolor="#fa780a",color=ft.colors.WHITE,width=200,height=50, on_click=realizar_deposito)
    saques = ft.ElevatedButton("Realizar Saques",icon=ft.icons.WALLET,bgcolor="#fa780a",color=ft.colors.WHITE,width=200,height=50, on_click=realizar_saques)
    finalizar = ft.ElevatedButton("Finalizar Sessão",icon=ft.icons.CLOSE,bgcolor="#fa780a",color=ft.colors.WHITE,width=200,height=50, on_click=finalizar_sessao)
    coluna_opcoes = ft.Column(controls=[
        ft.Row(controls=[titulo_cliente],alignment="center"), 
        ft.Row(controls=[ft.Icon(name=ft.icons.PAYMENT, color="#fa780a"),saldo_atual],alignment="center"),
        ft.Row(controls=[consulta],alignment="center"), 
        ft.Row(controls=[deposito],alignment="center"), 
        ft.Row(controls=[saques],alignment="center"), 
        ft.Row(controls=[finalizar],alignment="center"), 
        ft.Row(controls=[develop],alignment="center"), 
        ft.Row(controls=[curso],alignment="center"), 
        ft.Row(controls=[projeto],alignment="center"), 
        ft.Row(controls=[version],alignment="center") 
        ],
        alignment="center")

    # Cria os elementos da página    
    principal = ft.Container(content=coluna_principal,border=ft.border.all(0.1 , "#fa780a"),border_radius=10,width=450,height=620,
        shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLUE_GREY_300,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
    
    secundario = ft.Container(content=coluna_opcoes,border=ft.border.all(2, "#fa780a"),border_radius=10,width=0,height=0,
        shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLUE_GREY_300,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ))
    # Adiciona os elementos à página
    page.add(principal,secundario)

# Inicia a aplicação
ft.app(main)
