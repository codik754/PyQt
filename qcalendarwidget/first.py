#Программа с QCalendarWidget
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QTimeEdit')
window.resize(300, 300)
cal = QtWidgets.QCalendarWidget()
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(cal)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
