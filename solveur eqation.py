# Programme pour résoudre des équations à 3 inconnus 3 équations 
from fractions import Fraction
from tkinter import *
from math import gcd
matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

fen = Tk()
fen.title("solveur")
fen.geometry("500x400")
fen.configure(bg ="black")

def get_entry():
    global matrice_int,liste,x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result
    x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result="","","","","","","","","","","",""
    liste = [x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result]
    liste_entry = [x1_entry,y1_entry,z1_entry,line1_result_entry,x2_entry,y2_entry,z2_entry,line2_result_entry,x3_entry,y3_entry,z3_entry,line3_result_entry]
    for i in range(12):
        liste[i]= liste_entry[i].get()
        if liste[i] == "":
            liste[i]=0
    matrice_int =[]
    x=0
    for i in range(3):
        for a in range(4) :
            matrice[i][a]=liste[x]
            x+=1
            matrice_int.append(int(matrice[i][a]))
def fct_validation():
    global matrice_int
    get_entry()
    fct_pivot_gauss()

def fct_pivot_gauss():
    global matrice_int
    #1 ere ligne matrice pivot = 1
    for a in range (1,4):
        matrice_int[a]= Fraction(matrice_int[a]/matrice_int[0])
        matrice_int[a] = matrice_int[a]
        
    matrice_int[0]=1
    #2 eme ligne matrice moins la pivot 1
    x = 1
    for i in range(5,8):
        
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[4]*matrice_int[x]))
        x+=1
    matrice_int[4]= 0

    #3 eme ligne matrice moins le pivot 1
    x = 1
    for i in range(9,12):
        
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[8]*matrice_int[x]))
        x+=1
    matrice_int[8]= 0
    #2 eme ligne pivot = 1 :
    for a in range (6,8):
        matrice_int[a]= Fraction(matrice_int[a]/matrice_int[5])
    matrice_int[5]= 1
# 3 eme ligne moins le pivot 2
    x = 6
    for i in range (10,12):
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[9]*matrice_int[x]))
        x+=1
    matrice_int[9]=0
    #3 eme ligne pivot = 1:
    
    matrice_int[11]= Fraction(matrice_int[11]/matrice_int[10])
    matrice_int[10]= 1

    # on remonte le 3 eme pivot en ligne 2

    matrice_int[7]=matrice_int[7]-(matrice_int[6]*matrice_int[11])
    matrice_int[6]=0
    
    # on remonte le 3 eme pivot en ligne 1

    matrice_int[3]= matrice_int[3]-matrice_int[2]*matrice_int[11]
    matrice_int[2]=0

    # on remonte le 2 eme pivot en ligne 1
    matrice_int[3]= matrice_int[3]-matrice_int[1]*matrice_int[7]
    matrice_int[1]=0
    for i in range(3,12,4):
        matrice_int[i] = matrice_int[i].limit_denominator()

    texte = f"La solution de l'équation est x = {matrice_int[3]} y =  {matrice_int[7]} et z = {matrice_int[11]}"
    
        
    label_solution = Label(fen,text = texte,font ="arial 10 bold" )
    label_solution.pack()
    

x1_entry = Entry(fen,width=3)
x1_entry.place(x= 70,y = 70)
x1_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=65)


x2_entry = Entry(fen,width=3)
x2_entry.place(x= 70,y = 150)
x2_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=145)

x3_entry= Entry(fen,width=3)
x3_entry.place(x= 70,y = 220 )
x3_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=215)

y1_entry= Entry(fen,width=3)
y1_entry.place(x= 200,y = 70)
y1_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=65)

y2_entry= Entry(fen,width=3)
y2_entry.place(x= 200,y = 150)
y2_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=145)

y3_entry= Entry(fen,width=3)
y3_entry.place(x= 200,y = 220)
y3_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=215)

z1_entry= Entry(fen,width=3)
z1_entry.place(x= 330,y = 70)
z1_label = Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=65)

z2_entry= Entry(fen,width=3)
z2_entry.place(x= 330,y = 150)
z2_label = Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=145)

z3_entry= Entry(fen,width=3)
z3_entry.place(x= 330,y = 220)
z3_label= Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=215)

line1_result_entry = Entry(fen,width=3)
line1_result_entry.place(x= 460,y = 70)
line2_result_entry = Entry(fen,width=3)
line2_result_entry.place(x= 460,y = 150)
line3_result_entry = Entry(fen,width=3)
line3_result_entry.place(x= 460,y = 220)

submit_button = Button(fen, text="Valider", command=fct_validation).place(x=220,y=350)
fen.mainloop()
# Programme pour résoudre des équations à 3 inconnus 3 équations 
from fractions import Fraction
from tkinter import *
from math import gcd
matrice = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

fen = Tk()
fen.title("solveur")
fen.geometry("500x400")
fen.configure(bg ="black")

def get_entry():
    global matrice_int,liste,x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result
    x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result="","","","","","","","","","","",""
    liste = [x1,y1,z1,line1_result,x2,y2,z2,line2_result,x3,y3,z3,line3_result]
    liste_entry = [x1_entry,y1_entry,z1_entry,line1_result_entry,x2_entry,y2_entry,z2_entry,line2_result_entry,x3_entry,y3_entry,z3_entry,line3_result_entry]
    for i in range(12):
        liste[i]= liste_entry[i].get()
        if liste[i] == "":
            liste[i]=0
    matrice_int =[]
    x=0
    for i in range(3):
        for a in range(4) :
            matrice[i][a]=liste[x]
            x+=1
            matrice_int.append(int(matrice[i][a]))
def fct_validation():
    global matrice_int
    get_entry()
    fct_pivot_gauss()

def fct_pivot_gauss():
    global matrice_int
    #1 ere ligne matrice pivot = 1
    for a in range (1,4):
        matrice_int[a]= Fraction(matrice_int[a]/matrice_int[0])
        matrice_int[a] = matrice_int[a]
        
    matrice_int[0]=1
    #2 eme ligne matrice moins la pivot 1
    x = 1
    for i in range(5,8):
        
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[4]*matrice_int[x]))
        x+=1
    matrice_int[4]= 0

    #3 eme ligne matrice moins le pivot 1
    x = 1
    for i in range(9,12):
        
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[8]*matrice_int[x]))
        x+=1
    matrice_int[8]= 0
    #2 eme ligne pivot = 1 :
    for a in range (6,8):
        matrice_int[a]= Fraction(matrice_int[a]/matrice_int[5])
    matrice_int[5]= 1
# 3 eme ligne moins le pivot 2
    x = 6
    for i in range (10,12):
        matrice_int[i]= Fraction(matrice_int[i]-(matrice_int[9]*matrice_int[x]))
        x+=1
    matrice_int[9]=0
    #3 eme ligne pivot = 1:
    
    matrice_int[11]= Fraction(matrice_int[11]/matrice_int[10])
    matrice_int[10]= 1

    # on remonte le 3 eme pivot en ligne 2

    matrice_int[7]=matrice_int[7]-(matrice_int[6]*matrice_int[11])
    matrice_int[6]=0
    
    # on remonte le 3 eme pivot en ligne 1

    matrice_int[3]= matrice_int[3]-matrice_int[2]*matrice_int[11]
    matrice_int[2]=0

    # on remonte le 2 eme pivot en ligne 1
    matrice_int[3]= matrice_int[3]-matrice_int[1]*matrice_int[7]
    matrice_int[1]=0
    for i in range(3,12,4):
        matrice_int[i] = matrice_int[i].limit_denominator()

    texte = f"La solution de l'équation est x = {matrice_int[3]} y =  {matrice_int[7]} et z = {matrice_int[11]}"
    
        
    label_solution = Label(fen,text = texte,font ="arial 10 bold" )
    label_solution.pack()
    

x1_entry = Entry(fen,width=3)
x1_entry.place(x= 70,y = 70)
x1_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=65)


x2_entry = Entry(fen,width=3)
x2_entry.place(x= 70,y = 150)
x2_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=145)

x3_entry= Entry(fen,width=3)
x3_entry.place(x= 70,y = 220 )
x3_label = Label(fen,text = "x   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=100,y=215)

y1_entry= Entry(fen,width=3)
y1_entry.place(x= 200,y = 70)
y1_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=65)

y2_entry= Entry(fen,width=3)
y2_entry.place(x= 200,y = 150)
y2_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=145)

y3_entry= Entry(fen,width=3)
y3_entry.place(x= 200,y = 220)
y3_label = Label(fen,text = "y   +",font = "arial 16 bold ",bg = "black",fg = "white").place(x=230,y=215)

z1_entry= Entry(fen,width=3)
z1_entry.place(x= 330,y = 70)
z1_label = Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=65)

z2_entry= Entry(fen,width=3)
z2_entry.place(x= 330,y = 150)
z2_label = Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=145)

z3_entry= Entry(fen,width=3)
z3_entry.place(x= 330,y = 220)
z3_label= Label(fen,text = "z   =",font = "arial 16 bold ",bg = "black",fg = "white").place(x=360,y=215)

line1_result_entry = Entry(fen,width=3)
line1_result_entry.place(x= 460,y = 70)
line2_result_entry = Entry(fen,width=3)
line2_result_entry.place(x= 460,y = 150)
line3_result_entry = Entry(fen,width=3)
line3_result_entry.place(x= 460,y = 220)

submit_button = Button(fen, text="Valider", command=fct_validation).place(x=220,y=350)
fen.mainloop()
