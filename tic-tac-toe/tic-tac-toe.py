
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox

app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("tic-tac-toe/tic-tac-toe.ui")

window.show ()
app.exec ()