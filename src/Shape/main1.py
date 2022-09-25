from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class window_class(QMainWindow):
	def __init__(self):
		from PyQt5.uic import loadUi
		super(window_class, self).__init__()
		loadUi('../../ui/shape.ui', self)
		self.image = QImage(QSize(711, 441), QImage.Format_RGB32)
		self.image.fill(Qt.white)
		self.draw = False

	def paintEvent(self, e):
		from PyQt5 import QtGui

		canvas = QPainter(self)
		qpixmp = QtGui.QPixmap.fromImage(self.image)
		self.label.setPixmap(qpixmp)

	def mousePressEvent(self, e):
		self.drawCircle(e.x(), e.y())

	def drawCircle(self, x, y):
		x -= 50
		y -= 150

		qp = QPainter(self.image)
		qp.setPen(QPen(Qt.blue, 3))
		qp.drawEllipse(x, y, 20, 20)
		self.update()

import sys
app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()