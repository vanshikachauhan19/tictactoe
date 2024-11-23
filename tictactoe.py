import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.create_board()

    def create_board(self):
        """Creates the game board using tkinter.Canvas."""
        self.canvas = tk.Canvas(self.window, width=300, height=300)
        self.canvas.pack()

        # Draw grid lines
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, width=2)
            self.canvas.create_line(i * 100, 0, i * 100, 300, width=2)

        # Bind clicks to the canvas
        self.canvas.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        """Handles the click event and places a marker."""
        x, y = event.x, event.y
        row, col = y // 100, x // 100
        index = row * 3 + col

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.draw_marker(row, col, self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_marker(self, row, col, player):
        """Draws 'X' or 'O' on the canvas."""
        x1, y1 = col * 100 + 20, row * 100 + 20
        x2, y2 = (col + 1) * 100 - 20, (row + 1) * 100 - 20

        if player == "X":
            self.canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")
            self.canvas.create_line(x1, y2, x2, y1, width=2, fill="blue")
        else:
            self.canvas.create_oval(x1, y1, x2, y2, width=2, outline="red")

    def check_winner(self):
        """Checks if the current player has won."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]

        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def reset_board(self):
        """Resets the board for a new game."""
        self.board = [""] * 9
        self.canvas.delete("all")
        self.create_board()
        self.current_player = "X"

    def run(self):
        """Runs the tkinter main loop."""
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
