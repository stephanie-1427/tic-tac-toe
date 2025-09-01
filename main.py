from tkinter import *
import assests


def next_turn(row : int, column : int, label : Label):
    if assests.board[row][column]['text'] == "" and check_win() is False:

        assests.board[row][column].config(text=assests.player)
        status = check_win()

        if status == "Tie!":
            label.config(text='Tie!')
        elif status:
            label.config(text=f'{assests.player} wins!')
        else:
            assests.player = assests.players[1] if assests.player == assests.players[0] else assests.players[0]
            label.config(text=f'{assests.player} turn')


def check_win():
    # a win
    return False

def empty_spaces():
    # recognize a tie
    pass

def new_game():
    pass

def reset_button():
    reset_button = Button(text="Restart", font=('Verdana', 15), command=new_game)
    reset_button.pack(side="top")

def create_board(window : Tk, label : Label):
    frame = Frame(window)
    frame.pack()
    for row in range(3):
        for col in range(3):
            assests.board[row][col] = Button(frame, text="", font=('Verdana', 40), width=5, height=2,
                                     command=lambda row=row, col=col : next_turn(row, col, label))
            assests.board[row][col].grid(row=row, column=col)


def main(window : Tk):
    assests.pick_player()
    label = Label(text=f"{assests.player} turn", font=('Verdana', 30))
    label.pack(side="top")
    reset_button()
    create_board(window, label)


if __name__ == "__main__":
    window = Tk()
    window.title("TicTacToe")
    main(window)
    window.mainloop()
