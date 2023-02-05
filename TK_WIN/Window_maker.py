#importing
import os
import tkinter 
from PIL import Image, ImageTk
from tkinter import PhotoImage, ttk, messagebox
import customtkinter as tk

#class windowmaker - class to help create windows
class Window_maker():
    #constructor function
    def __init__(self):
        #private variables
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")
        self.user = "Guest"        
    
    #function that makes the window
    def Make_Win(self, Window, window_title, bgimg, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):
        
        Window.title(window_title)
        
        window_height = 600
        window_width = 900

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)


        self.buttonmaker(Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4)

        Window.mainloop()
    
    #function that makes the buttons
    def buttonmaker(self, Window, text1, text2, text3, text4, fgcolor, hcolor, command1, command2, command3, command4):
        Button1 = tk.CTkButton(master = Window, text = text1, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command1)
        Button1.place(x = 10, y = 370, width = 250, height = 70)

        Button2 = tk.CTkButton(master = Window, text = text2, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command2)
        Button2.place(x = 310, y = 370, width = 250, height = 70)

        Button3 = tk.CTkButton(master = Window, text = text3, text_font = ("Times New Roman", 30), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command3)
        Button3.place(x = 610, y = 370, width = 250, height = 70)

        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((50,50), resample = 0)
        button_img = ImageTk.PhotoImage(img)       

        Button4 = tk.CTkButton(master = Window, text = text4, text_color = "black", text_font = ("Times New Roman", 14), fg_color = fgcolor, hover_color = hcolor, bg_color = fgcolor ,command = command4, image = button_img, compound = "left")
        Button4.place(x = 10, y = 10, width = 120, height = 50)
        
        Label = tk.CTkLabel(master = Window, text = "Current user : "+ self.user, text_font = ("Times New Roman", 20), fg_color = fgcolor, bg_color = fgcolor)
        #Label.place(x = 600, y = 10, width = 270, height = 30)