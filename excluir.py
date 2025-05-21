import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="videogames")
cursor = conexao.cursor()

cod = input("Codigo do jogo a ser excluído: ")

cursor.execute(f"SELECT * FROM jogos WHERE codigo = {cod}")

if cursor.rowcount == 0 :
    print("Registro não encontrado.")
else:
    linha = cursor.fetchone()
    print(linha)
    
    resp = input("Confirma a exclusão? (s/n) ")
    if resp == 's' :
        cursor.execute(f"DELETE FROM jogos WHERE codigo = {cod}")
        conexao.commit() # confirma a exclusão
        print("Exculído com sucesso.")
    else:
        print("Nada foi excluído.")

conexao.close() # finaliza a conexão