#Программа c QColorDialog
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Программа c QColorDialog")
window.resize(500, 200)
colors = QtWidgets.QColorDialog()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(colors)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
