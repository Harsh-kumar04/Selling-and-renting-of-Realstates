from tkinter import *
from tkinter import ttk
import sqlite3
root= Tk()
root.state('zoomed')



    
#table1
s= ttk.Style()
s.theme_use('clam')
tree = ttk.Treeview(root, columns=("c1","c2","c3","c4"),show='headings',height=5)
tree.column("#1",anchor=CENTER)
tree.heading("#1",text='Date')
tree.column("#2",anchor=CENTER)
tree.heading("#2",text='ID')
tree.column("#3",anchor=CENTER)
tree.heading("#3",text='Subject')
tree.column("#4",anchor=CENTER)
tree.heading("#4",text='Discription')
tree.pack()



# date real,id real,subject real,discription real


def insert():
    conn= sqlite3.connect('admin.db')
    c= conn.cursor()
    c.execute("select * from feedback ")
    rows= c.fetchall()
    print(rows)
    for row in rows:
        tree.insert('','end',values=row)
   
tree.config(height= 20)
l1= Label(root,text='FeedBack Details',font=('calibri',51)).place(x=550,y=470)
b1= Button(root,text='SELECT DATA',font=('calibri',18,),border=1,bg='#FFC95C',relief=SOLID,activebackground='#FFC95C',fg='white',width=32,command=insert).place(x=580,y=670)
b2= Button(root,text='UPDATE',font=('calibri',18,),border=1,bg='#FFC95C',relief=SOLID,activebackground='#FFC95C',fg='white',width=32,command=insert).place(x=80,y=670)
b3= Button(root,text='DELETE',font=('calibri',18,),border=1,bg='#FFC95C',relief=SOLID,activebackground='#FFC95C',fg='white',width=32,command=insert).place(x=1080,y=670)

root.mainloop()
