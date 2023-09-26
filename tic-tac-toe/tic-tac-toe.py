
import random
from functools import partial
from PySide6.QtWidgets import QApplication , QMessageBox
from PySide6.QtUiTools import QUiLoader

def statement ( condition ) :
    global state
    state = condition

def play ( row , column ) :
    global player
    global score_x
    global score_tie
    global score_o
    global message
    global state

    if state == "player" :
        if buttons[row][column].text() == "" :
        
            if player == 1 :
                buttons[row][column].setText ("X")
                buttons[row][column].setStyleSheet("color : red ; background-color : pink")
                mode = result ()

                if mode == "win" :
                    message = QMessageBox ( text = "🎉🎉 X WINNER 🎉🎉")
                    message.show ()
                    score_x += 1
                    next_round ()
                
                else :
                    window.turn.setText ("                      O Turn")
                    player = 2

            elif player == 2 :
                buttons[row][column].setText ("O")
                buttons[row][column].setStyleSheet("color : blue ; background-color : lightblue")
                mode = result ()

                if mode == "win" :
                    message = QMessageBox ( text = "🎉🎉 O WINNER 🎉🎉")
                    message.show ()
                    score_o += 1
                    next_round ()
                
                else :
                    window.turn.setText ("                      X Turn")
                    player = 1
    
    if state == "computer" :
        
        if buttons[row][column].text() == "" :
            if player == 1 : 
                buttons[row][column].setText ("X")
                buttons[row][column].setStyleSheet("color : red ; background-color : pink")
                mode = result ()

                if mode == "win" :
                    message = QMessageBox ( text = "🎉🎉 X WINNER 🎉🎉")
                    message.show ()
                    score_x += 1
                    next_round ()
                
                else :
                    window.turn.setText ("                      O Turn")
                    player = 2
            
            if player == 2 :
                while True :
                    row = random.randint ( 0 , 2 )
                    column = random.randint ( 0 , 2 )
                    if buttons[row][column].text() == "" :
                        buttons[row][column].setText ("O")
                        buttons[row][column].setStyleSheet("color : blue ; background-color : lightblue")
                        mode = result ()

                        if mode == "win" :
                            message = QMessageBox ( text = "🎉🎉 O WINNER 🎉🎉")
                            message.show ()
                            score_o += 1
                            player = 1
                            window.turn.setText ("                      X Turn")
                            next_round ()
                        
                        else :
                            window.turn.setText ("                      X Turn")
                            player = 1
                            break

    if mode == "tie" :
        message = QMessageBox ( text = "🎉🎉 XO DRAW 🎉🎉")
        message.show ()
        score_tie += 1
        next_round ()

    score_bord ()
    
def result () :
    t = 0
    for i in range ( 3 ) :
        if buttons[i][0].text() == buttons[i][1].text() == buttons[i][2].text() == "X" or buttons[i][0].text() == buttons[i][1].text() == buttons[i][2].text() == "O" :
            return ("win")

        elif buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text() == "X" or buttons[0][i].text() == buttons[1][i].text() == buttons[2][i].text() == "O" :
            return ("win")
        
        elif buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() == "X" or buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() == "O" :
            return ("win")

        elif buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() == "X" or buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() == "O" :
            return ("win")

        for j in range ( 3 ) :
            if buttons[i][j].text() != "" :
                t += 1
    
    if t == 9 :
        return ("tie")


def score_bord () :
    global score_x
    global score_tie
    global score_o
    x_text = f"           X : {score_x}"
    tie_text = f"         Tie : {score_tie}"
    o_text = f"           O : {score_o}"
    window.Xscore.setText ( x_text )
    window.Tiescore.setText ( tie_text )
    window.Oscore.setText ( o_text )

def restart () :
    global score_x
    global score_tie
    global score_o

    for i in range ( 3 ) :
        for j in range ( 3 ) :
            buttons[i][j].setText ("")
            buttons[i][j].setStyleSheet ("background-color : rgb(170,255,127)")
    
    score_x = 0
    score_tie = 0
    score_o = 0
    score_bord ()

def next_round () :
    for i in range ( 3 ) :
        for j in range ( 3 ) :
            buttons[i][j].setText ("")
            buttons[i][j].setStyleSheet ("background-color : rgb(170,255,127)")

def about () :
    global message
    message = QMessageBox ( text = "Hi, Welcome to my Tic-Tac-Toe game play. You can play this game with a fried or you can play alone with \
computer. In each round the winner is the first player to get three of the same symbols in a row. You can see the number of rounds in wich \
you win , draw or lose in score bord. You can start the game from the begining by press on the restart button. You cant put your mark in a \
place wich has been chosen before. So don't try to cheet 😈 . I hope you enjoy my game. Have FUN 😉😁 ")
    message.show ()

app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("tic-tac-toe/tic-tac-toe.ui")
window.show ()

player = 1
score_x = 0
score_tie = 0
score_o = 0
state = "player"
window.turn.setText ("                     X Turn")

buttons = [[ window.topLeft , window.top , window.topRight ] ,
           [ window.left , window.mid , window.right ] ,
           [ window.bottomLeft , window.bottom , window.bottomRight ]]

for i in range ( 3 ) :
    for j in range ( 3 ) :
        buttons[i][j].clicked.connect ( partial ( play , i , j ))
        
window.restart.clicked.connect ( restart )
window.about.clicked.connect ( about )
window.player.setChecked ( True )
window.computer.clicked.connect ( partial ( statement , "computer" ))
window.player.clicked.connect ( partial ( statement , "player" ))
score_bord ()
app.exec ()