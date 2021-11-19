#Программа с QTextEdit
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QTextEdit')
window.resize(500, 500)
text = QtWidgets.QTextEdit()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(text)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
