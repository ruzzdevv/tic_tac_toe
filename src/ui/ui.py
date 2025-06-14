import tkinter as tk
from tkinter import messagebox, Toplevel
from src.game_logic.game_logic import check_winner, is_draw

class TicTacToeUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Inicializar puntajes
        self.score_x = 0
        self.score_o = 0

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.current_player = None

        # Crear y posicionar las etiquetas de puntuación
        self.score_label_x = tk.Label(self.window, text=f"Player X: {self.score_x}", font=("Arial", 14))
        self.score_label_x.grid(row=3, column=0, columnspan=1, pady=10) # Colocadas debajo del tablero

        self.score_label_o = tk.Label(self.window, text=f"Player O: {self.score_o}", font=("Arial", 14))
        self.score_label_o.grid(row=3, column=2, columnspan=1, pady=10) # Colocadas debajo del tablero

        self.create_board()
        self.show_player_selection_window()

        # Actualizar la visualización inicial de los puntajes
        self.update_score_display()

        self.window.mainloop()

    def show_player_selection_window(self):
        selection_window = Toplevel(self.window)
        selection_window.title("Select initial player")
        selection_window.grab_set()

        label = tk.Label(selection_window, text="Who starts?", font=("Arial", 16))
        label.pack(pady=10)

        def set_player(player):
            self.current_player = player
            selection_window.destroy()

        button_frame = tk.Frame(selection_window)
        button_frame.pack(pady=10)

        x_button = tk.Button(button_frame, text="X", font=("Arial", 18), width=5, command=lambda: set_player("X"))
        o_button = tk.Button(button_frame, text="O", font=("Arial", 18), width=5, command=lambda: set_player("O"))

        x_button.grid(row=0, column=0, padx=10)
        o_button.grid(row=0, column=1, padx=10)

        selection_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.window.wait_window(selection_window)

    def create_board(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    self.window, text="", font=("Arial", 36),
                    width=5, height=2,
                    command=lambda row=r, col=c: self.handle_click(row, col)
                )
                # Posicionar los botones del tablero en las filas 0, 1, 2
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def handle_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if check_winner(self.board, self.current_player):
                # Incrementar puntuación del jugador que ganó
                if self.current_player == "X":
                    self.score_x += 1
                else:
                    self.score_o += 1

                # Actualizar la visualización de los puntajes después de ganar
                self.update_score_display()

                messagebox.showinfo("End game", f"¡Player {self.current_player} won!")
                self.reset_game()
            elif is_draw(self.board):
                messagebox.showinfo("End game", "¡Draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="")
        self.show_player_selection_window()
        # Los puntajes no se resetean aquí, solo el tablero.
        # Si quisieras resetear puntajes al reiniciar, lo harías aquí.
        # self.update_score_display() # Si resetearas los puntajes, deberías actualizar la visualización aquí también.


    def update_score_display(self):
        """Actualiza el texto de las etiquetas de puntuación."""
        self.score_label_x.config(text=f"Player X: {self.score_x}")
        self.score_label_o.config(text=f"Player O: {self.score_o}")

