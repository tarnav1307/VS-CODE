import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.x_wins = 0
        self.o_wins = 0
        self.reset_count = 0

        self.create_widgets()

    def create_widgets(self):
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 16), command=self.reset_board, bg="black", fg="white")
        reset_button.pack(side=tk.TOP, pady=5)

        self.win_label = tk.Label(self.root, text="X Wins: 0 | O Wins: 0", font=("Arial", 14), bg="black", fg="white")
        self.win_label.pack(side=tk.TOP, pady=5)

        self.reset_label = tk.Label(self.root, text="Reset Count: 0", font=("Arial", 14), bg="black", fg="white")
        self.reset_label.pack(side=tk.TOP, pady=5)

        frame = tk.Frame(self.root, bg="black")
        frame.pack(expand=True)

        for i in range(3):
            for j in range(3):
                button = tk.Button(frame, text="", font=("Arial", 36), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col), bg="black", fg="white")
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.update_win_counter()
                self.disable_buttons()
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = "disabled"

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"

        self.reset_count += 1
        self.reset_label.config(text=f"Reset Count: {self.reset_count}")

        self.x_wins = 0
        self.o_wins = 0
        self.update_win_label()

    def update_win_counter(self):
        if self.current_player == "X":
            self.x_wins += 1
        else:
            self.o_wins += 1
        self.update_win_label()

    def update_win_label(self):
        self.win_label.config(text=f"X Wins: {self.x_wins} | O Wins: {self.o_wins}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
