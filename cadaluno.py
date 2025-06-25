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

class Ui_CadAluno(object):
    def setupUi(self, CadAluno):
        CadAluno.setObjectName("CadAluno")
        CadAluno.resize(259, 227)
        self.centralwidget = QtWidgets.QWidget(CadAluno)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.line_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nome.setObjectName("line_nome")
        self.gridLayout.addWidget(self.line_nome, 0, 1, 1, 1)
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.combo_curso = QtWidgets.QComboBox(self.centralwidget)
        self.combo_curso.setObjectName("combo_curso")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.gridLayout.addWidget(self.combo_curso, 1, 1, 1, 1)
        self.label_turno = QtWidgets.QLabel(self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 2, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_turno, 2, 1, 1, 1)
        self.label_extra = QtWidgets.QLabel(self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.gridLayout.addWidget(self.label_extra, 3, 0, 1, 1)
        self.horizontalLayout_extra = QtWidgets.QHBoxLayout()
        self.horizontalLayout_extra.setObjectName("horizontalLayout_extra")
        self.check_atleta = QtWidgets.QCheckBox(self.centralwidget)
        self.check_atleta.setObjectName("check_atleta")
        self.horizontalLayout_extra.addWidget(self.check_atleta)
        self.check_bolsista = QtWidgets.QCheckBox(self.centralwidget)
        self.check_bolsista.setObjectName("check_bolsista")
        self.horizontalLayout_extra.addWidget(self.check_bolsista)
        self.gridLayout.addLayout(self.horizontalLayout_extra, 3, 1, 1, 1)
        self.label_obs = QtWidgets.QLabel(self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 4, 0, 1, 1)
        self.text_obs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_obs.setObjectName("text_obs")
        self.gridLayout.addWidget(self.text_obs, 4, 1, 1, 1)
        self.botao_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName("botao_salvar")
## CLIQUE DO BOTÃO ########################################################
        self.botao_salvar.clicked.connect(self.salvar)
########################################################################### 
        self.gridLayout.addWidget(self.botao_salvar, 5, 1, 1, 1)
        CadAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadAluno)
        QtCore.QMetaObject.connectSlotsByName(CadAluno)

    def retranslateUi(self, CadAluno):
        _translate = QtCore.QCoreApplication.translate
        CadAluno.setWindowTitle(_translate("CadAluno", "Cadastro de Aluno"))
        self.label_nome.setText(_translate("CadAluno", "Nome:"))
        self.label_curso.setText(_translate("CadAluno", "Curso:"))
        self.combo_curso.setItemText(0, _translate("CadAluno", "Edificações"))
        self.combo_curso.setItemText(1, _translate("CadAluno", "Eletrotécnica"))
        self.combo_curso.setItemText(2, _translate("CadAluno", "Informática"))
        self.combo_curso.setItemText(3, _translate("CadAluno", "Mecânica"))
        self.label_turno.setText(_translate("CadAluno", "Turno:"))
        self.radio_manha.setText(_translate("CadAluno", "Manhã"))
        self.radio_tarde.setText(_translate("CadAluno", "Tarde"))
        self.radio_noite.setText(_translate("CadAluno", "Noite"))
        self.label_extra.setText(_translate("CadAluno", "Extra:"))
        self.check_atleta.setText(_translate("CadAluno", "Atleta"))
        self.check_bolsista.setText(_translate("CadAluno", "Bolsista"))
        self.label_obs.setText(_translate("CadAluno", "Obs.:"))
        self.botao_salvar.setText(_translate("CadAluno", "SALVAR"))

## FUNÇÃO DO BOTÃO SALVAR ################################################
    def salvar(self):
        nome = self.line_nome.text()
        curso = self.combo_curso.currentText()
        
        turno = ""
        if self.radio_manha.isChecked()  : turno = "Manhã"
        elif self.radio_tarde.isChecked(): turno = "Tarde"
        elif self.radio_noite.isChecked(): turno = "Noite"
        
        atleta = "Não"
        if self.check_atleta.isChecked(): atleta = "Sim"
                
        bolsista = "Não"
        if self.check_bolsista.isChecked(): bolsista = "Sim"
        
        obs = self.text_obs.toPlainText()
        
        #print(nome, curso, turno, atleta, bolsista, obs)
        
        sql = f'''INSERT INTO ALUNO VALUES(null,'{nome}', '{curso}',
                  '{turno}', '{atleta}', '{bolsista}', '{obs}') '''
        
        cursor.execute(sql)
        conexao.commit()
        print("GRAVADO COM SUCESSO.")
        
#####################################################################        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadAluno = QtWidgets.QMainWindow()
    ui = Ui_CadAluno()
    ui.setupUi(CadAluno)
    CadAluno.show()
    sys.exit(app.exec_())