from PyQt5.QtWidgets import QApplication, QMainWindow

class window_class(QMainWindow):
	def __init__(self):
		from PyQt5.uic import loadUi
		super(window_class, self).__init__()
		loadUi('../../ui/mouse.ui', self)

	def mousePressEvent(self, e):
		mouse_pt = "x={0},y={1}, global={2},{3}".format(e.x(), e.y(), e.globalX(), e.globalY())
		self.label.setText(mouse_pt)
		print('click')

import sys
app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()