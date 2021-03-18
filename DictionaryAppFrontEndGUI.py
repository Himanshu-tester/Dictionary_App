from tkinter import *
import tkinter.messagebox

import DictionaryApp_Backend
from DictionaryApp_Backend import know_meaning


def word_search():
    list1.delete(0, END)
    for row in DictionaryApp_Backend.know_meaning(word.get()):
        list1.insert(END, row)


window = Tk()
window.wm_title("Dictionary - Know Your Word")
window.geometry('50x10')


label1 = Label(window, text="Enter your Word")
label1.pack()

word = StringVar()
e1 = Entry(window, textvariable=word)
e1.pack()

button = Button(window, text="Enlighten Me!", width=12, command=word_search, bg="lightgreen")
button.pack()

list1 = Listbox(window, width=70, height=5, bd=5, relief=RIDGE, font="Helvetica")

list1.pack()
label1.config(width=0)
window.winfo_toplevel().wm_geometry("")
# my_scrollbar.config(command=list1.xview)
# my_scrollbar.pack(side=RIGHT, fill=X)
# my_frame.pack()
# list1.pack(pady=10)
window.mainloop()
