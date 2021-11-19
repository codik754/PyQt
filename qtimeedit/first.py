#Программа с QTimeEdit
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QTimeEdit')
window.resize(300, 200)
time = QtWidgets.QTimeEdit()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(time)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
