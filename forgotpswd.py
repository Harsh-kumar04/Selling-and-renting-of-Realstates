from tkinter import *
import sqlite3
from tkinter import messagebox as ms

root= Tk()
root.state('zoomed')
root.config(background='white')
#table
pswd= StringVar()
userid= StringVar()
def updt():
    conn =sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("update login set password= '%s' where fname = '%s' "%(pswd.get(),userid.get()) )
    conn.commit()
    conn.close()
    if e2=='':
        ms.showwarning('Warning','wrong id or password')
img1 = PhotoImage(file='usrimg/reset.png')
img1p = Label(root, image=img1,border=0).pack(side=TOP)
#entry
e1 = Entry(root,bg='#ECECEC', border=0, font=('Corbel',14),width=25,textvariable=userid).place(x=505,y=257)
e2 = Entry(root,bg='#ECECEC', border=0, font=('Corbel',14),width=22,textvariable=pswd).place(x=505,y=327)

#button
b1= Button(root,text='Done',font=('calibri',12),border=0,bg='#FFC95C',activebackground='#FFC95C',fg='white',command=updt).place(x=535,y=385)


root.mainloop()