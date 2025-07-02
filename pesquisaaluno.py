from PyQt5 import QtCore, QtGui, QtWidgets

## CONEXAO COM O BD ########################################
import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="escola")
cursor = conexao.cursor()
print("Conectou.")
############################################################

class Ui_PesqAlunos(object):
    def setupUi(self, PesqAlunos):
        PesqAlunos.setObjectName("PesqAlunos")
        PesqAlunos.resize(376, 359)
        self.centralwidget = QtWidgets.QWidget(PesqAlunos)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_pesquisa = QtWidgets.QLineEdit(self.centralwidget)
        self.line_pesquisa.setObjectName("line_pesquisa")
        self.horizontalLayout.addWidget(self.line_pesquisa)
        self.botao_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_pesquisar.setObjectName("botao_pesquisar")
        
        self.botao_pesquisar.clicked.connect(self.pesquisar)
        
        self.horizontalLayout.addWidget(self.botao_pesquisar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.text_dados = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_dados.setObjectName("text_dados")
        self.verticalLayout.addWidget(self.text_dados)
        PesqAlunos.setCentralWidget(self.centralwidget)

        self.retranslateUi(PesqAlunos)
        QtCore.QMetaObject.connectSlotsByName(PesqAlunos)

    def retranslateUi(self, PesqAlunos):
        _translate = QtCore.QCoreApplication.translate
        PesqAlunos.setWindowTitle(_translate("PesqAlunos", "Pesquisa de Alunos"))
        self.label.setText(_translate("PesqAlunos", "Nome ou Curso:"))
        self.botao_pesquisar.setText(_translate("PesqAlunos", "Pesquisar"))
    
    
    def pesquisar(self):
        pesq = self.line_pesquisa.text() # capturar o texto digitado
        
        sql = f'''SELECT * FROM aluno WHERE nome LIKE '%{pesq}%'
                    OR curso LIKE '%{pesq}%'; '''
        
        cursor.execute(sql)
        
        dados = ""
        
        for linha in cursor:
            dados += "Codigo: " + str(linha[0]) + "\n"
            dados += "Nome : " + linha[1] + "\n"
            dados += "Curso: " + linha[2] + "\n"
            dados += "----------------------------\n"
        
        dados += str(cursor.rowcount) + " registros encontrados."
        
        self.text_dados.setPlainText(dados)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PesqAlunos = QtWidgets.QMainWindow()
    ui = Ui_PesqAlunos()
    ui.setupUi(PesqAlunos)
    PesqAlunos.show()
    sys.exit(app.exec_())
