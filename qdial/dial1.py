#Круговая шкала с ползунком
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Круговая шкала с ползунком')
window.resize(400, 400)
dial = QtWidgets.QDial()
dial.setNotchesVisible(True) #Отображать риски
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(dial)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
