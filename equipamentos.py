## CONEXÃO ##############################################
import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="empresa")
cursor = conexao.cursor()
#print("Conexao OK.")

## CADASTRAR #############################################

def cadastrar() :
    print("=== CADASTRAR EQUIPAMENTO ===")
    descricao = input("Descrição do equipamento: ")
    marca = input("Marca: ")
    valor = input("Valor: ")
    
    sql = f'''INSERT INTO equipamento VALUES
              (null,'{descricao}','{marca}',
              {valor.replace(',','.')}); '''
    
    cursor.execute(sql)
    conexao.commit()
    print("CADASTRADO COM SUCESSO!\n")

## PESQUISAR ##############################################

def pesquisar() :
    print("=== PESQUISAR EQUIPAMENTO ===")
    descricao = input("Descrição: ")
    marca = input("Marca: ")
    print("----------------------------------")
    
    sql = f'''SELECT * FROM equipamento
              WHERE descricao LIKE '%{descricao}%'
              AND marca LIKE '%{marca}%';  '''

    cursor.execute(sql)
    
    if cursor.rowcount > 0 :
        for linha in cursor:
            print(f"Código: {linha[0]}")
            print(f"Descrição: {linha[1]}")
            print(f"Marca: {linha[2]}")
            print(f"Valor: R$ {linha[3]:.2f}")
            print("----------------------------------")
        print(cursor.rowcount, "item(ns) encontrados.")
    else:
        print("Nenhum item encontrado.")
        print("----------------------------------")

## EXCLUIR ################################################
        
def excluir() :
    print("=== EXCLUIR EQUIPAMENTO ===")
    codigo = input("Código do equipamento: ")
    
    sql = f"SELECT * FROM equipamento WHERE codigo = {codigo}"
    cursor.execute(sql)
    
    if cursor.rowcount == 0 :
        print("Código não encontrado.\n")
    
    else:
        linha = cursor.fetchone()  # transfere o resultado para uma variável
        print(linha)
        resp = input("Excluir? (s/n) ")
        if resp == 's':
            cursor.execute(f"DELETE FROM equipamento WHERE codigo = {codigo}")
            conexao.commit()
            print("Excluído com sucesso.\n")
        else:
            print("Nada foi excluído.\n")
    
    
## ATUALIZAR ###############################################

def atualizar() :
    print("=== ATUALIZAR EQUIPAMENTO ===")
    codigo = input("Código do equipamento: ")
    cursor.execute(f"SELECT * FROM equipamento WHERE codigo = {codigo}")
    if cursor.rowcount == 0 :
        print("Código não encontrado.\n")
    else:
        linha = cursor.fetchone()  # transfere o resultado para uma variável
        print(linha)
        resp = input("Atualizar este equipamento? (s/n) ")
        if resp == 's' :
            coluna = input("Qual coluna? (descricao/marca/valor) ")
            if coluna in ('descricao','marca','valor') :
                nova = input("Nova informação: ")
                cursor.execute(f''' UPDATE equipamento
                                   SET {coluna} = '{nova.replace(',','.')}'
                                   WHERE codigo = {codigo} ''')
                conexao.commit()
                print("Atualizado com sucesso.")
            else:
                print("Coluna não existe.")
        else:
            print("Nada foi alterado.")

## MENU ###################################################
            
while True:
    print("=== SISTEMA DE CONTROLE DE EQUIPAMENTOS ===")
    print(" 1-Cadastrar\n 2-Pesquisar\n 3-Excluir\n 4-Alterar\n 5-Sair")
    opcao = int(input("Opção? "))
    
    if   opcao == 1: cadastrar()
    elif opcao == 2: pesquisar()
    elif opcao == 3: excluir()
    elif opcao == 4: atualizar()
    else: break