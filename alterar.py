try:
    import mariadb
    conexao = mariadb.connect(host="localhost",user="ro",
                              password="", database="videogames")
    cursor = conexao.cursor()

    cod = input("Codigo do jogo a ser alterado: ")

    cursor.execute(f"SELECT * FROM jogos WHERE codigo = {cod}")

    if cursor.rowcount == 0 :
        print("Registro não encontrado.")
    else:
        linha = cursor.fetchone()
        print(linha)
        
        coluna = input("Qual informação deseja alterar? (titulo/plataforma) ")
        
        if coluna in ("titulo","plataforma"):
            valor = input("Digite a atualização: ")        
            cursor.execute(
                f"UPDATE jogos SET {coluna} = '{valor}' WHERE codigo = {cod}")
            conexao.commit()
            print("Atualizado com sucesso.")
        else:
            print("Coluna não existe.")
            
    conexao.close()

except ModuleNotFoundError:
    print("Erro ao importar o driver do banco de dados.")

except mariadb.OperationalError:
    print("Erro ao estabelecer a conexão.")
    
except:
    raise