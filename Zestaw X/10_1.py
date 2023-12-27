from tkinter import *
import random

window = Tk()

window.configure(bg='white')

window.geometry("360x450")

window.title("Rolling The Dices Game")
def roll_dices():
    faces = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    choice=str(random.choice(faces))
    label.configure(
        text=choice)
    label.pack()
Font_tuple = ("Arial", 300)
# Adding button to roll the dices
roll_button = Button(window, text="Rzut!", font=("Arial",20),
 bg="yellow",command=roll_dices)
# Setting the position of the button
roll_button.pack(padx=10, pady=15)

label = Label(window, font=Font_tuple,
              bg="white", fg="black")

window.mainloop()