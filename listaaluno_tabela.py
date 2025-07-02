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
        ListarAluno.resize(350, 400)
        self.centralwidget = QtWidgets.QWidget(ListarAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botao_listar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_listar.setObjectName("botao_listar")
        self.botao_listar.clicked.connect(self.listar)
        
        self.verticalLayout.addWidget(self.botao_listar)
        self.table_dados = QtWidgets.QTableWidget(self.centralwidget)
        self.table_dados.setObjectName("table_dados")
        self.table_dados.setColumnCount(3)
        self.table_dados.setHorizontalHeaderLabels(["Código", "Nome", "Curso"])
        self.table_dados.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.table_dados)
        
        ListarAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListarAluno)
        QtCore.QMetaObject.connectSlotsByName(ListarAluno)

    def retranslateUi(self, ListarAluno):
        _translate = QtCore.QCoreApplication.translate
        ListarAluno.setWindowTitle(_translate("ListarAluno", "Listagem de Alunos"))
        self.botao_listar.setText(_translate("ListarAluno", "LISTAR"))

    def listar(self):
        cursor.execute("SELECT * FROM aluno")
        resultados = cursor.fetchall()

        self.table_dados.setRowCount(len(resultados))

        for i, linha in enumerate(resultados):
            for j, valor in enumerate(linha):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.table_dados.setItem(i, j, item)
        
        self.table_dados.resizeColumnsToContents()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListarAluno = QtWidgets.QMainWindow()
    ui = Ui_ListarAluno()
    ui.setupUi(ListarAluno)
    ListarAluno.show()
    sys.exit(app.exec_())
