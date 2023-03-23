from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter.font import BOLD
root= Tk()
root.state('zoomed')
#mainframe
main_frame= Frame(root)
main_frame.pack(fill=BOTH, expand=1)
 
#create_canvas
my_canvas= Canvas(main_frame,width=200,bg='white')
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
 
#add scrollbar
 
my_scrollbar= ttk.Scrollbar(main_frame,orient= VERTICAL, command= my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
 
#configure scrollbar
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>" , lambda e : my_canvas.configure(scrollregion=my_canvas.bbox('all')))
 
#create another frame inside the canvas
second_frame= Frame(my_canvas)
# Image View image
 
#add the new frame to the window in canvas
my_canvas.create_window((0,0),window=second_frame,anchor= "nw")
 
#background
 
for thing in range(2):
    #bg= PhotoImage(file='bgnew.png',height=600)
    Label(second_frame,bg="white",width=700,height=70).pack(side=BOTTOM)


def change():
    img1.config(file='usrimg/garden.png')
def change1():
    img1.config(file='usrimg/ins1 (3).png')
def change2():
    img1.config(file='usrimg/ins1 (8).png')
def change3():
    img1.config(file='usrimg/ins1 (2).png')
#e0ffff

#up images

img= PhotoImage(file='usrimg/12.png')
imgp= Label(second_frame,image=img,border=0).place(x=0,y=0)

l1= Label(second_frame,text='#1, 3Bhk House,Ahemdabad,Gujrat',font=('Calibri',20,UNDERLINE,BOLD),bg='#E8E8E8').place(x=580,y=20)
img1= PhotoImage(file='usrimg/test.png')
img1p= Label(second_frame,image=img1,border=0).place(x=450,y=100)

img2= PhotoImage(file='usrimg\gardensmall.png')
img2p= Button(second_frame,image=img2,border=0,command=change).place(x=10,y=10)

img3= PhotoImage(file='usrimg\ins3small.png')
imp= Button(second_frame,image=img3,border=0,command=change1).place(x=100,y=150)

img4= PhotoImage(file='usrimg\ins4small.png')
img4p= Button(second_frame,image=img4,border=0,command=change2).place(x=1190,y=590)

img5= PhotoImage(file='usrimg\ins2small.png')
img5p= Button(second_frame,image=img5,border=0,command=change3).place(x=1100,y=450)



 
#house detail
discbox = Label(second_frame,border=3, relief=RIDGE).place(x=50,y=620)

#details
pan2= Label(second_frame,width=200,height=230,border=1,bg='white',relief=SOLID).place(x=70,y=850)
address=Label(second_frame,text="Address\n\n Dp East, sector 25 - Mira Road and Beyond, Gaziyabad ",font=('monospace',15),background='white').place(x=500,y=900)
Price= Label(second_frame,text="Rent\n\n₹20,000 to ₹30,000 ",font=('monospace',15,UNDERLINE),background='white').place(x=650,y=1100)
movingstatus= Label(second_frame,text="salient features\n\nWater Availability\n24 Hours Available\nStatus of Electricity\nNo/Rare Powercut",font=('monospace',15,),background='white').place(x=650,y=1200)
Buildingdesigner= Label(second_frame,text="Currently Owned By - Vision housing",font=('monospace',15,UNDERLINE),background='white').place(x=550,y=1300)
Pricing= Label(second_frame,text="View all Details\n\nDescription - Sunshine Green Park in Vasai East, is a ready-to-move housing complex. \n It offers apartments in varied budget range.\n These units are a perfect combination of comfort and style, specifically designed to suit your requirements and conveniences.\n There are Studio , 1 BHK and 2 BHK apartments available in this project. \n This housing complex is now ready to be called home as families have started moving in.",font=('monospace',15,),background='white').place(x=170,y=1300)

#appointment area
appbg= Label(second_frame,bg="white",width=230,height=50).place(x=0,y=1500)

img9= PhotoImage(file='usrimg/appoint.png')
img9p= Label(second_frame,image=img9,border=0,).place(x=50,y=1600) 

appbg1= Label(second_frame,text='Book\nAppointment ?',font=('calibri',50,BOLD),bg='white').place(x=700,y=1800)

img10= PhotoImage(file='usrimg/btn2.png')
img10p= Button(second_frame,image=img10,border=0).place(x=750,y=2000) 

""" img8= PhotoImage(file='usrimg\details.png')
img8p= Label(second_frame,image=img8,border=0,).place(x=150,y=1500)  """

root.mainloop()
