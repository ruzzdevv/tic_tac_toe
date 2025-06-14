import tkinter as tk
from tkinter import messagebox
from src.game_logic.game_logic import check_winner, is_draw

class TicTacToeUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.window, text="", font=("Arial", 36),
                    width=5, height=2,
                    command=lambda row=r, col=c: self.handle_click(row, col)
                )
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def handle_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if check_winner(self.board, self.current_player):
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.current_player} ganó!")
                self.reset_game()
            elif is_draw(self.board):
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="")
        self.current_player = "X"
