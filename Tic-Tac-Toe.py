import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def on_click(row, col):
    global player
    if buttons[row][col]['text'] == "" and not check_winner():
        buttons[row][col]['text'] = player
        board[row][col] = player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            player = 'O' if player == 'X' else 'X'

def reset_board():
    global board, player
    player = 'X'
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            buttons[i][j]['text'] = ""

root = tk.Tk()
root.title("Tic-Tac-Toe")

player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Arial', 20), height=2, width=5,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
