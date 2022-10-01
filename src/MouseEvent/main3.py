from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class window_class(QMainWindow):
	def __init__(self):
		from PyQt5.uic import loadUi
		super(window_class, self).__init__()
		loadUi('../../ui/mouse.ui', self)

	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			click = 'Left Mouse'
		if e.button() == Qt.MidButton:
			click = 'Middle Mouse'
		if e.button() == Qt.RightButton:
			click = 'Right Mouse'
		self.label.setText(click)

import sys
app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()