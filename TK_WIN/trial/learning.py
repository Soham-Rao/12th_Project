#https://www.youtube.com/watch?v=itRLRfuL_PQ
#https://www.youtube.com/watch?v=g81l3y2i-so
#https://www.youtube.com/watch?v=Xt6SqWuMSA8














#importing
import tkinter as tk
from tkinter import BooleanVar, ttk, messagebox
import os



#creating window, naming and size
window = tk.Tk()
window.title("Project")
window.geometry("650x500")

#frame
bottom = tk.Frame(window).pack(side = "bottom")


#functions for clicking
def clickedb():
    a.configure(text = "successfully clicked")

def clickedc():
    a.configure(text = "hi")

def clickedd():
    a.configure(text = "u entered:" + e.get())

def clickedi():
    messagebox.showinfo("showinfo", "Information")
    messagebox.showwarning("showwarning", "Warning")
    messagebox.showerror("showerror", "Error")
    messagebox.askquestion("askquestion", "Are you sure?")
    messagebox.askokcancel("askokcancel", "Want to continue?")
    messagebox.askyesno("askyesno", "Find the value?")
    messagebox.askretrycancel("askretrycancel", "Try again?")


#text
a = tk.Label(window, text = "hi", fg = "red", font = ("times new roman", 20))
a.place(x = 0, y = 0)

#button
b = tk.Button(window, text = "click", fg = "blue", font = ("Arial", 10), command = clickedb)
b.place(x = 0, y = 100)

#button
c = tk.Button(window, text = "click me too", fg = "green", font = ("Arial", 10), command = clickedc)
c.place(x = 100, y = 100)

#button
d = tk.Button(window, text = "change", fg = "purple", font = ("Arial", 10), command = clickedd)
d.place(x = 200, y = 100)

#entry
e = tk.Entry(window, width = 10)
e.place(x = 0, y = 200)

#combobox
f = ttk.Combobox(window, width = 10)
f['values'] = (1, 2, 3, 4, 5)
f.current(0)
f.place(x = 0, y = 300)

#checkbutton
g = tk.Checkbutton(window, text = "choose", var = BooleanVar())
g.place(x = 100, y = 300)

#radiobutton
h1 = tk.Radiobutton(window, text = "coffee", value = 1)
h1.place(x = 200, y = 300)

h2 = tk.Radiobutton(window, text = "tea", value = 2)
h2.place(x = 300, y = 300)

#button
i = tk.Button(window, text = "msgbox", command = clickedi)
i.place(x = 100, y = 200)

#spinbox
j = tk.Spinbox(window, from_ = 0, to = 100, width = 10)
j.place(x = 400, y = 300)

#button with frames
k = tk.Button(bottom, text = "left corner")
k.pack(side = "bottom")



###########################################################

def sayhi(Z):
    tk.Button(window, text = 'hellllllllo', command = z).place(x = 100, y = 400)

def z():
    Z = tk.Button(window,text = "click me", fg = "blue", font = ("arial", 10))
    Z.place(x = 200, y = 400)
    Z.bind("<Button-1>",sayhi)


Z = tk.Button(window,text = "click me", fg = "blue", font = ("arial", 10))
Z.place(x = 0, y = 400)
Z.bind("<Button-3>",sayhi)



#L = tk.PhotoImage(file = "D:\\PC files\\Solo Leveling ScreenShots\\Solo Leveling\\blue.png")
#label = tk.Label(window, image = L).pack() 






def slitherio(S):
    os.system(r'python slitherio\Game\main_slither.py')

S = tk.Button(window, text = 'open game')
S.pack()
S.bind("<Button-1>",slitherio)




def newwin():
    winnew = tk.Tk()
    winnew.geometry('100x200')
    winnew.title("new window")
    window.destroy()
    winnew.mainloop()
BUTTON = tk.Button(window, text = 'new window', fg = 'red', command = newwin).pack()



#mainloop
window.mainloop()