from tkinter import *
import sqlite3
import os
from tkinter import messagebox as ms
root= Tk()
root.state('zoomed')
#fetch and  match data
userinput= StringVar()
passs= StringVar()
def login():
    conn= sqlite3.connect('cracc.db')
    c= conn.cursor()
    c.execute("select * from adminlg where uid='%s' "%(userinput.get()))
    rows= c.fetchone()
    print(rows)
#all functions here
    a= userinput.get()
    b= passs.get()
    if a==rows[0] and b==rows[3] :
        file= 'home.py'
        os.system(file)
        ms.askokcancel("welcome","login success")
    else:
        ms.showwarning('Warning','wrong id or password')
bg= PhotoImage(file='usrimg/adminlogin.png')
bgplace= Label(root,image=bg).place(x=0,y=-250)

e1 =Entry(root,width=25,font=('monospace',15),textvariable=userinput,border=0)
e1.place(x=910,y=230)
e2 = Entry(root,width=25,font=('monospace',15),border=0,show='*',textvariable=passs).place(x=910,y=282)
B1 = Button(root,text='Login',font=('monospace',17),fg='white',activebackground='#007DFE',border=0,activeforeground='black',background='#007DFE',command=login).place(x=1016,y=362)
root.mainloop()