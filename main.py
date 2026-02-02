from tkinter import *
import pandas as pd
import pprint
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
# I will creator A project using tkinter where I use pandas and it prompt and you have a chance to answer


# ------------------------- Pandas ------------------------------
data = pd.read_csv(filepath_or_buffer="./data/afrikaans.csv")

words = {row.AFRIKAANS:row.ENGLISH for (index, row) in data.iterrows()}



# -----------------------  UI -------------------------------

window = Tk()
window.title("Words learning")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)



# ----------------- Pandas ----------------------
def pick():
    picker = random.choice(list(words.keys()))
    # canvas.itemconfig(title,"Afrikaans")
    canvas.itemconfig(word, text=picker)



def click_wrong():
    photo_back = PhotoImage(file="./images/card_back.png")
    canvas.config()
    pick()

def click_right():
    pick()
# ------------------------ front Image --------------------------
canvas = Canvas(width=600, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(300,150,image=photo_front)
title = canvas.create_text(300,50, text="Afrikaans",font=(FONT_NAME, 30, "italic"))
word = canvas.create_text(300,150, text="word",font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=4, pady=25,)


# --------------------------- Input --------------------------------
user_entry = Entry(width=25, font=(FONT_NAME, 14, "normal"),)
user_entry.focus()
user_entry.insert(0, "Type answer.")
user_entry.grid(column=2, row=1)


# ---------------------- X image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=click_wrong)
wrong.grid(column=0, row=1)


# ---------------------- correct image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=click_right)
right.grid(column=3, row=1)




window.mainloop()