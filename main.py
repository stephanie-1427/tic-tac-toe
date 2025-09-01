from tkinter import *
from random import choice
from assests import *


def next_turn(row : int, column : int, player : str):
    pass

def check_win():
    # a win
    pass

def empty_spaces():
    # recognize a tie
    pass

def new_game():
    pass

def reset_button():
    reset_button = Button(text="Restart", font=('Verdana', 15), command=new_game)
    reset_button.pack(side="top")

def create_board(window : Tk):
    frame = Frame(window)
    frame.pack()
    for row in range(3):
        for col in range(3):
            board[row][col] = Button(frame, text="", font=('Verdana', 40), width=5, height=2,
                                     command=lambda row=row, col=col : next_turn(row, col))
            board[row][col].grid(row=row, column=col)


def main(window : Tk):
    player = choice(players)
    label = Label(text=f"{player} turn", font=('Verdana', 30))
    label.pack(side="top")
    reset_button()
    create_board(window)


if __name__ == "__main__":
    window = Tk()
    window.title("TicTacToe")
    main(window)
    window.mainloop()
