from PyQt5.QtWidgets import QApplication, QMainWindow

class window_class(QMainWindow):
	def __init__(self):
		from PyQt5.uic import loadUi
		super(window_class, self).__init__()
		self.setMouseTracking(True)
		loadUi('../../ui/mouse.ui', self)

	def mouseMoveEvent(self, e):
		mouse_pt = "x={0},y={1}, global={2},{3}".format(e.x(), e.y(), e.globalX(), e.globalY())
		self.label.setText(mouse_pt)
		print(mouse_pt)
		#return super().mouseMoveEvent(a0)

import sys
app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()