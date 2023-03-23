from tkinter import *
import sqlite3
from tkinter import messagebox as ms
from tkinter.font import BOLD
import datetime as dt   
root= Tk()
root.config(border='0')
root.state('zoomed')
def emt():
    if e4.get()=='':
        ms.showwarning('Warning','wrong id or password')
    else:
        ms.showinfo('welcome', 'Right option')

    
img1 = PhotoImage(file='usrimg/feedback1.png')
img1p = Label(root, image=img1,anchor='e').pack(side=LEFT)
date= dt.datetime.now()
appbg1= Label(root,text='Forgot\nPassword',font=('calibri',50,BOLD),bg='white').place(x=620,y=100)
#e2 = Entry(root,bg='White', border=2,relief=SOLID, font=('Corbel',18),width=30).place(x=580,y=350)
e3 = Entry(root,bg='white', border=2,relief=SOLID, font=('Corbel',18),width=30).place(x=580,y=550)
e4=Entry(root, width=28,font=('monospace',20),bg='white',border=0)
e4.place(x=585,y=270)
e4.insert(0,f"{date:%A,%B %d, %Y}")



l1 = Label(root,text="Question", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=350)

#Set the Menu initially
menu= StringVar()
menu.set("Select Your Question")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"Your school name","Your Pet name","Your nick name","Your age","your DOB" )
drop.place(x=580,y=350)
drop.config(bg='white',border=2,relief=SOLID,font=('Corbel',12,BOLD),width=40)

l7 = Label(root,text="Answer", bg='white',font=('Corbel',18,BOLD)).place(x=450,y=550)
b1= Button(root,text='Submit',font=('calibri',18,),border=1,bg='#FFC95C',relief=SOLID,activebackground='#FFC95C',fg='white',width=30,command=emt).place(x=580,y=670)
root.mainloop()