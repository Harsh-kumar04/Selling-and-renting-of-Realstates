from tkinter import *
import sqlite3
from tkinter import messagebox as ms
import os
root= Tk()
root.state('zoomed')
root.config(background='#FFC95C')
img1 = PhotoImage(file='usrimg/sup.png')
img1p = Label(root, image=img1,border=0).pack(side=TOP)
#sql table
#creating table

conn =sqlite3.connect('admin.db')
c= conn.cursor()

c.execute('''create table if not exists login (fname real,lname real,email real,question real,password real, mob number,answer real) ''')
conn.commit()
conn.close()

#Insert query
fname= StringVar()
lname= StringVar()
email= StringVar()
pswd= StringVar()
menu= StringVar()
ans= StringVar()
mob= StringVar()
def data():
    conn= sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("insert into login values ('%s', '%s','%s', '%s','%s','%s','%s')"%(fname.get(),lname.get(),email.get(),menu.get(),pswd.get(),mob.get(),ans.get()))
    c.close()
    conn.commit()
    conn.close()
    filename='loginpg.py'
    os.system(filename)
#textbox
e1 = Entry(root,bg='white', border=0,textvariable=fname, font=('Corbel',14),width=25).place(x=460,y=310)
e2 = Entry(root,bg='white', border=0,textvariable=lname, font=('Corbel',14),width=25).place(x=765,y=310)
e3 = Entry(root,bg='white', border=0,textvariable=email, font=('Corbel',14),width=35).place(x=455,y=390)
e4 = Entry(root,bg='white', border=0,textvariable=pswd, font=('Corbel',14),width=25).place(x=460,y=470)
e6 = Entry(root,bg='white', border=0,textvariable=mob, font=('Corbel',14),width=55).place(x=455,y=550)



menu.set("Select Your Question")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"Your school name","Your Pet name","Your nick name","Your age","your DOB", )
drop.place(x=780,y=465)
drop.config(bg='white',border=0,relief=SOLID,font=('Corbel',14),width=20)
l2= Entry(root,bg='white', border=0,textvariable=menu, font=('Corbel',14),width=25).place(x=455,y=600) 
e7 = Entry(root,bg='white', border=2, font=('Corbel',14),width=25,textvariable=ans).place(x=650,y=600) 
#button
b1= Button(root,text='Sign Up',font=('calibri',18,),border=1,bg='#FFC95C',relief=SOLID,activebackground='#FFC95C',fg='white',width=32,command=data).place(x=580,y=670)

root.mainloop()