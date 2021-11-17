#Программа Hello world с помощью PyQt
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Привет, мир!")
window.resize(500, 200)
label = QtWidgets.QLabel("<center>Привет, мир!</center>")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
