from tkinter import *
from random import choice
from assests import *


def next_turn():
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
    reset_button = Button(text="Restart", font=('Verdana', 20), command=new_game)
    reset_button.pack(side="top")


def main():
    player = choice(players)
    label = Label(text=f"{player} turn", font=('Verdana', 40))
    label.pack(side="top")
    reset_button()


if __name__ == "__main__":
    window = Tk()
    window.title("TicTacToe")
    window.geometry("480x720")
    main()
    window.mainloop()
