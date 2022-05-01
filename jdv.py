from time import sleep
from tkinter import *
import ctypes

def numb(t,x,y):
    t[y+1][x+1]=1

def copie(l):
    u=[]
    for i in l:
        u.append(list(i))
    return list(u)

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
    win.after(speed,start)

def click(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    base.create_rectangle(x, y, x+c, y+c, fill='black')
    numb(table,int(x/c),int(y/c))

def go(event):
    start() 

def afficherGr(t):
    base.delete(ALL)
    for y in range(1,h+1):
        for x in range(1,w+1):
            if t[y][x]==0:
                base.create_rectangle(x*c, y*c, x*c+c, y*c+c, fill='white',outline="white")
            else:
                base.create_rectangle(x*c, y*c, x*c+c, y*c+c, fill='black')
    
#programme princ.
print("___________________________________________________________________________\nclick gauche>>>poser une case\nclick droit>>>start\n(action à effectuer sur la fenetre une fois les valeurs entrées)\n___________________________________________________________________________")
speed=int(float(input("vitesse(fps):"))*1000)
c=int(input("taille d'une case(px):"))
win=Tk()
user32 = ctypes.windll.user32 
w = user32.GetSystemMetrics(78)//c
h = user32.GetSystemMetrics(79)//c
print(w,h)
table=[[0 for i in range(w+2)]for i in range(h+2)]
base = Canvas(win,width=w*c,height=h*c,bg='white')
base.bind("<Button-1>",click)
base.bind('<Button-3>',go)
base.pack()
win.mainloop()




