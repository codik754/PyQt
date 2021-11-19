#Программа с QTimeEdit
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QDateEdit')
window.resize(500, 200)
date = QtWidgets.QDateEdit()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(date)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
