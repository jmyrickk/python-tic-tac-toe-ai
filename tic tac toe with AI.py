import customtkinter as ctk
import sys, os
import random
from tkinter import messagebox
wstep="x"
butons=[]
winingComb=((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
def Cs():
    #prioritets 1. win 2. block 3. centr 4. couriers 5. 1, 3, 5, 7
    #win
    for i,o,p in winingComb:
        buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
        if buttonText.count("o")==2 and buttonText.count("")==1:
            indxOfNothing=[i, o, p][buttonText.index("")]
            butons[indxOfNothing].configure(text="o")
            Win()
            return
    #block
    for i,o,p in winingComb:
        buttonText=[butons[i].cget("text"), butons[o].cget("text"), butons[p].cget("text")]
        if buttonText.count("x")==2 and buttonText.count("")==1:
            indxOfNothing=[i,o,p][buttonText.index("")]
            butons[indxOfNothing].configure(text="o")
            Win()
            return
    #centr
    if butons[4].cget("text")=="":
        butons[4].configure(text="o")
        Win()
        return
    #couriers
    if butons[0].cget("text")=="" or butons[2].cget("text")=="" or butons[6].cget("text")=="" or butons[8].cget("text")=="":
        indxOfNothing = []
        for i in [0, 2, 6, 8]:
            if butons[i].cget("text")=="":
                indxOfNothing.append(i)
        rcs=random.choice(indxOfNothing)
        butons[rcs].configure(text="o")
        Win()
        return
    #1, 3, 5, 7
    if butons[1].cget("text") == "" or butons[3].cget("text") == "" or butons[5].cget("text") == "" or butons[7].cget("text") == "":
        indxOfNothing = []
        for i in [1, 3, 5, 7]:
            if butons[i].cget("text")=="":
                indxOfNothing.append(i)
        rcs=random.choice(indxOfNothing)
        butons[rcs].configure(text="o")
        Win()
        return
def Win():
    global scoreX, plx, scoreO, plo
    for i,o,p in winingComb:
        if butons[i].cget("text")=="x" and butons[o].cget("text")=="x" and butons[p].cget("text")=="x":
            print("win x")
            scoreX+=1
            plx.configure(text=f"player x : {scoreX}")
            messagebox.showinfo(title="win", message="x has win")
            for bb in butons:
                bb.configure(fg_color="green", text="x win", font=("Courier", 30, "bold"))
        elif butons[i].cget("text")=="o" and butons[o].cget("text")=="o" and butons[p].cget("text")=="o":
            print("win o")
            scoreO += 1
            plo.configure(text=f"player o : {scoreO}")
            messagebox.showinfo(title="win", message="o has win")
            for aa in butons:
                aa.configure(fg_color="green", text="o win", font=("Courier", 30, "bold"))
def openicon(put):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, put)
    return os.path.join(os.path.abspath("."), put)
def step(indx):
    global wstep, butons
    if butons[indx].cget("text")=="":
        butons[indx].configure(text=wstep)
        Win()
        Cs()
def reset():
    for e in range(9):
        butons[e].configure(fg_color="black", font=("Courier", 100, "bold"), text="")
scoreX=0
scoreO=0
window=ctk.CTk(fg_color="white")
window.geometry("518x600+620+100")
window.title("tic-tac-toe")
window.wm_iconbitmap(openicon("imag.ico"))
for u in range(1, 10):
    buton=ctk.CTkButton(window, text="", height=173, width=173, font=("Courier", 100, "bold"), fg_color="black", hover_color="gray", command=lambda nam=u: step(nam-1))
    buton.grid(column=(u-1)%3, row=(u-1)//3+2, sticky="wesn")
    butons.append(buton)
plx=ctk.CTkLabel(window, text=f"player x : {scoreX}", text_color="black", height=100, width=50, font=("Courier", 20, "bold"))
plo=ctk.CTkLabel(window, text=f"player o : {scoreO}", text_color="black", height=100, width=50, font=("Courier", 20, "bold"))
rb=ctk.CTkButton(window, text="reset", fg_color="red", hover_color="brown", font=("Courier", 20, "bold"), command=reset)
plx.grid(column=0, row=5, sticky="wesn")
plo.grid(column=2, row=5, sticky="wesn")
rb.grid(column=1, row=5, sticky="wesn")
window.mainloop()