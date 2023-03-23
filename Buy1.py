
from cProfile import label
from distutils.command.config import config
from email.mime import image
from msilib import Table
from re import L
from sqlite3 import Row
from sysconfig import is_python_build
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
from tkinter.tix import COLUMN
from turtle import color, onclick, width
from unicodedata import is_normalized
import os
import sqlite3

from setuptools import Command

root=Tk()
root.state('zoomed')




 #button state
global is_on 
is_on = True

global is_on1
is_on1= True

global is_on2
is_on2= True

global is_on3
is_on3= True

global is_on4
is_on4= True

global is_on5
is_on5= True

global is_on6
is_on6= True

global is_on7
is_on7= True

global is_on8
is_on8= True

global is_on9
is_on9= True

global is_on10
is_on10= True

global is_on11
is_on11= True

global is_on12
is_on12= True

#function

#switch
def switch():
    global is_on
    if is_on:
        on.configure(file="heart1.png")
        is_on= False
    else:
        on.configure(file="heart.png")
        is_on= True 


def switch1():
    global is_on1
    if is_on1:
        on1.configure(file="heart1.png")
        is_on1= False
    else:
        on1.configure(file="heart.png")
        is_on1= True 
def switch2():
    global is_on2
    if is_on2:
        on2.configure(file="heart1.png")
        is_on2= False
    else:
        on2.configure(file="heart.png")
        is_on2= True 
def switch3():
    global is_on3
    if is_on3:
        on3.configure(file="heart1.png")
        is_on3= False
    else:
        on3.configure(file="heart.png")
        is_on3= True 
def switch4():
    global is_on4
    if is_on4:
        on4.configure(file="heart1.png")
        is_on4= False
    else:
        on4.configure(file="heart.png")
        is_on4= True 
def switch5():
    global is_on5
    if is_on5:
        on5.configure(file="heart1.png")
        is_on5= False
    else:
        on5.configure(file="heart.png")
        is_on5= True 
def switch6():
    global is_on6
    if is_on6:
        on6.configure(file="heart1.png")
        is_on6= False
    else:
        on6.configure(file="heart.png")
        is_on6= True 
def switch7():
    global is_on7
    if is_on7:
        on7.configure(file="heart1.png")
        is_on7= False
    else:
        on7.configure(file="heart.png")
        is_on7= True 
def switch8():
    global is_on8
    if is_on8:
        on8.configure(file="heart1.png")
        is_on8= False
    else:
        on8.configure(file="heart.png")
        is_on8= True 
def switch9():
    global is_on9
    if is_on9:
        on9.configure(file="heart1.png")
        is_on9= False
    else:
        on9.configure(file="heart.png")
        is_on9= True 
def switch10():
    global is_on10
    if is_on10:
        on10.configure(file="heart1.png")
        is_on10= False
    else:
        on10.configure(file="heart.png")
        is_on10= True 
def switch11():
    global is_on11
    if is_on11:
        on11.configure(file="heart1.png")
        is_on11= False
    else:
        on11.configure(file="heart.png")
        is_on11= True
def switch12():
    global is_on12
    if is_on12:
        on12.configure(file="heart1.png")
        is_on12= False
    else:
        on12.configure(file="heart.png")
        is_on12= True 
def pg1():
    filename = "bview1.py"
    os.system(filename)

def pg2():
    filename = "bview2.py"
    os.system(filename)
def pg3():
    filename = "bview3.py"
    os.system(filename)

#mainframe
main_frame= Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#create_canvas
my_canvas= Canvas(main_frame,width=90,bg='#191970')
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

#add scrollbar

my_scrollbar= ttk.Scrollbar(main_frame,orient= VERTICAL, command= my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

#configure scrollbar
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>" , lambda e : my_canvas.configure(scrollregion=my_canvas.bbox('all')))

#create another frame inside the canvas

second_frame= Frame(my_canvas)
 
#add the new frame to the window in canvas
my_canvas.create_window((0,0),window=second_frame,anchor= "nw")
 
#background

for thing in range(3):
    # bg= PhotoImage(file='bgnew.png',height=600)
    Label(second_frame,bg="white",width=500,height=100).pack(side=BOTTOM)

#sidebar for filters
background= Label(root, bg='#191970',height=305,width=50).place(x=0,y=0)

        
#all building BOX  

Label(second_frame,text='Favourites',font=('monospace',35,UNDERLINE)).place(x=830,y=0)
#box
panl= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=50)
btn=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground="white",command=pg1).place(x=1267,y=55)
IMG1= PhotoImage(file="images_rent\small\img2.png")
img1place= Label(second_frame,image=IMG1).place(x=420,y=70)
timeperiod=Label(second_frame,font=('monospace',10,UNDERLINE),background='white')
timeperiod.place(x=850,y=150)
details= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=180)
movingstatus= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=210)
Buildingdesigner= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=240)
Pricing= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=320)
on= PhotoImage(file="heart.png")
onbtn= Button(second_frame,image=on,border=0,command=switch,bg="#191970",activebackground="#191970").place(x=1448,y=70)

#box2
panl1= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=400)
btn1=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white',command=pg2).place(x=1267,y=405)
IMG2=  PhotoImage(file="images_rent\small\img1.png")
img2place= Label(second_frame,image=IMG2).place(x=420,y=420)
location1= Label(second_frame,font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=420)
timeperiod1=Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=500)
details1= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=530)
movingstatus1= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=560)
Buildingdesigner1= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=590)
Pricing1= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=670)
on1= PhotoImage(file="heart.png")
onbtn1= Button(second_frame,image=on1,border=0,command=switch1,bg="#191970",activebackground="#191970").place(x=1448,y=420)
#box3
panl2= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=750)
btn2=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white',command=pg3).place(x=1267,y=755)
IMG3=  PhotoImage(file="images_rent\small\img3.png")
img3place= Label(second_frame,image=IMG3).place(x=420,y=770)
location2= Label(second_frame,font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=770)
Timeperiod2=Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=850)
details2= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=880)
movingstatus2= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=910)
Buildingdesigner2= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=940)
Pricing2= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=1020)
on2= PhotoImage(file="heart.png")
onbtn2= Button(second_frame,image=on2,border=0,command=switch2,bg="#191970",activebackground="#191970").place(x=1448,y=770)
#box4
panl3= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=1100)
btn3=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=1105)
IMG4=  PhotoImage(file="images_rent\small\img4.png")
img4place= Label(second_frame,image=IMG4).place(x=420,y=1120)
location3= Label(second_frame,font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=1120)
timeperiod3=Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1200)
details3= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1230)
movingstatus3= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1260)
Buildingdesigner3= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1290)
Pricing3= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=1370) 
on3= PhotoImage(file="heart.png")
onbtn3= Button(second_frame,image=on3,border=0,command=switch3,bg="#191970",activebackground="#191970").place(x=1448,y=1120)
#box5
panl4= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=1450)
btn4=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=1455)
IMG5=  PhotoImage(file="images_rent\small\img5.png")
img5place= Label(second_frame,image=IMG5).place(x=420,y=1470)
location4= Label(second_frame,font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=1470)
timeperiod4=Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1550)
details4= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1580)
movingstatus4= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1610)
Buildingdesigner4= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1640)
Pricing4= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=1720)
on4= PhotoImage(file="heart.png")
onbtn4= Button(second_frame,image=on4,border=0,command=switch4,bg="#191970",activebackground="#191970").place(x=1448,y=1470)
#box6
panl5= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=1800)
btn5=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=1805)
IMG13=  PhotoImage(file="images_rent\small\img6.png")
img13place= Label(second_frame,image=IMG13).place(x=420,y=1820)
location5= Label(second_frame,font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=1820)
timeperiod5=Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1900)
details5= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1930)
movingstatus5= Label(second_frame,font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1960)
Buildingdesigner5= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=1990)
Pricing5= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=2070)
on5= PhotoImage(file="heart.png")
onbtn5= Button(second_frame,image=on5,border=0,command=switch5,bg="#191970",activebackground="#191970").place(x=1448,y=1820)
#box7
panl6= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=2150)
btn6=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=2155)
IMG6=  PhotoImage(file="images_rent\small\img7.png")
img6place= Label(second_frame,image=IMG6).place(x=420,y=2170)
location6= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=2170)
timeperiod6=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2250)
details6= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2280)
movingstatus6= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2310)
Buildingdesigner6= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2340)
Pricing6= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=2420)
on6= PhotoImage(file="heart.png")
onbtn6= Button(second_frame,image=on6,border=0,command=switch6,bg="#191970",activebackground="#191970").place(x=1448,y=2170)
#box8
panl7= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=2500)
btn7=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=2505)
IMG7=  PhotoImage(file="images_rent\small\img4.png")
img7place= Label(second_frame,image=IMG7).place(x=420,y=2520)
location7= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=2520)
timeperiod7=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2600)
details7= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2630)
movingstatus7= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2660)
Buildingdesigner7= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2690)
Pricing7= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=2770) 
on7= PhotoImage(file="heart.png")
onbtn7= Button(second_frame,image=on7,border=0,command=switch7,bg="#191970",activebackground="#191970").place(x=1448,y=2520)
#box9
panl8= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=2850)
btn8=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=2855)
IMG8=  PhotoImage(file="images_rent\small\img6.png")
img8place= Label(second_frame,image=IMG8).place(x=420,y=2870)
location8= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=2870)
timeperiod8=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2950)
details8= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=2980)
movingstatus8= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3010)
Buildingdesigner8= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3040)
Pricing8= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=3120) 
on8= PhotoImage(file="heart.png")
onbtn8= Button(second_frame,image=on8,border=0,command=switch8,bg="#191970",activebackground="#191970").place(x=1448,y=2870)
#box10
panl9= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=3200)
btn9=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=3205)
IMG9=  PhotoImage(file="images_rent\small\img1.png")
img9place= Label(second_frame,image=IMG9).place(x=420,y=3220)
location9= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=3320)
timeperiod9=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3400)
details9= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3430)
movingstatus9= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3460)
Buildingdesigner9= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3490)
Pricing9= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=3570)
on9= PhotoImage(file="heart.png")
onbtn9= Button(second_frame,image=on9,border=0,command=switch9,bg="#191970",activebackground="#191970").place(x=1448,y=3320)
#box11
panl10= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=3550)
btn10=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=3555)
IMG10=  PhotoImage(file="images_rent\small\img3.png")
img10place= Label(second_frame,image=IMG10).place(x=420,y=3570)
location10= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=3570)
timeperiod10=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3650)
details10= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3680)
movingstatus10= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3710)
Buildingdesigner10= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=3740)
Pricing10= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=3820)
on11= PhotoImage(file="heart.png")
onbtn11= Button(second_frame,image=on11,border=0,command=switch11,bg="#191970",activebackground="#191970").place(x=1448,y=3570)

#box12
panl11= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=3900)
btn11=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=3905)
IMG11=  PhotoImage(file="images_rent\small\img7.png")
img11place= Label(second_frame,image=IMG11).place(x=420,y=3920)
location11= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=3920)
timeperiod11=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4000)
details11= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4030)
movingstatus11= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4060)
Buildingdesigner11= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4090)
Pricing11= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=4170)
on12= PhotoImage(file="heart.png")
onbtn12= Button(second_frame,image=on12,border=0,command=switch12,bg="#191970",activebackground="#191970").place(x=1448,y=3920)
#box13
panl12= Label(second_frame,width=155,height=20,border=1,bg='white',relief=SOLID).place(x=400,y=4250)
btn12=  Button(second_frame,width=30,height=19,bg='#191970',relief=FLAT,border=0,activebackground='white').place(x=1267,y=4255)
IMG12=  PhotoImage(file="images_rent\small\img4.png")
img12place= Label(second_frame,image=IMG12).place(x=420,y=4270)
location12= Label(second_frame,text="5-BHK villa , sector-25, Rohini,New Delhi",font=('monospace',16,BOLD,UNDERLINE),background='white').place(x=850,y=4270)
timeperiod12=Label(second_frame,text="Year Of Build=2022",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4350)
details12= Label(second_frame,text="Configuration= 5-BHK, 3 Vehicles Parking",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4380)
movingstatus12= Label(second_frame,text="Possetion Status= Ready To Move",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4410)
Buildingdesigner12= Label(second_frame,text="Currently Owned By= Vision Housing",font=('monospace',10,UNDERLINE),background='white').place(x=850,y=4440)
Pricing12= Label(second_frame,text="Pricing= 6.5Cr to 7.2Cr",font=('monospace',10,UNDERLINE),background='white').place(x=1000,y=4520)
on10= PhotoImage(file="heart.png")
onbtn0= Button(second_frame,image=on10,border=0,command=switch10,bg="#191970",activebackground="#191970").place(x=1448,y=4270)
#display of building info
opt1= Label(second_frame,width=100, height=5, border=1, bg='red')
root.mainloop()