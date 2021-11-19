#Программа с QTabWidget
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Программа с QTabWidget')
window.resize(500, 200)
t = QtWidgets.QTabWidget() #Создаем объкт QTatWidgets
t.addTab(QtWidgets.QLabel('Тут написан текст вкладки 1'), 'Вкладка &1')
t.addTab(QtWidgets.QLabel('Тут написан текст вкладки 2'), 'Вкладка &2')
t.addTab(QtWidgets.QLabel('Тут написан текст вкладки 3'), 'Вкладка &3')
t.addTab(QtWidgets.QLabel('Тут написан текст вкладки 4'), 'Вкладка &4')
t.addTab(QtWidgets.QLabel('Тут написан текст вкладки 5'), 'Вкладка &5')
t.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(t)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
