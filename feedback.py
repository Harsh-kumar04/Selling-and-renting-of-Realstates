from tkinter import *
import sqlite3
import os
from tkinter import messagebox as ms
from tkinter.font import BOLD
import datetime as dt
root= Tk()
root.state('zoomed')

conn =sqlite3.connect('admin.db')
c= conn.cursor()

c.execute('''create table if not exists feedback (date real,id real,subject real,discription real) ''')
conn.commit()
conn.close()

dt1= StringVar()
id= StringVar()
subject= StringVar()
desc= StringVar()
def data():
    conn= sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("insert into feedback  values ('%s', '%s','%s', '%s')"%(dt1.get(),id.get(),subject.get(),desc.get()))
    c.close()
    conn.commit()
    conn.close()
date= dt.datetime.now()
img1 = PhotoImage(file='usrimg/feedback1.png')
img1p = Label(root, image=img1,anchor='e').pack(side=LEFT)

appbg1= Label(root,text='Give\nFeedback',font=('calibri',50,BOLD),bg='white').place(x=620,y=100)
#e1 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30,textvariable=id).place(x=580,y=350)
e2 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30,textvariable=subject).place(x=580,y=450)
e3 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30,textvariable=desc).place(x=580,y=550)
e4=Entry(root, width=28,font=('monospace',20),bg='white',border=0,textvariable=dt1)
e4.place(x=585,y=350)
e4.insert(0,f"{date:%A,%B %d, %Y}")

#l1 = Label(root,text="ID", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=350)
l2 = Label(root,text="Subject", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=450)
l3 = Label(root,text="Discription", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=550)



btn =Button(root,bg='#FFC95C',activebackground='#FFC95C',border=0,text='Submit', font=('Corbel',18),width=25,command=data).place(x=600,y=650)
root.mainloop()