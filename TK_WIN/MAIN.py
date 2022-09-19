#https://www.youtube.com/watch?v=6VbzpWL49Q4

import os
import csv
import tkinter 
import customtkinter as tk
from Window_maker import Window_maker
from PIL import Image, ImageTk
from tkinter import PhotoImage, ttk, messagebox
from Login_Window import Login_Window


class Windows:
    def __init__(self):
        self.First_Window()

    def First_Window(self):        
        Window = tk.CTk()
        
        FirstWin = Window_maker()
        
        def open_win2():
            self.Second_Window()
            try:
                Window.destroy()
            except tkinter.TclError:
                pass

        def leave():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass

        def login():
            self.login()

        def close():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass


        FirstWin.Make_Win(Window = Window, window_title = "Arcade", bgimg = "1stbg", text1 = "Login/Logout", text2 = "Games", text3 = "Exit", text4 = "close", fgcolor = "#9532a8", hcolor = "#b55bc7", command1 = login, command2 = open_win2, command3 = leave, command4 = close)
        


    def Second_Window(self):
        Gamewin = tk.CTkToplevel()

        SecondWin = Window_maker()
        
        def open_slither_window():
            self.Third_Window()
            try:
                Gamewin.destroy()
            except tkinter.TclError:
                pass

        def open_space_window():
            self.Fourth_Window()
            try:
                Gamewin.destroy()
            except tkinter.TclError:
                pass

        def close():
            try:
                Gamewin.destroy()
            except tkinter.TclError:
                pass


        SecondWin.Make_Win(Window = Gamewin, window_title = "Games", bgimg = "2ndbg", text1 = "Slither.io", text2 = "Space Battles", text3 = "Game3", text4 = "back", fgcolor = "#9532a8", hcolor = "#b55bc7", command1 = open_slither_window, command2 = open_space_window, command3 = None, command4 = close)

    def Third_Window(Self):
        Slither_Window = tk.CTkToplevel()

        ThirdWin = Window_maker()
        
        def open_slither_game():
            os.system(r'python slitherio\Game\main_slither.py')
            try:
                Slither_Window.destroy()
            except tkinter.TclError:
                pass
            
        def open_slither_rules():
            Rule_window = tk.CTkToplevel()
            window_height = 600
            window_width = 1200
            Rule_window.title("Rules of slither.io")

            screen_width = Rule_window.winfo_screenwidth()
            screen_height = Rule_window.winfo_screenheight()
        
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int(((screen_height/2) - (window_height/2))-50)

            Rule_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            Rule_window.resizable(False, False)

            f = open('Rules\slitherio_rules.txt','r')
            data = f.read()
            
            rules = tk.CTkLabel(master = Rule_window, text = data, text_font = ("calibri", 17), bg_color = "#1e1e1e")
            rules.place(x = 0, y = 0, width = 1200, height = 600)

            # def closewin():
            #     try:
            #         Rule_Window.destroy()
            #     except tkinter.TclError:
            #         pass
                

            # close_button = tk.CTkButton(master = Rule_window, text = "Ok", text_font = ("calibri", 10), bg_color = "#1e1e1e", fg_color = "#1e1e1e", hover_color = "#444444", command = closewin)
            # close_button.place(x = 550, y = 550, width = 100, height = 40)

            Rule_window.mainloop()
            try:
                Slither_Window.destroy()
            except tkinter.TclError:
                pass
            
        def close():
            try:
                Slither_Window.destroy()
            except tkinter.TclError:
                pass


        def open_slither_highscores():
            Score_window = tk.CTkToplevel()
            window_height = 600
            window_width = 1200
            Score_window.title("Highscores of slither.io")

            screen_width = Score_window.winfo_screenwidth()
            screen_height = Score_window.winfo_screenheight()
        
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int(((screen_height/2) - (window_height/2))-50)

            Score_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            Score_window.resizable(False, False)

            f = open(os.path.join("","slither_highscore.csv"),'r')
            csr = csv.reader(f)
            D = {}
            for i in csr:
                D[i[0]] = i[1] #dictionary (username: score)
            f.close()
            
            
            scores = tk.CTkLabel(master = Score_window, text = D, text_font = ("calibri", 17), bg_color = "#1e1e1e")
            scores.place(x = 0, y = 0, width = 1200, height = 600)

            Score_window.mainloop()
            try:
                Slither_Window.destroy()
            except tkinter.TclError:
                pass

        
        ThirdWin.Make_Win(Window = Slither_Window, window_title = "slither.io", bgimg = "3rdbg", text1 = "Play", text2 = "Rules", text3 = "Highscores", text4 = "back", fgcolor = "#363d36", hcolor = "#626962", command1 = open_slither_game, command2 = open_slither_rules, command3 = open_slither_highscores, command4 = close)


    def Fourth_Window(self):
        Space_Window = tk.CTkToplevel()

        FourthWin = Window_maker()

        def open_space_game():
            self.Tenth_Window()
            try:
                Space_Window.destroy()
            except tkinter.TclError:
                pass
            
        def open_space_rules():
            Rule_window = tk.CTkToplevel()
            window_height = 600
            window_width = 1200
            Rule_window.title("Rules of space battles")

            screen_width = Rule_window.winfo_screenwidth()
            screen_height = Rule_window.winfo_screenheight()
        
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int(((screen_height/2) - (window_height/2))-50)

            Rule_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            Rule_window.resizable(False, False)

            f = open('Rules\Space_battles_rules.txt','r')
            data = f.read()
            rules = tk.CTkLabel(master = Rule_window, text = data, text_font = ("calibri", 17), bg_color = "#1e1e1e")
            rules.place(x = 0, y = 0, width = 1200, height = 600)
            Rule_window.mainloop()
            try:
                Space_Window.destroy()
            except tkinter.TclError:
                pass            

        def close():
            try:
                Space_Window.destroy()
            except tkinter.TclError:
                pass

        def open_space_highscores():
            Score_window = tk.CTkToplevel()
            window_height = 600
            window_width = 1200
            Score_window.title("Highscores of slither.io")

            screen_width = Score_window.winfo_screenwidth()
            screen_height = Score_window.winfo_screenheight()
        
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int(((screen_height/2) - (window_height/2))-50)

            Score_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            Score_window.resizable(False, False)

            f = open(os.path.join("","space_highscore.csv"),'r')
            csr = csv.reader(f)
            D = {}
            for i in csr:
                D[i[0]] = i[1] #dictionary (username: score)
            f.close()
            
            
            scores = tk.CTkLabel(master = Score_window, text = D, text_font = ("calibri", 17), bg_color = "#1e1e1e")
            scores.place(x = 0, y = 0, width = 1200, height = 600)

            Score_window.mainloop()
            try:
                Space_Window.destroy()
            except tkinter.TclError:
                pass


        FourthWin.Make_Win(Window = Space_Window, window_title = "Space Battles", bgimg = "4thbg", text1 = "Play", text2 = "Rules", text3 = "Highscores", text4 = "back", fgcolor = "#011e3e", hcolor = "#36587d", command1 = open_space_game, command2 = open_space_rules, command3 = open_space_highscores, command4 = close)




    def Tenth_Window(self):
        Choose_Window = tk.CTkToplevel()
        Choose_Window.title("Choose a mode")
        
        window_height = 300
        window_width = 450

        screen_width = Choose_Window.winfo_screenwidth()
        screen_height = Choose_Window.winfo_screenheight()
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Choose_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Choose_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","4thbg.jpg"))
        bgmg.save(os.path.join("imgs","4thbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)       

        background = tk.CTkLabel(master = Choose_Window, image = bg_img)
        background.place(x = 0, y = 0)

        def open_multi():
            os.system(r'python Space_Battles\Space_Battles\main_old_multiplayer.py')
            try:
                Choose_Window.destroy()
            except tkinter.TclError:
                pass
            
        def open_single():
            os.system(r'python Space_Battles\Space_Battles\New\main_space.py')
            try:
                Choose_Window.destroy()
            except tkinter.TclError:
                pass
            
        Button1 = tk.CTkButton(master = Choose_Window, text = "Single-Player", text_font = ("Times New Roman", 20), fg_color = "#011e3e", hover_color = "#36587d", bg_color = "#011e3e" ,command = open_single)
        Button1.place(x = 15, y = 150, width = 180, height = 60)

        Button2 = tk.CTkButton(master = Choose_Window, text = "Multi-Player", text_font = ("Times New Roman", 20), fg_color = "#011e3e", hover_color = "#36587d", bg_color = "#011e3e" ,command = open_multi)
        Button2.place(x = 255, y = 150, width = 180, height = 60)

        Choose_Window.mainloop()
    

    def login(self):
        LWIN = tk.CTkToplevel()
        Fifth_Window = Login_Window()
        Fifth_Window.Make_Win(Window = LWIN, window_title = "Login", bgimg = "5thbg")



WINDOW = Windows()
