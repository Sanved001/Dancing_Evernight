# This file was on my computes so i decided to upload it to GitHub!



import os
import sys
from PyQt6 import QtWidgets, QtGui, QtCore



script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
sys.path.append(script_dir)


app = QtWidgets.QApplication([])


window = QtWidgets.QLabel()
window.setWindowFlags(
    QtCore.Qt.WindowType.FramelessWindowHint |   
    QtCore.Qt.WindowType.WindowStaysOnTopHint | 
    QtCore.Qt.WindowType.Tool                    
)


window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)


movie = QtGui.QMovie("evernightdanse-evernight.gif")
window.setMovie(movie)
movie.start()



screen = app.primaryScreen().availableGeometry()
gif_width = movie.frameRect().width()
gif_height = movie.frameRect().height()
x = screen.width() - gif_width
y = screen.height() - gif_height
window.setGeometry(x, y, gif_width, gif_height)

window.show()
sys.exit(app.exec())
