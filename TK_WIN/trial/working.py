#https://www.youtube.com/watch?v=6VbzpWL49Q4

import os
from PIL import Image, ImageTk
import tkinter 
from tkinter import PhotoImage, ttk, messagebox
import customtkinter as tk

class Windows:
    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")
        self.First_Window()

    def First_Window(self):        
        Window = tk.CTk()
        Window.title("Arcade")
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","1stbg.jpg"))
        bgmg.save(os.path.join("imgs","1stbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        butmg = Image.open(os.path.join("imgs","button.jpg"))
        butmg.save(os.path.join("imgs","button.png"))
        img = butmg.resize((350, 70), resample = 0)
        button_img = ImageTk.PhotoImage(butmg)       

        def GamesWin():
            self.Second_Window()
            Window.destroy()

        Games = tk.CTkButton(master = Window, text = "Games", text_font = ("Times New Roman", 30), fg_color = "#9532a8", hover_color = "#b55bc7", bg_color = "#9532a8" ,command = GamesWin)
        Games.place(x = 10, y = 370, width = 250, height = 70)
        
        
        
        
        Window.mainloop()


    def Second_Window(self):
        Gamewin = tk.CTkToplevel()
        Gamewin.title("Games")
        
        window_height = 600
        window_width = 900

        screen_width = Gamewin.winfo_screenwidth()
        screen_height = Gamewin.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Gamewin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Gamewin.resizable(False, False)


        bgmg = Image.open(os.path.join("imgs","2ndbg.jpg"))
        bgmg.save(os.path.join("imgs","2ndbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Gamewin, image = bg_img)
        background.place(x = 0, y = 0)

        def open_slither_window():
            self.Third_Window()
            Gamewin.destroy()

        slither_button = tk.CTkButton(master = Gamewin, text = "Slither.io", text_font = ("Times New Roman", 30), fg_color = "#9532a8", hover_color = "#b55bc7", bg_color = "#9532a8" ,command = open_slither_window)
        slither_button.place(x = 10, y = 370)



        Gamewin.mainloop()

    def Third_Window(Self):
        Slither_Window = tk.CTkToplevel()
        Slither_Window.title("Slither.io")
        
        window_height = 600
        window_width = 900

        screen_width = Slither_Window.winfo_screenwidth()
        screen_height = Slither_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Slither_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Slither_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","3rdbg.png"))
        bgmg.save(os.path.join("imgs","3rdbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Slither_Window, image = bg_img)
        background.place(x = 0, y = 0)

        def open_slither():
            os.system(r'python slitherio\Game\main_slither.py')
            Slither_Window.destroy()

        slither_button = tk.CTkButton(master = Slither_Window, text = "Play", text_font = ("Times New Roman", 30), fg_color = "#363d36", hover_color = "#626962", bg_color = "#363d36" ,command = open_slither)
        slither_button.place(x = 10, y = 370)


        Slither_Window.mainloop()

WINDOW = Windows()
