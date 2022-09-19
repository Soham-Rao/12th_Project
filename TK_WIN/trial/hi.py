#https://www.youtube.com/watch?v=6VbzpWL49Q4

import os
from PIL import Image, ImageTk
import tkinter 
from tkinter import PhotoImage, ttk, messagebox
import customtkinter as tk

class Main_window:
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

        bgmg = Image.open(os.path.join("imgs","bg1.jpg"))
        bgmg.save(os.path.join("imgs","bg1.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(Window, image = bg_img)
        background.place(x = 0, y = 0)

        butmg = Image.open(os.path.join("imgs","button.jpg"))
        butmg.save(os.path.join("imgs","button.png"))
        img = butmg.resize((350, 70), resample = 0)
        button_img = ImageTk.PhotoImage(butmg)       

        def printhello():
            print("Hello")
        Games = tk.CTkButton(master = Window, text = "Games", text_font = ("Times New Roman", 30), fg_color = "#b55bc7", hover_color = "#9532a8"  ,command = printhello)
        Games.place(x = 10, y = 370, width = 250, height = 70)
        
        
        

        
        
        Window.mainloop()





WINDOW = Main_window()
