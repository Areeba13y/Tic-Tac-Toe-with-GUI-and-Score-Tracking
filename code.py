import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe with Scores")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Initialize game variables
        self.board = ['' for _ in range(9)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}

        # Create GUI components
        self.create_gui()

    def create_gui(self):
        # Scoreboard
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 16))
        self.score_label.pack(pady=10)

        # Game board
        self.buttons = []
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        for i in range(9):
            button = tk.Button(self.board_frame, text='', font=("Arial", 24), width=5, height=2, 
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 14), command=self.reset_game)
        self.reset_button.pack(pady=20)

        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 14), command=self.root.quit)
        self.quit_button.pack(pady=10)

    def get_score_text(self):
        return f"Player X: {self.scores['X']}   |   Player O: {self.scores['O']}"

    def make_move(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state='disabled')

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.scores[self.current_player] += 1
                self.update_score()
                self.reset_board()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def reset_board(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.config(text='', state='normal')
        self.current_player = "X"

    def reset_game(self):
        self.scores = {"X": 0, "O": 0}
        self.update_score()
        self.reset_board()

    def update_score(self):
        self.score_label.config(text=self.get_score_text())

    def run(self):
        self.root.mainloop()

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
