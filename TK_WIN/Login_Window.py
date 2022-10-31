import mysql.connector as sql

import os
import tkinter
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import END, INSERT, PhotoImage, ttk, messagebox
from Window_maker import Window_maker
import pickle as p
import csv

class Login_Window():
    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("dark-blue")
        self.current_user = None
        self.windowmaker = Window_maker()

#FIRST MAKE WINDOW LOGIN
    def Make_Win(self, Window, window_title, bgimg):

        Window.title(window_title)

        window_height = 500
        window_width = 450

        screen_width = Window.winfo_screenwidth()
        screen_height = Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        Window.resizable(False, False)

        global bg_img

        bgmg = Image.open(os.path.join("imgs",bgimg+".jpg"))
        bgmg.save(os.path.join("imgs",bgimg+".png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)


        background = tk.CTkLabel(master = Window, image = bg_img)
        background.place(x = 0, y = 0)

        self.widgetmaker(Window)

        Window.mainloop()

#WIDGETS
    def widgetmaker(self, Window):
        user_Entry = tk.CTkEntry(master = Window)
        user_Entry.place(x = 30, y = 110, width = 310, height = 30)

        user_Entry.insert(0, "Username")

        def on_enter(e):
            user_Entry.delete(0, END)
        def on_leave(e):
            if user_Entry.get() == "":
                user_Entry.insert(0, "Username")

        user_Entry.bind("<FocusIn>", on_enter)
        user_Entry.bind("<FocusOut>", on_leave)

        pass_Entry = tk.CTkEntry(master = Window, show = "*")
        pass_Entry.place(x = 30, y = 160, width = 310, height = 30)

        pass_Entry.insert(0, "Password")

        def on_enter(e):
            pass_Entry.delete(0, END)
        def on_leave(e):
            if pass_Entry.get() == "":
                pass_Entry.insert(0, "Password")

        pass_Entry.bind("<FocusIn>", on_enter)
        pass_Entry.bind("<FocusOut>", on_leave)


        def register():
            self.reg_window()

        def sql_login():
            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()
            username = user_Entry.get()
            password = pass_Entry.get()

            query = '''select * from  login where username = %s and password = %s'''
            mycursor.execute(query, [(username),(password)])
            data = mycursor.fetchall()

            if data:

                self.current_user = user_Entry.get()
                f = open("user.bin", "wb")
                p.dump(self.current_user, f)
                f.close()

                messagebox.showinfo("","Login Success")
                mysqldb.close()
                user_Entry.delete(0, END)
                pass_Entry.delete(0, END)

                self.windowmaker.user = str(self.current_user)

                return True
            else:
                messagebox.showerror("","Incorrect Username or Password")
                mysqldb.close()
                user_Entry.delete(0, END)
                pass_Entry.delete(0, END)
                return False

        def update():
            self.update_Window()

        def admin():
            self.admin_window()

        def deswin():
            try:
                Window.destroy()
            except tkinter.TclError:
                pass

        def logoff():
            self.current_user = None
            self.windowmaker.user = "Guest"
            messagebox.showinfo("","You have successfully logged out")

        def score():
            pass


        img1 = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img1 = img1.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img1)

        img2 = Image.open(os.path.join("imgs","download.png"))
        #img2.save(os.path.join("imgs","LLLG.png"))
        img2 = img2.resize((30,40), resample = 0)
        logout_img = ImageTk.PhotoImage(img2)

        login_button = tk.CTkButton(master = Window, text = "Login", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = sql_login)
        login_button.place(x = 35, y = 220, width = 100, height = 50)

        reg_question = tk.CTkLabel(master = Window, text = "Dont have an account yet?",text_font = ("Calibri", 13), text_color = "#c371c5", fg_color = "#191919")
        reg_question.place(x = 155, y = 278, width = 200, height = 20)

        register_button = tk.CTkButton(master = Window, text = "Register", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = register)
        register_button.place(x = 195, y = 220, width = 110, height = 50)

        admin_button = tk.CTkButton(master = Window, text = "Access Admin", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = admin)
        admin_button.place(x = 150, y = 310, width = 200, height = 50)

        back_button = tk.CTkButton(master = Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
        back_button.place(x = 10, y = 10, width = 60, height = 30)

        logout_button = tk.CTkButton(master = Window, text = "Logout", text_color = "black", text_font = ("Times New Roman", 12), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = logoff, image = logout_img, compound = "right")
        logout_button.place(x = 340, y = 8, width = 100, height = 44)

        update_button = tk.CTkButton(master = Window, text = "Update details", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = update)
        update_button.place(x = 150, y = 380, width = 200, height = 50)

        scores_button = tk.CTkButton(master = Window, text = "Highscores", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = score)
        scores_button.place(x = 150, y = 440, width = 200, height = 50)

#REGISTER
    def reg_window(self):
        register_Window = tk.CTkToplevel()
        register_Window.title("Register")

        window_height = 500
        window_width = 450

        screen_width = register_Window.winfo_screenwidth()
        screen_height = register_Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        register_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        register_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","5thbg.jpg"))
        bgmg.save(os.path.join("imgs","5thbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)

        background = tk.CTkLabel(master = register_Window, image = bg_img)
        background.place(x = 0, y = 0)

        ruser_Entry = tk.CTkEntry(master = register_Window)
        ruser_Entry.place(x = 20, y = 100, width = 300, height = 30)

        ruser_Entry.insert(0, "Username")

        def on_enter(e):
            ruser_Entry.delete(0, END)
        def on_leave(e):
            if ruser_Entry.get() == "":
                ruser_Entry.insert(0, "Username")

        ruser_Entry.bind("<FocusIn>", on_enter)
        ruser_Entry.bind("<FocusOut>", on_leave)

        remail_Entry = tk.CTkEntry(master = register_Window)
        remail_Entry.place(x = 20, y = 140, width = 300, height = 30)

        remail_Entry.insert(0, "Email")

        def on_enter(e):
            remail_Entry.delete(0, END)
        def on_leave(e):
            if remail_Entry.get() == "":
                remail_Entry.insert(0, "Email")

        remail_Entry.bind("<FocusIn>", on_enter)
        remail_Entry.bind("<FocusOut>", on_leave)

        rpass_Entry = tk.CTkEntry(master = register_Window)
        rpass_Entry.place(x = 20, y = 180, width = 300, height = 30)

        rpass_Entry.insert(0, "Password")

        def on_enter(e):
            rpass_Entry.delete(0, END)
        def on_leave(e):
            if rpass_Entry.get() == "":
                rpass_Entry.insert(0, "Password")

        rpass_Entry.bind("<FocusIn>", on_enter)
        rpass_Entry.bind("<FocusOut>", on_leave)

        re_pass_Entry = tk.CTkEntry(master = register_Window)
        re_pass_Entry.place(x = 20, y = 220, width = 300, height = 30)

        re_pass_Entry.insert(0, "Re-Enter Password")

        def on_enter(e):
            re_pass_Entry.delete(0, END)
        def on_leave(e):
            if re_pass_Entry.get() == "":
                re_pass_Entry.insert(0, "Re-Enter Password")

        re_pass_Entry.bind("<FocusIn>", on_enter)
        re_pass_Entry.bind("<FocusOut>", on_leave)


        def destroy():
            register_Window.destroy()

        def sql_register():
            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()
            username = ruser_Entry.get()
            password = rpass_Entry.get()
            email = remail_Entry.get()
            re_enter = re_pass_Entry.get()

            query1 = '''insert into login values(%s,%s,%s);'''
            query2 = '''insert into scores values(%s,0,0,0,Null)'''

            if password == re_enter:
                # try:
                mycursor.execute(query1, [(username),(password),(email)])
                mycursor.execute(query2, [(username)])
                mysqldb.commit()
                messagebox.showinfo("","Registered Successfully\nLogin with your details")
                mysqldb.close()
                ruser_Entry.delete(0, END)
                rpass_Entry.delete(0, END)
                rpass_Entry.delete(0, END)
                re_pass_Entry.delete(0, END)
                return True
                # except IntegrityError:
                #     messagebox.showerror("","Username already exists")

            else:
                messagebox.showerror("","Password doesn't match confirmation password")
                mysqldb.close()
                ruser_Entry.delete(0, END)
                rpass_Entry.delete(0, END)
                rpass_Entry.delete(0, END)
                re_pass_Entry.delete(0, END)
                return False

        def deswin():
            try:
                register_Window.destroy()
            except tkinter.TclError:
                pass

        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img)

        register_button_2 = tk.CTkButton(master = register_Window, text = "Register", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = sql_register)
        register_button_2.place(x = 80, y = 270, width = 110, height = 50)

        login_question = tk.CTkLabel(master = register_Window, text = "Already have an account?",text_font = ("Calibri", 13), text_color = "#c371c5", fg_color = "#191919")
        login_question.place(x = 180, y = 330, width = 200, height = 20)

        login_button = tk.CTkButton(master = register_Window, text = "Login", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = lambda:destroy())
        login_button.place(x = 225, y = 270, width = 100, height = 50)

        back_button = tk.CTkButton(master = register_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
        back_button.place(x = 10, y = 10, width = 60, height = 25)

        register_Window.mainloop()

    def del_window(self):
        del_Window = tk.CTkToplevel()
        del_Window.title("Remove a User")

        window_height = 500
        window_width = 450

        screen_width = del_Window.winfo_screenwidth()
        screen_height = del_Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        del_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        del_Window.resizable(False, False)

        bgmg = Image.open(os.path.join("imgs","5thbg.jpg"))
        bgmg.save(os.path.join("imgs","5thbg.png"))
        img = bgmg.resize((window_width,window_height), resample = 0)
        bg_img = ImageTk.PhotoImage(img)

        background = tk.CTkLabel(master = del_Window, image = bg_img)
        background.place(x = 0, y = 0)

        label = tk.CTkLabel(master = del_Window, text = "Enter username to be deleted", text_font = ("Calibri", 15), bg_color = "#191a1c")
        label.place(x = 30, y = 70, width = 270, height = 30)

        del_user_Entry = tk.CTkEntry(master = del_Window)
        del_user_Entry.place(x = 30, y = 110, width = 310, height = 30)

        def sql_delete():
            
            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()
            username = del_user_Entry.get()

            query1 = '''delete from scores where username = %s;'''
            mycursor.execute(query1,[(username)])
            query2 = '''delete from login where username = %s;'''
            mycursor.execute(query2, [(username)])
            mysqldb.commit()

            if username == "":
                messagebox.showerror("","Enter a name to delete")
            else:
                messagebox.showinfo("","User successfully deleted")

            mysqldb.close()

            f = open("slither_highscore.csv", "r", newline = "")
            csr = csv.reader(f)
            t = open("temp1.csv", 'w', newline = "")
            csw = csv.writer(t)
            found = 0
            for i in csr:
                if i[0] != username:
                    csw.writerow(i)
                else:
                    found = 1
            f.close()
            t.close()
            if found == 1:
                os.remove("slither_highscore.csv")
                os.rename("temp1.csv", "slither_highscore.csv")

            f = open("space_highscore.csv", "r", newline = "")
            csr = csv.reader(f)
            t = open("temp2.csv", 'w', newline = "")
            csw = csv.writer(t)
            found = 0
            for i in csr:
                if i[0] != username:
                    csw.writerow(i)
                else:
                    found = 1
            f.close()
            t.close()
            if found == 1:
                os.remove("space_highscore.csv")
                os.rename("temp2.csv", "space_highscore.csv")

        def deswin():
            try:
                del_Window.destroy()
            except tkinter.TclError:
                pass

        def see_user():
            user_Window = tk.CTkToplevel()
            user_Window.title("Admin Controls")

            window_height = 500
            window_width = 450

            screen_width = user_Window.winfo_screenwidth()
            screen_height = user_Window.winfo_screenheight()

            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int(((screen_height/2) - (window_height/2))-50)

            user_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            user_Window.resizable(False, False)

            global bg_img

            background = tk.CTkLabel(master = user_Window, image = bg_img)
            background.place(x = 0, y = 0)

            img = Image.open(os.path.join("imgs","back_button.png"))
            #img.save(os.path.join("imgs","back_button.png"))
            img = img.resize((20,20), resample = 0)
            button_img = ImageTk.PhotoImage(img)

            def deswin():
                try:
                    user_Window.destroy()
                except tkinter.TclError:
                    pass

            back_button = tk.CTkButton(master = user_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
            back_button.place(x = 10, y = 10, width = 60, height = 30)

            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()            
            query = '''select username from login;'''
            mycursor.execute(query)
            data = mycursor.fetchall()

            f1 = open("t.txt","w")
            for i in data:
                a = "".join(i)
                f1.write(a)
                f1.write("\n")
            f1.close()

            f2 = open("t.txt","r")
            d = f2.read()
            f2.close()

            user_label = tk.CTkLabel(master = user_Window, text = d, text_color = "White", text_font = ("calibri", 27), bg_color = "#1e1e1e")
            user_label.place(x = 0, y = 0, height = 500, width = 450)


            user_Window.mainloop()


        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img)


        delete_button = tk.CTkButton(master = del_Window, text = "Delete", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = sql_delete)
        delete_button.place(x = 40, y = 170, width = 110, height = 50)

        back_button = tk.CTkButton(master = del_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
        back_button.place(x = 10, y = 10, width = 60, height = 25)

        see_user_button = tk.CTkButton(master = del_Window, text = "see users", text_font = ("Calibri",20), fg_color = "#c371c5", hover_color = "#e886eb", command = see_user)
        see_user_button.place(x = 180, y = 170, width = 200, height = 50)

        del_Window.mainloop()

    def admin_window(self):
        admin_Window = tk.CTkToplevel()
        admin_Window.title("Admin Controls")

        window_height = 500
        window_width = 450

        screen_width = admin_Window.winfo_screenwidth()
        screen_height = admin_Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        admin_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        admin_Window.resizable(False, False)

        global bg_img

        background = tk.CTkLabel(master = admin_Window, image = bg_img)
        background.place(x = 0, y = 0)

        user_Entry = tk.CTkEntry(master = admin_Window)
        user_Entry.place(x = 30, y = 110, width = 310, height = 30)

        user_Entry.insert(0, "Username")

        def on_enter(e):
            user_Entry.delete(0, END)
        def on_leave(e):
            if user_Entry.get() == "":
                user_Entry.insert(0, "Username")

        user_Entry.bind("<FocusIn>", on_enter)
        user_Entry.bind("<FocusOut>", on_leave)

        pass_Entry = tk.CTkEntry(master = admin_Window, show = "*")
        pass_Entry.place(x = 30, y = 160, width = 310, height = 30)

        pass_Entry.insert(0, "Password")

        def on_enter(e):
            pass_Entry.delete(0, END)
        def on_leave(e):
            if pass_Entry.get() == "":
                pass_Entry.insert(0, "Password")

        pass_Entry.bind("<FocusIn>", on_enter)
        pass_Entry.bind("<FocusOut>", on_leave)

        def deswin():
            try:
                admin_Window.destroy()
            except tkinter.TclError:
                pass

        def sql_login():
            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()
            global username
            username = user_Entry.get()
            password = pass_Entry.get()

            query = '''select * from admin where username = %s and password = %s'''
            mycursor.execute(query, [(username),(password)])
            data = mycursor.fetchall()

            if data:

                self.current_user = user_Entry.get()
                f = open("user.bin", "wb")
                p.dump(self.current_user, f)
                f.close()

                self.del_window()
                mysqldb.close()
                
                self.windowmaker.user = str(self.current_user)

                return True
            else:
                messagebox.showerror("","Incorrect Username or Password")
                mysqldb.close()
                user_Entry.delete(0, END)
                pass_Entry.delete(0, END)
                return False

        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img)

        login_button = tk.CTkButton(master = admin_Window, text = "Login", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = sql_login)
        login_button.place(x = 35, y = 220, width = 100, height = 50)

        back_button = tk.CTkButton(master = admin_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
        back_button.place(x = 10, y = 10, width = 60, height = 30)

        admin_Window.mainloop()

    def update_Window(self):
        update_Window = tk.CTkToplevel()
        update_Window.title("Update your details")

        window_height = 500
        window_width = 450

        screen_width = update_Window.winfo_screenwidth()
        screen_height = update_Window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int(((screen_height/2) - (window_height/2))-50)

        update_Window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        update_Window.resizable(False, False)

        global bg_img
        global username
 
        background = tk.CTkLabel(master = update_Window, image = bg_img)
        background.place(x = 0, y = 0)

        user_Entry = tk.CTkEntry(master = update_Window)
        user_Entry.place(x = 30, y = 110, width = 310, height = 30)

        user_Entry.insert(0, "Username")

        def on_enter(e):
            user_Entry.delete(0, END)
        def on_leave(e):
            if user_Entry.get() == "":
                user_Entry.insert(0, "Username")

        user_Entry.bind("<FocusIn>", on_enter)
        user_Entry.bind("<FocusOut>", on_leave)

        email_Entry = tk.CTkEntry(master = update_Window)
        email_Entry.place(x = 30, y = 160, width = 310, height = 30)

        email_Entry.insert(0, "Enter new Email")

        def on_enter(e):
            email_Entry.delete(0, END)
        def on_leave(e):
            if email_Entry.get() == "":
                email_Entry.insert(0, "Enter new Email")

        email_Entry.bind("<FocusIn>", on_enter)
        email_Entry.bind("<FocusOut>", on_leave)

        pass_Entry = tk.CTkEntry(master = update_Window)
        pass_Entry.place(x = 30, y = 210, width = 310, height = 30)

        pass_Entry.insert(0, "Enter new Password")

        def on_enter(e):
            pass_Entry.delete(0, END)
        def on_leave(e):
            if pass_Entry.get() == "":
                pass_Entry.insert(0, "Enter new Password")

        pass_Entry.bind("<FocusIn>", on_enter)
        pass_Entry.bind("<FocusOut>", on_leave)

        repass_Entry = tk.CTkEntry(master = update_Window)
        repass_Entry.place(x = 30, y = 260, width = 310, height = 30)

        repass_Entry.insert(0, "Confirm new Password")

        def on_enter(e):
            pass_Entry.delete(0, END)
        def on_leave(e):
            if pass_Entry.get() == "":
                pass_Entry.insert(0, "Confirm new Password")

        pass_Entry.bind("<FocusIn>", on_enter)
        pass_Entry.bind("<FocusOut>", on_leave)

        def sql_update():
            
            username = user_Entry.get()
            mysqldb = sql.connect(host = "localhost", user = "root", password = "password", database = "project")
            mycursor = mysqldb.cursor()
            email = email_Entry.get()
            pass1 = pass_Entry.get()
            pass2 = repass_Entry.get()

            if str(pass1) == str(pass2):

                query = '''update login set email_id = %s, password = %s where username = %s'''
                mycursor.execute(query, [(email),(pass1),(username)])
                mysqldb.commit()

                messagebox.showinfo("","successfully updated")
                mysqldb.close()
                email_Entry.delete(0, END)
                pass_Entry.delete(0, END)
                repass_Entry.delete(0, END)
            
            else:
                messagebox.showerror("","Passwords don't match")
                mysqldb.close()
                email_Entry.delete(0, END)
                pass_Entry.delete(0, END)
                repass_Entry.delete(0, END)

        def deswin():
            try:
                update_Window.destroy()
            except tkinter.TclError:
                pass

        img = Image.open(os.path.join("imgs","back_button.png"))
        #img.save(os.path.join("imgs","back_button.png"))
        img = img.resize((20,20), resample = 0)
        button_img = ImageTk.PhotoImage(img)

        update_button = tk.CTkButton(master = update_Window, text = "Update", text_font = ("Calibri", 20), fg_color = "#c371c5", hover_color = "#e886eb", command = sql_update)
        update_button.place(x = 35, y = 320, width = 100, height = 50)

        back_button = tk.CTkButton(master = update_Window, text = "back", text_color = "black", text_font = ("Times New Roman", 8), fg_color = "#c371c5", hover_color = "#e886eb", bg_color = "#c371c5" ,command = deswin, image = button_img, compound = "left")
        back_button.place(x = 10, y = 10, width = 60, height = 30)


        update_Window.mainloop()