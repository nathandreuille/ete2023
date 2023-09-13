from tkinter import *

def fct_checkerboard():
    x1=0
    y1 =0
    x2=50
    y2=50
    color = ["#F3B368","#B07127"]
    c=0
    for i in range(10): #colone 
        for a in range(10):  #ligne   
            can.create_rectangle(x1,y1,x2,y2,fill=color[c])
            if a!=9 :  
                if c==0:
                    c=1
                else:
                    if a>5 :
                        can.create_oval(x1+10, y1+10 ,x2-10  ,y2-10 ,fill = "white")
                    if a<4 :
                        can.create_oval(x1+10, y1+10 ,x2-10  ,y2-10 ,fill = "black")
                    c=0
            else :
                if c==0:
                    c=0
                else:
                    c=1
                    can.create_oval(x1+10, y1+10 ,x2-10  ,y2-10 ,fill = "white")
            y1+=50
            y2+=50
        x1+=50
        x2+=50
        y1,y2=0,50
        
def fct_token(x1,y1,x2,y2,player):
    color = ["black","white"]
    can.create_oval(x1+10, y1+10, x2-10, y2-10 ,fill = color[player])

def clic(event):
    global player
    X = event.x//50
    Y = event.y//50
    
    #fct_token(X*50,Y*50,X*50+50,Y*50+50,player)
    if player==1: # changement du joueur 
        player=0
    elif player==0:
        player=1
    else :
         pass

window = Tk ()
can = Canvas(window, width = 500, height = 500, bg ="white")
can.pack()
player = 1
checkerboard_list = [[0,1,0,1,0,1,0,1,0,1],
                     [1,0,1,0,1,0,1,0,1,0],
                     [0,1,0,1,0,1,0,1,0,1],
                     [1,0,1,0,1,0,1,0,1,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,2,0,2,0,2,0,2,0,2],
                     [2,0,2,0,2,0,2,0,2,0],
                     [0,2,0,2,0,2,0,2,0,2],
                     [2,0,2,0,2,0,2,0,2,0]]

can.bind("<Button>",clic)
fct_checkerboard()

window.mainloop()