import sys
from PyQt5.QtWidgets import *

class MyMain(QMainWindow):
	def __init__(self):
		super().__init__()
		self.statusbar = self.statusBar()
		print(self.hasMouseTracking())
		self.setMouseTracking(True)   # True 면, mouse button 안눌러도 , mouse move event 추적함.
		print(self.hasMouseTracking())
		self.setGeometry(300, 200, 400, 200)
		self.show()

		def mouseMoveEvent(self, event):
			txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
			self.statusbar.showMessage(txt)
			print(event.globalX())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyMain()
	sys.exit(app.exec_())