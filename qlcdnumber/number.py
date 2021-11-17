#Программа c QLCDNumber
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Программа c QLCDNumber")
window.resize(500, 200)
lcdNumber = QtWidgets.QLCDNumber(8)
lcdNumber.display(12345678)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(lcdNumber)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
