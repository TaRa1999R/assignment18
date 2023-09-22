
import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def numbers ( num ) :
    global number
    number = number + num
    window.textbox.setText ( number )

def minus () :
    global number
    number = "-" + number
    window.textbox.setText ( number )

def ac () :
    global number
    number = ""
    window.textbox.setText ( number )


def sum () : ...
def sub () : ...
def multi () : ...
def divide () : ...
def sqrt () : ...
def percent () : ...
def log () : ...
def sin () : ...
def cos () : ...
def tan () : ...
def cot () : ...
def equal () : ...

app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("calculator\calculator.ui")
number = ""
operation = ""

window.zero.clicked.connect ( partial ( numbers , "0" ))
window.one.clicked.connect ( partial ( numbers , "1" ))
window.two.clicked.connect ( partial ( numbers , "2" ))
window.three.clicked.connect ( partial ( numbers , "3" ))
window.four.clicked.connect ( partial ( numbers , "4" ))
window.five.clicked.connect ( partial ( numbers , "5" ))
window.six.clicked.connect ( partial ( numbers , "6" ))
window.seven.clicked.connect ( partial ( numbers , "7" ))
window.eight.clicked.connect ( partial ( numbers , "8" ))
window.nine.clicked.connect ( partial ( numbers , "9" ))
window.point.clicked.connect ( partial ( numbers , "." ))
window.minus.clicked.connect ( minus )

window.sum.clicked.connect ( sum )
window.sub.clicked.connect ( sub )
window.multi.clicked.connect ( multi )
window.divide.clicked.connect ( divide )
window.sqrt.clicked.connect ( sqrt )
window.log.clicked.connect ( log )
window.sin.clicked.connect ( sin )
window.cos.clicked.connect ( cos )
window.tan.clicked.connect ( tan )
window.cot.clicked.connect ( cot )
window.equal.clicked.connect ( equal )

window.ac.clicked.connect ( ac )


window.show ()
app.exec ()

