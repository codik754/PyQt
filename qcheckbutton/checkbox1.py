#Программа с QCheckBox
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Использование QGroupBox')
window.resize(250, 100)
r1 = QtWidgets.QCheckBox('Да')
r2 = QtWidgets.QCheckBox('Не знаю')
r3 = QtWidgets.QCheckBox('Нет')
groupBox = QtWidgets.QGroupBox('2 * 2 = 4???  ')
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(r1)
hbox.addWidget(r2)
hbox.addWidget(r3)
groupBox.setLayout(hbox)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(groupBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
