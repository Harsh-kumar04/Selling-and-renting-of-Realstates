from tkinter import *
import sqlite3
import os
root=Tk()
root.state("zoomed")
def createac():
    filename='ADMIN_ca.py'
    os.system(filename)
def signin():
    filename='adminac.py'
    os.system(filename)

#bg
bg= PhotoImage(file='usrimg/admin1.png')
bgplace= Label(root,image=bg).pack(side=TOP)
signbtn =Button(root,text='sign in' ,font=('script MT',12,),border=0,bg='white',fg='#a8bdd8',activebackground='white',command=signin).place(x=1340,y=70)
logbtn =Button(root,text='Login' ,font=('script MT',16,),border=0,bg='#52A8FC',fg='white',activebackground='#52A8FC',command= createac).place(x=260,y=425)

root.mainloop()
#design