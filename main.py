from tkinter import *
from random import choice
import pandas as pd
#-------------data stuff--------------#
df = pd.read_csv("data/french_words.csv")
data = df.to_dict(orient='records')
current_card = {}


def choose_words():
    global current_card,timer
    window.after_cancel(timer)
    current_card = choice(data)
    canvas.itemconfig(front_side,image=card_front)
    canvas.itemconfig(card_title,text = "French",fill = "black")
    canvas.itemconfig(ques,text = current_card['French'],fill = "black")
    timer = window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(front_side,image=card_back)
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(ques,text=current_card["English"],fill="white")

def is_known():
    data.remove(current_card)
    print(len(data))
    choose_words()

#-------------GUI--------------#ss
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash card project")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = window.after(3000,func=flip_card)
canvas = Canvas(width=800,height=525)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
front_side = canvas.create_image(400,263,image=card_front)

card_title = canvas.create_text(400,150,font=("Ariel",40,"italic"))
ques = canvas.create_text(400,263,font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross = PhotoImage(file="images/wrong.png")
unknown_buton = Button(image=cross,highlightthickness=0,command=choose_words)
unknown_buton.grid(row=1,column=0)

check = PhotoImage(file="images/right.png")
right_button = Button(image=check,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)
choose_words()

window.mainloop()