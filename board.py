import tkinter as tk

ROWS = 6
COLS = 7
CELL_SIZE = 80
RADIUS = CELL_SIZE // 2 - 5

class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4")
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='blue')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 1  # Player 1 = red, Player 2 = yellow

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x0 = c * CELL_SIZE + 5
                y0 = r * CELL_SIZE + 5
                x1 = x0 + 2*RADIUS
                y1 = y0 + 2*RADIUS

                if self.board[r][c] == 1:
                    color = "red"
                elif self.board[r][c] == 2:
                    color = "yellow"
                else:
                    color = "white"

                self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black")

    def on_click(self, event):
        col = event.x // CELL_SIZE
        if 0 <= col < COLS:
            for row in reversed(range(ROWS)):
                if self.board[row][col] == 0:
                    self.board[row][col] = self.current_player
                    self.current_player = 2 if self.current_player == 1 else 1
                    self.draw_board()
                    break

if __name__ == "__main__":
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()
