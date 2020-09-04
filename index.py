from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from main import *
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,100)
is_running = False

def set_DFS():
    global is_running
    if is_running:
        pygame.quit()
        is_running=False
    is_running=True
    main(600,50,"DFS")

def set_BFS():
    global is_running
    if is_running:
        pygame.quit()
        is_running=False
    is_running=True
    main(600,50,"BFS")

def window():
        app = QApplication(sys.argv)
        win = QMainWindow()
        width=300
        height=300
        win.setGeometry(140,280,width,height)
        win.setWindowTitle("Path finder")

        b1=QtWidgets.QPushButton(win)
        b1.setText("DFS")
        b1.clicked.connect(set_DFS)

        b2=QtWidgets.QPushButton(win)
        b2.setText("BFS")
        b2.clicked.connect(set_BFS)
        b2.setGeometry(QtCore.QRect(100, 100, 93, 28))

        win.show()
        sys.exit(app.exec_())
window()
