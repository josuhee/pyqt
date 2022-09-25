import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPainterPath
from PyQt5.QtCore import Qt
class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	
	def initUI(self):
		self.setGeometry(300, 300, 400, 400)
		self.setWindowTitle('QPainter를 이용한 그래픽스')
		self.show()

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.drawText(event, qp)
		qp.drawEllipse(100, 100, 50, 50)
		qp.end()

	def drawText(self, event, qp):
		qp.setPen(QColor(0, 0, 0))
		qp.setFont(QFont('나눔명조', 35))
		qp.drawText(event.rect(), Qt.AlignCenter, '스산한 늦가을\n아니.. 초겨울인가?')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWindow()
	sys.exit(app.exec_())