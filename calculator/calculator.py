
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


def sum () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "+"
    number = ""
    window.textbox.setText ( number )

def sub () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "-"
    number = ""
    window.textbox.setText ( number )

def multi () :
    global number 
    global operation
    global first 
    first = float ( number )
    operation = "*"
    number = ""
    window.textbox.setText ( number )

def divide () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "/"
    number = ""
    window.textbox.setText ( number )

def sqrt () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "sqrt"
    number = f"sqrt({first})"
    window.textbox.setText ( number )

def percent () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "%"
    number = f"{first}%"
    window.textbox.setText ( number )

def log () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "log"
    number = f"log({first})"
    window.textbox.setText ( number )

def sin () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "sin"
    number = f"sin({first})"
    window.textbox.setText ( number )

def cos () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "cos"
    number = f"cos({first})"
    window.textbox.setText ( number )

def tan () : 
    global number
    global operation
    global first
    first = float ( number )
    operation = "tan"
    number = f"tan({first})"
    window.textbox.setText ( number )

def cot () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "cot"
    number = f"cot({first})"
    window.textbox.setText ( number )

def equal () :
    global number
    global operation
    global first
    
    if operation == "+" or operation == "-" or operation == "*" or operation == "/" :
        second = float ( number )
        if operation == "+" :
            result = first + second
        
        elif operation == "-" :
            result = first - second

        elif operation == "*" :
            result = first * second

        elif operation == "/" :
            if second == 0 :
                result = "        Error!!"
            
            else :
                result = first / second
        
    else :
        if operation == "sqrt" :
            if first < 0 :
                result = "        Error!!"

            else :
                result = math.sqrt ( first)

        elif operation == "%" :
            result = first / 100

        elif operation == "log" :
            result = math.log10 ( first )

        elif operation == "sin" :
            rad = first * ( math.pi / 180 )
            result = math.sin ( rad )

        elif operation == "cos" :
            rad = first * ( math.pi / 180 )
            result = math.cos ( rad )

        elif operation == "tan" :
            rad = first * ( math.pi / 180 )
            result = math.tan ( rad )

        elif operation == "cot" :
            rad = first * ( math.pi / 180 )
            result = 1 / math.tan ( rad )

    window.textbox.setText ( str ( result ))
    number = ""
    first = ""
    operation = ""

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
window.percent.clicked.connect ( percent )
window.log.clicked.connect ( log )
window.sin.clicked.connect ( sin )
window.cos.clicked.connect ( cos )
window.tan.clicked.connect ( tan )
window.cot.clicked.connect ( cot )
window.equal.clicked.connect ( equal )
window.ac.clicked.connect ( ac )

window.show ()
app.exec ()