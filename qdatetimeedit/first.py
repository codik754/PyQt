#Программа с QDateTimeEdit
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QDateTimeEdit')
window.resize(500, 200)
datetime = QtWidgets.QDateTimeEdit()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(datetime)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
