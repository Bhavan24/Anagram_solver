from tkinter import *
import tkinter as tk
from itertools import permutations

root = Tk()
root.title("Anagram Solver")
root.geometry("462x258")
root.resizable(width=False, height=False)
user_input = tk.StringVar(root)

txt_anagram = tk.Entry(root)
txt_anagram["borderwidth"] = "1px"
txt_anagram["fg"] = "#333333"
txt_anagram["justify"] = "center"
txt_anagram["textvariable"] = user_input
txt_anagram.place(x=230,y=20,width=212,height=30)

lblText = tk.Label(root)
lblText["fg"] = "#333333"
lblText["justify"] = "center"
lblText["text"] = "Enter your anagram: "
lblText["relief"] = "flat"
lblText.place(x=10,y=10,width=226,height=44)


def press():    
    listx = []
    x = user_input.get()
    spel = [''.join(data) for data in permutations(x)]
    for i in spel:
        with open("WordList.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()
                if i == stripped_line:
                    listx.append(stripped_line)
    if len(listx) == 0:
        lbl_anagram.config(text = "No anagram found")
    else:
        lbl_anagram.config(text = listx)


btn_anagram = tk.Button(root)
btn_anagram["bg"] = "#efefef"
btn_anagram["fg"] = "#000000"
btn_anagram["justify"] = "center"
btn_anagram["text"] = "Generate"
btn_anagram["relief"] = "groove"
btn_anagram.place(x=190,y=220,width=70,height=25)
btn_anagram["command"] = press

lbl_anagram = tk.Label(root)
lbl_anagram["fg"] = "#333333"
lbl_anagram["justify"] = "left"
lbl_anagram["text"] = "Your answers will show up here!"
lbl_anagram["relief"] = "ridge"
lbl_anagram.place(x=30,y=60,width=407,height=152)


root.mainloop()