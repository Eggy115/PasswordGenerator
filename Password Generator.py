from random import *
import os
import tkinter

os.system("@echo off")
os.system("title Eggy115's Password Generator")
os.system("color 0a")
os.system("cls")


def continues():
    try:
        inp = inputtxt.get(1.0, "end-1c")
        lettercount = inp
        gui.destroy()
        

        password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8','9', 
            ':', ';', '@', '#', '~', '/', '?', '.', ',','<','>', 
            '!', '$', '%', '^','&', '*', '(', ')', '{', '}', '[', ']', '-', '+', '=', '_', ' ','\\', '|', '`', '¬', '"', '£', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 
            'W', 'X', 'Y', 'Z', ]

        passw = ""

        for key in range(int(lettercount)):
            passw_letter = password[randint(0, 94)]
            passw = str(passw_letter) + str(passw)

        os.system("color 0a")
        os.system("cls")
        print("Your randomly generated password is:\n" + passw)
        os.system("pause >nul")
    except:
        print("Something went wrong here. You may not have put in a valid number/any number at all. If this problem persists, please report it.")
        os.system("pause >nul")

def exits():
    exit()

gui = tkinter.Tk()

gui.geometry("350x300")
gui.title("Password Generator")
gui.resizable(0,0)
gui.configure(bg='#424242')


label = tkinter.Label(gui, text ="\nPress Continue to begin generating a program.\nPress exit to close down the window.\n", bg = '#424242', fg = 'white')
label.pack()

info = tkinter.Label(gui, text ="Enter the amount of digits in the password here.\n", bg = '#424242', fg = 'white')
info.pack()
inputtxt = tkinter.Text(gui, bg = '#313131', fg = 'white', height=1, width=8)
inputtxt.pack()

info = tkinter.Label(gui, text =" ", bg = '#424242', fg = 'white')
info.pack() 

B1 = tkinter.Button(gui, text ="Continue", command=continues, bg = '#424242', fg = 'white')
B2 = tkinter.Button(gui, text ="Exit", cursor="pirate", command=exits, bg = '#424242', fg = 'white')
B1.pack()
B2.pack()




  
gui.mainloop()



