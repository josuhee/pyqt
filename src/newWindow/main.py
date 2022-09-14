from PyQt5.QtWidgets import QApplication, QMainWindow

class window_class(QMainWindow):
	def __init__(self):
		from PyQt5.uic import loadUi
		super(window_class, self).__init__()
		loadUi('../../ui/ex1.ui', self)

import sys
app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()