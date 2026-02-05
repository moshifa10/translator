from tkinter import *
import pandas as pd
import pprint
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
# I will creator A project using tkinter where I use pandas and it prompt and you have a chance to answer


# ------------------------- Pandas ------------------------------
data = pd.read_csv(filepath_or_buffer="./data/afrikaans.csv")

words = data.to_dict(orient="records")
current_card = {}
# ----------------- Pandas ----------------------
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(words)
    canvas.itemconfig(word1, text="Afrikaans", fill="black")
    canvas.itemconfig(word, text=current_card["AFRIKAANS"], fill="black")
    canvas.itemconfig(canvas_image, image=photo_front)
    timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(word1, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["ENGLISH"],fill="white")
    canvas.itemconfig(canvas_image, image=photo_back)
    
def is_known():
    words.remove(current_card)
    print(len(words))
    data = pd.DataFrame(pd)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

    # canvas.create_image(300,150,photo_back)
# -----------------------  UI -------------------------------

window = Tk()
window.title("Words learning")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


timer = window.after(3000, func=flip_card)


# ------------------------ front Image --------------------------
canvas = Canvas(width=600, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_back = PhotoImage(file="./images/card_back.png")
photo_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(300,150,image=photo_front)
word1 = canvas.create_text(300,50, text="",font=(FONT_NAME, 30, "italic"))
word = canvas.create_text(300,150, text="",font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=4, pady=25,)


# --------------------------- Input --------------------------------
user_entry = Entry(width=25, font=(FONT_NAME, 14, "normal"),)
user_entry.focus()
user_entry.insert(0, "Type answer.")
user_entry.grid(column=2, row=1)


# ---------------------- X image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)


# ---------------------- correct image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right.grid(column=3, row=1)


next_card()

window.mainloop()