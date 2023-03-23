from tkinter import *
import sqlite3
import os
from tkinter import messagebox as ms
root= Tk()
root.state('zoomed')
img1 = PhotoImage(file='usrimg/bg1.png')
img1p = Label(root, image=img1,anchor='e').pack(side=LEFT)
#table
#fetch and  match data
userinput= StringVar()
passs= StringVar()
def login():
    conn= sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("select * from login where fname='%s' "%(userinput.get()))
    rows= c.fetchone()
    print(rows)
#all functions here
    a= userinput.get()
    b= passs.get()
    if a==rows[0] and b==rows[3] :
        ms.askokcancel("welcome","login success")
    else:
        ms.showwarning('Warning','wrong id or password')
#switchpage
def forgot():
    filename='forgotpswd.py'
    os.system(filename)
def create():
    filename='createac.py'
    os.system(filename)
#lable
l1 = Label(root,text='New Here,', bg='white',font=('Corbel',12)).place(x=375,y=582)
l2 = Label(root,text="E-mail", bg='white',font=('Corbel',12)).place(x=213,y=350)

#textbox
e1 = Entry(root,bg='white', border=0, font=('Corbel',14),width=32,textvariable=userinput)
e1.place(x=213,y=350)
e2 = Entry(root,bg='white', border=0, font=('Corbel',14),width=32,textvariable=passs)
e2.place(x=213,y=400)
e1.insert(0,'Username')
e2.insert(0,'Password')
#button
b1= Button(root,text='Login',font=('calibri',12,),border=0,bg='#E040FA',activebackground='#E040FA',fg='white',width=32,command=login).place(x=260,y=510)
b2= Button(root,text='Forgot Password ?',fg='#E040FA',activebackground='white',activeforeground='yellow',bg='white',border=0,font=('corbel',12,UNDERLINE),command=forgot).place(x=450,y=450)
b2= Button(root,text='Create Account ?',fg='#E040FA',activebackground='white',activeforeground='yellow',bg='white',border=0,font=('corbel',12,UNDERLINE),command= create).place(x=450,y=580)
root.mainloop()