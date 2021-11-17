#Простая программа с кнопкой
from PyQt5 import QtWidgets
import sys

def onClick():
   print("Есть клик!")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Программа с кнопкой")
window.resize(500, 200)
button = QtWidgets.QPushButton("Нажми эту кнопку")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
button.clicked.connect(onClick)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
