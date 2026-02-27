import tkinter as tk
import random

word_list = ["APPLE", "GRAPE", "MELON", "PEACH", "BERRY"]

root = tk.Tk()
root.title("Wordle Clone")
root.geometry("950x950")
root["bg"]="#FADAF6"

header = tk.Label(root, text="Wordle Clone", font=("Arial", 20, "bold"),fg="#00060B", bg="#FADAF6")
header.pack(pady=10)

instructions_text = (
    "How to play: Guess the 5-letter word in 5 tries. "
    "If a tile turns green, the letter is in the word and in the correct position."
    "If a tile turns yellow, the letter is in the word but in the wrong position."
    "If a tile turns gray, the letter is not in the word."
)
instructions = tk.Label(root, text=instructions_text, font=("Arial", 12),fg="#00060B", bg="#FADAF6",wraplength=500, justify="center")
instructions.pack(pady=5)

grid_frame = tk.Frame(root, bg="#FADAF6")
grid_frame.pack(pady=20)

rows = 5
cols = 5
labels = [[None for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        lbl = tk.Label(grid_frame, text="", width=5, height=3, font=("Arial", 16), relief="solid", borderwidth=4, bg="#FBFDFF")
        lbl.grid(row=r, column=c, padx=6, pady=6)
        labels[r][c] = lbl


message_label = tk.Label(root, text="", font=("Arial", 14), bg="#FADAF6")
message_label.pack(pady=10)


current_row = 0
current_col = 0
secret_word = random.choice(word_list)


def key_pressed(event):
    global current_row, current_col
    if current_row >= rows:
        return

    if event.keysym == "BackSpace":
        if current_col > 0:
            current_col -= 1
            labels[current_row][current_col].config(text="")
    elif event.keysym == "Return":
        if current_col == cols:
            guess = ''.join(labels[current_row][c].cget("text") for c in range(cols))
            
            for i, char in enumerate(guess):
                if char == secret_word[i]:
                    labels[current_row][i].config(bg="green", fg="white")
                elif char in secret_word:
                    labels[current_row][i].config(bg="yellow", fg="black")
                else:
                    labels[current_row][i].config(bg="gray", fg="white")
            if guess == secret_word:
                message_label.config(text=f"Congratulations! You guessed the correct word! It was {secret_word}!", fg="green")
            else:
                current_row += 1
                current_col = 0
                if current_row == rows:
                    message_label.config(text=f"Game Over! The word was {secret_word}", fg="red")
    elif event.char.isalpha() and len(event.char) == 1:
        if current_col < cols:
            labels[current_row][current_col].config(text=event.char.upper())
            current_col += 1

root.bind("<Key>", key_pressed)


root.mainloop()