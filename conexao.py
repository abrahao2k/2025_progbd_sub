import mariadb   # ativar a biblioteca

# estabelecer a conexao com o servidor/banco
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco" )

# criar o objeto que executa os comandos
cursor = conexao.cursor()

# executar um comando SQL
cursor.execute(" INSERT INTO CLIENTE VALUES(null,'Marcos',280); ")

# confirmar a gravação
conexao.commit()

print("Gravado com sucesso.")