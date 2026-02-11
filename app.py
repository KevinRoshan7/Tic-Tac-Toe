import tkinter as tk
from tkinter import messagebox
import logic

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

buttons = []

def on_click(i):
    if not logic.make_move(i):
        return

    buttons[i].config(text=logic.current_player)

    result = logic.check_winner()
    if result:
        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {result} wins!")
        reset()
        return

    logic.switch_player()
    status.config(text=f"Player {logic.current_player}'s turn")

def reset():
    logic.reset_game()
    for b in buttons:
        b.config(text="")
    status.config(text="Player X's turn")

status = tk.Label(root, text="Player X's turn", font=("Arial", 12))
status.grid(row=0, column=0, columnspan=3, pady=5)

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=1 + i // 3, column=i % 3)
    buttons.append(btn)

tk.Button(root, text="Restart", command=reset).grid(
    row=4, column=0, columnspan=3, pady=5
)

root.mainloop()
