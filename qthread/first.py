#Простая программа ддя создания потока
from PyQt5 import QtCore, QtWidgets

#Класс потока
class MyThread(QtCore.QThread):
   mysignal = QtCore.pyqtSignal(str)
   def __init__(self, parent=None):
      QtCore.QThread.__init__(self, parent)
   def run(self):
      self.mysignal.emit('Work!')
      self.sleep(3)
      self.mysignal.emit('Да работает')

#Класс окна
class MyWindow(QtWidgets.QWidget):
   def __init__(self, parent=None):
      QtWidgets.QWidget.__init__(self, parent)
      self.label = QtWidgets.QLabel('Для запуска нажмите кнопку')
      self.label.setAlignment(QtCore.Qt.AlignHCenter)
      self.button = QtWidgets.QPushButton('Старт')
      self.vbox = QtWidgets.QVBoxLayout()
      self.vbox.addWidget(self.label)
      self.vbox.addWidget(self.button)
      self.setLayout(self.vbox)
      self.thread = MyThread()
      self.button.clicked.connect(self.onClick)
      self.thread.mysignal.connect(self.onChange, QtCore.Qt.QueuedConnection)
   def onClick(self):
      self.button.setDisabled(True)
      self.thread.start()

   def onChange(self, text):
      self.label.setText(text)

if __name__ == '__main__':
   import sys
   app = QtWidgets.QApplication(sys.argv)
   window = MyWindow()
   window.setWindowTitle('Простая програамма с QThread')
   window.resize(400, 100)
   window.show()
   sys.exit(app.exec_())
