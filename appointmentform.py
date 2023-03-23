from tkinter import *
import sqlite3
from tkinter.font import BOLD
import datetime as dt
import calendar
import sqlite3
root=Tk()
root.state("zoomed")
date= dt.datetime.now()
# table

conn =sqlite3.connect('admin.db')
c= conn.cursor()

c.execute('''create table if not exists appoint ( Fname real,lname real,number interger , address real,date real) ''')

conn.commit()
conn.close()

fnam= StringVar()
lnam= StringVar()
num= StringVar()
add= StringVar()
dat = StringVar()
def ins():
    conn= sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("insert into appoint values('%s', '%s','%s', '%s','%s')"%(fnam.get(),lnam.get(),num.get(),add.get(),dat.get()))
    c.close()
    conn.commit()
    conn.close()





bgplace = PhotoImage(file='usrimg/appsmall.png')
bg = Label(root,image=bgplace).pack(side=TOP)

logoplace2= Label(root,bg='#4577E6',width=200,height=9).place(x=63,y=60)
#heading
h1= Label(root,text='Vision Housing',font=('monospace',28,BOLD),bg='#4577e6',fg='white').place(x=80,y=120)
#h2 =Label(root,text='Book Appointment',font=('monospace',20),bg='white',fg='#4577e6').place(x=350,y=220)
e1= Entry(root,width=18,font=('monospace',15),border=0,textvariable=fnam)
e1.place(x=852,y=338)
e2= Entry(root,width=18,font=('monospace',15),border=0,textvariable=lnam)
e2.place(x=1068,y=338)
e3= Entry(root, width=28,font=('monospace',20),textvariable=dat)
e3.place(x=852,y=560)
e4 =Entry(root,border=0,width=28,font=('monospace',15),textvariable=num)
e4.place(x=852,y=385)
e5 =Entry(root,border=0,width=28,font=('monospace',15),textvariable=add)
e5.place(x=852,y=435)
b1 = Button(root,text='Submit',bg='white',command=ins,border=2,relief=SOLID,font=('monospace',15)).place(x=200,y=420)
e3.insert(0,f"{date:%A,%B %d, %Y}")
e1.insert(0,'First Name')
e2.insert(0,'Last Name')
e4.insert(0,'Mob. number')
e5.insert(0,'Address')

root.mainloop()