import mariadb
conexao = mariadb.connect(host="localhost",user="root",password="",
                          database="banco")
cursor = conexao.cursor()

### PESQUISAR PELO NOME DO CLIENTE ####################################
nome = input("Nome do cliente: ")

cursor.execute(f"SELECT * FROM CLIENTE WHERE nome LIKE '%{nome}%' ")  

for linha in cursor:
    #print(linha)          # (1, 'Ana', 2000)  # tupla
    print("Código:", linha[0])
    print("Nome:  ", linha[1])
    print("Saldo: ", linha[2])
    print("-------------------")

print(cursor.rowcount, " resultados encontrados.")

# converter em lista
#lista = cursor.fetchall()
#print("Tamanho da lista:", len(lista))