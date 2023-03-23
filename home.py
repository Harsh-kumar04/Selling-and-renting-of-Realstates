from tkinter import *
import sqlite3
import os
from tkinter import messagebox as ms
root= Tk()
root.state('zoomed')
img1 = PhotoImage(file='usrimg/home.png')
img1p = Label(root, image=img1).pack(side=TOP)

#button
b1= Button(root,text='Rent',font=('corbel',18,UNDERLINE),border=0,bg='white',activeforeground='orange').place(x=400,y=50)
b2= Button(root,text='Buy',bg='white',border=0,font=('corbel',18,UNDERLINE),activeforeground='orange').place(x=100,y=50)
b2= Button(root,text='About Us',activeforeground='orange',bg='white',border=0,font=('corbel',18,UNDERLINE)).place(x=220,y=50)
b1= Button(root,text='Feedback',font=('corbel',12,UNDERLINE),border=0,fg='white',bg='#FF7271',activebackground='#FF7271').place(x=220,y=468)
b1= Button(root,text='Profile',font=('corbel',12,UNDERLINE),border=0,fg='white',bg='#FF7271',activebackground='#FF7271').place(x=1280,y=75)
root.mainloop()