import random
import tkinter
canvas=tkinter.Canvas(width=1000, height=800)
canvas.pack()

pozadie=tkinter.PhotoImage(file='nove1.png')
ramcek=tkinter.PhotoImage(file='citron2.png')
pozadie2=tkinter.PhotoImage(file='citron.png')
koniec=tkinter.PhotoImage(file='vlny.png')

def hlavne():
    global obrazovka
    obrazovka='hlavne'
    canvas.create_image(500,400,image=pozadie)
    canvas.create_text(500,250,text='OBESENEC',font='Georgia 70 bold',fill='#FAFAD2')
    canvas.create_image(500,450,image=ramcek)
    canvas.create_rectangle(300,410,700,490,width=5, outline='grey')
    canvas.create_text(500,450,text='Nová hra',font='Calibri 20 bold',fill='grey')

hlavne()


def pismenka():
    canvas.create_image(500,400,image=pozadie2)
    a=0
    for i in range(5):
        canvas.create_rectangle(230+a,450,290+a,510)
        canvas.create_rectangle(230+a,570,290+a,630)
        canvas.create_rectangle(230+a,690,290+a,750)
        a+=120
    canvas.create_text(260,480, text='E')
    canvas.create_text(260,600, text='F')
    canvas.create_text(260,720, text='H')
    canvas.create_text(380,480, text='G')
    canvas.create_text(380,600, text='I')
    canvas.create_text(380,720, text='N')
    canvas.create_text(500,480, text='O')
    canvas.create_text(500,600, text='R')
    canvas.create_text(500,720, text='S')
    canvas.create_text(620,480, text='T')
    canvas.create_text(620,600, text='C')
    canvas.create_text(620,720, text='A')
    canvas.create_text(740,480, text='K')
    canvas.create_text(740,600, text='B')
    canvas.create_text(740,720, text='L')
    

nespravne=0

def mys(a):

    x=a.x #suradnice kliknutie
    y=a.y

    #nova hra
    global obrazovka,slovo,nespravne
    
    if 300<x<700 and 410<y<490 and obrazovka=='hlavne':
        canvas.delete('all')
        obrazovka='hra'
        pismenka()
        slovo=random.choice(('crab','bear','frog','fish','horse','insect','shark','snake','tiger','ant','cat','lion'))
        for i in range(len(slovo)):
            canvas.create_line(100+(i*60),300,130+(i*60),300)
                
    #E                  
    if 230<x<290 and 450<y<510 and obrazovka=='hra' and slovo.count('e')>0:
        b=slovo.find('e')
        canvas.create_text(115+(b*60),280,text='E')
    elif 230<x<290 and 450<y<510 and obrazovka=='hra' and slovo.count('e')==0:
        nespravne+=1

    #F    
    if 230<x<290 and 570<y<630 and obrazovka=='hra' and slovo.count('f')>0:
        c=slovo.find('f')
        canvas.create_text(115+(c*60),280,text='F')
    elif 230<x<290 and 570<y<630 and obrazovka=='hra' and slovo.count('f')==0:
        nespravne+=1

    #H
    if 230<x<290 and 690<y<750 and obrazovka=='hra' and slovo.count('h')>0:
        d=slovo.find('h')
        canvas.create_text(115+(d*60),280,text='H')
    elif 230<x<290 and 690<y<750 and obrazovka=='hra' and slovo.count('h')==0:
        nespravne+=1
        
    #G
    if 350<x<410 and 450<y<510 and obrazovka=='hra' and slovo.count('g')>0:
        e=slovo.find('g')
        canvas.create_text(115+(e*60),280,text='G')
    elif 350<x<410 and 450<y<510 and obrazovka=='hra' and slovo.count('g')==0:
        nespravne+=1

    #I
    if 350<x<410 and 570<y<630 and obrazovka=='hra' and slovo.count('i')>0:
        f=slovo.find('i')
        canvas.create_text(115+(f*60),280,text='I')
    elif 350<x<410 and  570<y<630 and obrazovka=='hra' and slovo.count('i')==0:
        nespravne+=1

    #N
    if 350<x<410 and 690<y<750 and obrazovka=='hra' and slovo.count('n')>0:
        g=slovo.find('n')
        canvas.create_text(115+(g*60),280,text='N')
    elif 350<x<410 and 690<y<750 and obrazovka=='hra' and slovo.count('n')==0:
        nespravne+=1
    
    #O
    if 470<x<530 and 450<y<510 and obrazovka=='hra' and slovo.count('o')>0:
        h=slovo.find('o')
        canvas.create_text(115+(h*60),280,text='O')
    elif 470<x<530 and 450<y<510 and obrazovka=='hra' and slovo.count('o')==0:
        nespravne+=1

    #R
    if 470<x<530 and 570<y<630 and obrazovka=='hra' and slovo.count('r')>0:
        i=slovo.find('r')
        canvas.create_text(115+(i*60),280,text='R')
    elif 470<x<530 and 570<y<630 and obrazovka=='hra' and slovo.count('r')==0:
        nespravne+=1

    #S
    if 470<x<530 and 690<y<750 and obrazovka=='hra' and slovo.count('s')>0:
        j=slovo.find('s')
        canvas.create_text(115+(j*60),280,text='S')
    elif 470<x<530 and 690<y<750 and obrazovka=='hra' and slovo.count('s')==0:
        nespravne+=1

    #T
    if 590<x<650 and 450<y<510 and obrazovka=='hra' and slovo.count('t')>0:
        k=slovo.find('t')
        canvas.create_text(115+(k*60),280,text='T')
    elif 590<x<650 and 450<y<510 and obrazovka=='hra' and slovo.count('t')==0:
        nespravne+=1

    #C
    if 590<x<650 and 570<y<630 and obrazovka=='hra' and slovo.count('c')>0:
        l=slovo.find('c')
        canvas.create_text(115+(l*60),280,text='C')
    elif 590<x<650 and 570<y<630 and obrazovka=='hra' and slovo.count('c')==0:
        nespravne+=1

    #A
    if 590<x<650 and 690<y<750 and obrazovka=='hra' and slovo.count('a')>0:
        m=slovo.find('a')
        canvas.create_text(115+(m*60),280,text='A')
    elif 590<x<650 and 690<y<750 and obrazovka=='hra' and slovo.count('a')==0:
        nespravne+=1

    #K
    if 710<x<770 and 450<y<510 and obrazovka=='hra' and slovo.count('k')>0:
        n=slovo.find('k')
        canvas.create_text(115+(n*60),280,text='K')
    elif 710<x<770 and 450<y<510 and obrazovka=='hra' and slovo.count('k')==0:
        nespravne+=1

    #B
    if 710<x<770 and 570<y<630 and obrazovka=='hra' and slovo.count('b')>0:
        o=slovo.find('b')
        canvas.create_text(115+(o*60),280,text='B')
    elif 710<x<770 and 570<y<630 and obrazovka=='hra' and slovo.count('b')==0:
        nespravne+=1
                                                   
    #L
    if 710<x<770 and 690<y<750 and obrazovka=='hra' and slovo.count('l')>0:
        p=slovo.find('l')
        canvas.create_text(115+(p*60),280,text='L')
    elif 710<x<770 and 690<y<750 and obrazovka=='hra' and slovo.count('l')==0:
        nespravne+=1
        
    if nespravne==1:
        canvas.create_line(550,100,700,100)
    elif nespravne==2:
        canvas.create_line(700,100,700,300)
    elif nespravne==3:
        canvas.create_line(700,300,750,400)
    elif nespravne==4:
        canvas.create_line(700,300,650,400)
    elif nespravne==5:
        canvas.create_line(550,100,550,130)
    elif nespravne==6:
        canvas.create_oval(520,130,580,170)
    elif nespravne==7:
        canvas.create_line(550,170,550,250)
    elif nespravne==8:
        canvas.create_line(550,250,580,260)
    elif nespravne==9:
        canvas.create_line(550,250,520,260)
    elif nespravne==10:
        canvas.create_line(550,210,580,200)
    elif nespravne==11:
        canvas.create_line(550,210,520,200)
    elif nespravne==12:
        canvas.delete('all')
        obrazovka='koniec'
        canvas.create_image(500,400,image=koniec)
        canvas.create_rectangle(300,410,700,490,width=5, outline='grey')
        canvas.create_text(500,450,text='Game over',font='Calibri 20 bold',fill='grey')
        nespravne=0

    if 300<x<700 and 410<y<490 and obrazovka=='koniec':
        canvas.delete('all')
        obrazovka='hlavna'
        hlavne()
        
                                                    

canvas.bind('<Button-1>',mys)

canvas.mainloop()
