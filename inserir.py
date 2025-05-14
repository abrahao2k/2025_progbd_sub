import mariadb   # ativar a biblioteca
# estabelecer a conexao com o servidor/banco
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="banco" )
# criar o objeto que executa os comandos
cursor = conexao.cursor()

nome = input("Digite o nome do cliente: ")
saldo = input("Digite o saldo do cliente: ") 
saldo = saldo.replace(',' , '.') # troca virgula/ponto na casa decimal

# executar um comando SQL
cursor.execute(f" INSERT INTO CLIENTE VALUES(null,'{nome}', {saldo}); ")
# confirmar a gravação
conexao.commit()

print("Gravado com sucesso.")