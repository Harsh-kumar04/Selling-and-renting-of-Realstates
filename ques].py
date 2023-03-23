from tkinter import *
import sqlite3
from tkinter import messagebox as ms
from tkinter.font import BOLD
import datetime as dt   
root= Tk()
root.config(border='')
root.state('zoomed')
img1 = PhotoImage(file='usrimg/feedback1.png')
img1p = Label(root, image=img1,anchor='e').pack(side=LEFT)
date= dt.datetime.now()
appbg1= Label(root,text='Give\nFeedback',font=('calibri',50,BOLD),bg='white').place(x=620,y=100)
e1 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30,textvariable=id).place(x=580,y=350)
e2 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30).place(x=580,y=450)
e3 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30).place(x=580,y=550)
e4=Entry(root, width=28,font=('monospace',20),bg='white',border=0)
e4.place(x=585,y=270)
e4.insert(0,f"{date:%A,%B %d, %Y}")

l1 = Label(root,text="ID", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=350)
l2 = Label(root,text="Subject", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=450)
l3 = Label(root,text="Discription", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=550)
root.mainloop()