import sys
import random

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow



class App(QMainWindow):

    def __init__(self, title : str, xPop: int = 0, yPop : int = 0, width : int = 500, height : int = 350):
        super(App, self).__init__()
        self.initUI()

        self.setGeometry(xPop, yPop, width, height)
        self.setWindowTitle("Title")


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Are you stupid ?")
        self.label.setStyleSheet("font-size : 11pt")
        self.label.move(200, 150)


        self.yesButton = QtWidgets.QPushButton(self)
        self.yesButton.setText("Yes")
        self.yesButton.move(100, 275)
        self.yesButton.clicked.connect(self.yesClicked)

        self.noButton = QtWidgets.QPushButton(self)
        self.noButton.setText("No")
        self.noButton.move(300, 275)
        self.noButton.clicked.connect(self.noClicked)


    def yesClicked(self):
        self.label.setText("I knew it !")


    def noClicked(self):
        positionsList = [
            (250, 250), (250, 275), (250, 300), (250, 325),
            (275, 250), (275, 275), (275, 300), (275, 325),
            (300, 250), (300, 275), (300, 300), (300, 325),
            (325, 250), (325, 275), (325, 300), (325, 325), 
            (350, 250), (350, 275), (350, 300), (350, 325)
        ]
        
        width, height = random.choice(positionsList)

        self.noButton.move(width, height)



def window():
    app = QApplication(sys.argv)
    win = App("My Title")
    
    win.show()
    sys.exit(app.exec_())


window()
