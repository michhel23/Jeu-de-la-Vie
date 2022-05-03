from tkinter import *
from copy import deepcopy as copie

def numb(t,x,y,n):
    t[y+1][x+1]=n

def color():
    global colorCell
    global id
    if id != len(rgb)-1 and id+1!=idd or id!=9 and idd!=0:
        id+=1
    elif id+1==idd:
        id+=2
    elif id==9 and idd==0:
        id=1
    else:
        id=0
    
    colorCell=rgb[id]

def colorBg():
    global idd
    if idd != len(rgb)-1 and idd+1!=id or idd!=9 and id!=0:
        idd+=1
    elif idd+1==id:
        idd+=2
    elif idd==9 and id==0:
        idd=1
    else:
        idd=0
    
    base.configure(bg=rgb[idd])

def start():
    global table
    #création copie du tableau princ.
    past=copie(table)
    for y in range(1,h+1):
        for x in range(1,w+1):
            #compte le nombre de cellule vivantes dans les 8 cases autour
            life=0
            for i in range(-1,2):
                for j in range(-1,2):
                    life+=table[y+i][x+j]
            #naissance si 3 cellules vivantes autour d'une morte (règle n°1)
            if table[y][x]==0 and life==3:
                past[y][x]=1
            #mort si moins de 2 cellules vivantes ou plus de 3 cellules vivantes autour d'une vivante (règle n°2)
            elif table[y][x]==1 and life>4 or table[y][x]==1 and life<3:
                past[y][x]=0
    #après application des règles on modifie le tableau
    table=copie(past)
    #affichage du changement
    afficherGr(table)
    win.after(speed,go)

def click_gauche(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    base.create_rectangle(x, y, x+c, y+c, fill=colorCell,outline=colorCell)
    numb(table,int(x/c),int(y/c),1)

def click_droit(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    base.create_rectangle(x, y, x+c, y+c, fill=colorDeadCell,outline=colorDeadCell)
    numb(table,int(x/c),int(y/c),0) 

def stop():
    global stop
    stop=1

def go():
    global stop
    if stop==1:
        stop=0
    else:
        start()

def afficherGr(t):
    base.delete(ALL)
    for y in range(1,h+1):
        for x in range(1,w+1):
            if t[y][x]==1:
                base.create_rectangle(x*c, y*c, x*c+c, y*c+c, fill=colorCell,outline=colorCell)
    
#programme princ.
id=1
idd=8
rgb=["red","black","blue","green","yellow","purple","cyan","orange","white","pink"]
colorCell=rgb[id]
colorDeadCell=rgb[idd]
speed=200
win=Tk()
stop=0
#nombre de cases (largeur-hauteur)
w = 70
h = 50
width=700
height=500
c=10
win.configure(bg="grey")
table=[[0 for i in range(w+2)]for i in range(h+2)]
base = Canvas(win,width=700,height=500)
base.bind("<Button-1>",click_gauche)
base.bind('<Button-3>',click_droit)
base.configure(bg="white")
base.pack(side =TOP)



b1 = Button(win, text ='Go!', command =start)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(win,text="color change", command =color)
b2.pack(side = RIGHT,padx=3,pady=3)
b3 = Button(win,text="color bg change", command =colorBg)
b3.pack(side = RIGHT,padx=3,pady=3)
win.mainloop()




