def cadastrar():
    titulo = input("Digite o título: ")
    plataforma = input("Digite a plataforma: ")
    #...insert...

def pesquisar():
    titulo = input("Digite o título a ser pesquisado: ")
    #...select...

def excluir():
    cod = input("Código a ser excluído: ")
    #...delete...
    
while True:
    print("*** MENU ***")
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Excluir")
    opcao = input("Digite uma opção: ")
