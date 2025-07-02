# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets

## CONEXAO COM O BD ########################################
import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="escola")
cursor = conexao.cursor()
print("Conectou.")
############################################################

class Ui_ListarAluno(object):
    def setupUi(self, ListarAluno):
        ListarAluno.setObjectName("ListarAluno")
        ListarAluno.resize(299, 408)
        self.centralwidget = QtWidgets.QWidget(ListarAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botao_listar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_listar.setObjectName("botao_listar")
        
        self.botao_listar.clicked.connect(self.listar)
        
        self.verticalLayout.addWidget(self.botao_listar)
        self.text_dados = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_dados.setObjectName("text_dados")
        self.verticalLayout.addWidget(self.text_dados)
        ListarAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListarAluno)
        QtCore.QMetaObject.connectSlotsByName(ListarAluno)

    def retranslateUi(self, ListarAluno):
        _translate = QtCore.QCoreApplication.translate
        ListarAluno.setWindowTitle(_translate("ListarAluno", "Listagem de Alunos"))
        self.botao_listar.setText(_translate("ListarAluno", "LISTAR"))

    def listar(self):
        cursor.execute("SELECT * FROM aluno")
        
        dados = ""
        
        for linha in cursor:
            dados += "Codigo: " + str(linha[0]) + "\n"
            dados += "Nome : " + linha[1] + "\n"
            dados += "Curso: " + linha[2] + "\n"
            dados += "----------------------------\n"
        
        self.text_dados.setPlainText(dados)
        
        
            
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListarAluno = QtWidgets.QMainWindow()
    ui = Ui_ListarAluno()
    ui.setupUi(ListarAluno)
    ListarAluno.show()
    sys.exit(app.exec_())
