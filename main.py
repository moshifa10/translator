from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
# I will creator A project using tkinter where I use pandas and it prompt and you have a chance to answer



# -----------------------  UI -------------------------------

window = Tk()
window.title("Words learning")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


# ------------------------ front Image --------------------------
canvas = Canvas(width=600, height=300, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(300,150,image=photo_front)
text_front = canvas.create_text(300,50, text="Title",font=(FONT_NAME, 27, "normal"))
text_front = canvas.create_text(300,100, text="Word",font=(FONT_NAME, 27, "bold"))
canvas.grid(column=0, row=0, columnspan=4, pady=25,)



# ---------------------- X image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong.grid(column=0, row=1)


# ---------------------- correct image ------------------------------
# x = Canvas(height=100, width=100, bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="./images/right.png")
wrong = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0,)
wrong.grid(column=3, row=1)


window.mainloop()