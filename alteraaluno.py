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

class Ui_AlteraAluno(object):
    def setupUi(self, AlteraAluno):
        AlteraAluno.setObjectName("AlteraAluno")
        AlteraAluno.resize(315, 251)
        self.centralwidget = QtWidgets.QWidget(AlteraAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 1, 0, 1, 1)
        self.combo_curso = QtWidgets.QComboBox(self.centralwidget)
        self.combo_curso.setObjectName("combo_curso")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.gridLayout.addWidget(self.combo_curso, 2, 2, 1, 1)
        self.line_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nome.setObjectName("line_nome")
        self.gridLayout.addWidget(self.line_nome, 1, 2, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 2, 0, 1, 1)
        self.label_obs = QtWidgets.QLabel(self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 5, 0, 1, 1)
        self.text_obs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_obs.setObjectName("text_obs")
        self.gridLayout.addWidget(self.text_obs, 5, 2, 1, 1)
        self.horizontalLayout_extra = QtWidgets.QHBoxLayout()
        self.horizontalLayout_extra.setObjectName("horizontalLayout_extra")
        self.check_atleta = QtWidgets.QCheckBox(self.centralwidget)
        self.check_atleta.setObjectName("check_atleta")
        self.horizontalLayout_extra.addWidget(self.check_atleta)
        self.check_bolsista = QtWidgets.QCheckBox(self.centralwidget)
        self.check_bolsista.setObjectName("check_bolsista")
        self.horizontalLayout_extra.addWidget(self.check_bolsista)
        self.gridLayout.addLayout(self.horizontalLayout_extra, 4, 2, 1, 1)
        self.label_turno = QtWidgets.QLabel(self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 3, 0, 1, 1)
        self.botao_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName("botao_salvar")
        self.gridLayout.addWidget(self.botao_salvar, 6, 2, 1, 1)
        self.horizontalLayout_turno = QtWidgets.QHBoxLayout()
        self.horizontalLayout_turno.setObjectName("horizontalLayout_turno")
        self.radio_manha = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_manha.setObjectName("radio_manha")
        self.horizontalLayout_turno.addWidget(self.radio_manha)
        self.radio_tarde = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_tarde.setObjectName("radio_tarde")
        self.horizontalLayout_turno.addWidget(self.radio_tarde)
        self.radio_noite = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_noite.setObjectName("radio_noite")
        self.horizontalLayout_turno.addWidget(self.radio_noite)
        self.gridLayout.addLayout(self.horizontalLayout_turno, 3, 2, 1, 1)
        self.label_extra = QtWidgets.QLabel(self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.gridLayout.addWidget(self.label_extra, 4, 0, 1, 1)
        self.label_codigo = QtWidgets.QLabel(self.centralwidget)
        self.label_codigo.setObjectName("label_codigo")
        self.gridLayout.addWidget(self.label_codigo, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_codigo.setObjectName("line_codigo")
        self.horizontalLayout_3.addWidget(self.line_codigo)
        self.botao_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.botao_abrir.setObjectName("botao_abrir")
        
        self.botao_abrir.clicked.connect(self.abrir)
        
        self.horizontalLayout_3.addWidget(self.botao_abrir)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        AlteraAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlteraAluno)
        QtCore.QMetaObject.connectSlotsByName(AlteraAluno)

    def retranslateUi(self, AlteraAluno):
        _translate = QtCore.QCoreApplication.translate
        AlteraAluno.setWindowTitle(_translate("AlteraAluno", "Alteração de Aluno"))
        self.label_nome.setText(_translate("AlteraAluno", "Nome:"))
        self.combo_curso.setItemText(0, _translate("AlteraAluno", "Edificações"))
        self.combo_curso.setItemText(1, _translate("AlteraAluno", "Eletrotécnica"))
        self.combo_curso.setItemText(2, _translate("AlteraAluno", "Informática"))
        self.combo_curso.setItemText(3, _translate("AlteraAluno", "Mecânica"))
        self.label_curso.setText(_translate("AlteraAluno", "Curso:"))
        self.label_obs.setText(_translate("AlteraAluno", "Obs.:"))
        self.check_atleta.setText(_translate("AlteraAluno", "Atleta"))
        self.check_bolsista.setText(_translate("AlteraAluno", "Bolsista"))
        self.label_turno.setText(_translate("AlteraAluno", "Turno:"))
        self.botao_salvar.setText(_translate("AlteraAluno", "SALVAR"))
        self.radio_manha.setText(_translate("AlteraAluno", "Manhã"))
        self.radio_tarde.setText(_translate("AlteraAluno", "Tarde"))
        self.radio_noite.setText(_translate("AlteraAluno", "Noite"))
        self.label_extra.setText(_translate("AlteraAluno", "Extra:"))
        self.label_codigo.setText(_translate("AlteraAluno", "Código:"))
        self.botao_abrir.setText(_translate("AlteraAluno", "ABRIR"))
        
        
    def abrir(self):
        #capturar o código digitado
        codigo = self.line_codigo.text()
        
        cursor.execute("SELECT * FROM aluno WHERE codigo = " + codigo)
        
        if cursor.rowcount == 0 :
            print("CÓDIGO NÃO ENCONTRADO.")
            
        else: # carregar dados no formulario
            dados = cursor.fetchone()
            
            self.line_nome.setText(dados[1])
            
            self.combo_curso.setCurrentText(dados[2])
            
            if   dados[3] == "Manhã" : self.radio_manha.setChecked(True)
            elif dados[3] == "Tarde" : self.radio_tarde.setChecked(True)
            elif dados[3] == "Noite" : self.radio_noite.setChecked(True)
            
            if dados[4] == "Sim" : self.check_atleta.setChecked(True)
            else: self.check_atleta.setChecked(False)
            
            if dados[5] == "Sim" : self.check_bolsista.setChecked(True)
            else: self.check_bolsista.setChecked(False)
            
            self.text_obs.setPlainText(dados[6])
            
            
            
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlteraAluno = QtWidgets.QMainWindow()
    ui = Ui_AlteraAluno()
    ui.setupUi(AlteraAluno)
    AlteraAluno.show()
    sys.exit(app.exec_())
