from tkinter import *
from PL.AppRegister import *
from PL.AppRegister import App
from BE.bePersonal import Personal
import customtkinter

customtkinter.set_appearance_mode("green")
customtkinter.set_default_color_theme("blue")

if __name__=="__main__":
    screen=customtkinter.CTk()
    screen.geometry(("1200x700+100+10"))
    screen.title("Language school")
    screen.iconbitmap("img/lang.ico")
    screen.configure(background="#f6f6f7")
    PageMe=App(screen)
    screen.mainloop()






