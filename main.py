from tkinter import *
import assests


def next_turn(row : int, column : int, label : Label) -> None:
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


def check_win() -> bool | str:
    # Horizontal
    for row in range(3):
        if assests.board[row][0]['text'] == assests.board[row][1]['text'] == assests.board[row][2]['text'] != "":
            return True

    # Vertical
    for col in range(3):
        if assests.board[0][col]['text'] == assests.board[1][col]['text'] == assests.board[2][col]['text'] != "":
            return True

    # Diagonal
    if assests.board[0][0]['text'] == assests.board[1][1]['text'] == assests.board[2][2]['text'] != "":
        return True
    elif assests.board[0][2]['text'] == assests.board[1][1]['text'] == assests.board[2][0]['text'] != "":
        return True
    # Tie
    elif empty_spaces() is False:
        return 'Tie!'

    return False


def empty_spaces() -> bool:
    spaces = 9

    for row in range(3):
        for col in range(3):
            if assests.board[row][col]['text'] != "":
                spaces -= 1

    # Condition for if spaces is 0
    if not spaces:
        return False
    return True


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
