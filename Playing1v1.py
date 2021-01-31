#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:53:26 2021

@author: mahir
"""

import tkinter
from tkinter import *
import Rules
# from Rules import creatingAmoveBoard as CAB
# from Rules import printBoard as pb
import Checking as ch
def play(n):
    master=Tk()
    master.configure(bg='black')
    global t
    global turned
    global flag
    global Round
    global winners
    global scoreboard
    Round=1
    master.title('TIC TAC TOE')
    flag='X'
    
    turned={}
    t=1
    Board=Rules.creatingAmoveBoard(n)[2]
    winner=None
    winners={'X':0, 'O':0}
    
    #scoreboard
    scoreboard= Label(master, bg='black', fg='white', text=('Round '+str(Round)+ '--> X: '+str(winners['X'])+' , O: '+ str(winners['O'])))
    #command when clicked
    
    
    def buttonCommand(event):

           global t
           global turned
           global flag
           global Round
           global winners
           global scoreboard
           def clearBoard(b):
                for x in range(len(b)):
                    for t in range(len(b[x])):
                        b[x][t]='?'
           winner=ch.checkIfSomeoneWon(Board) 
                      
           def update(): 
                global Round
                if cTf()!=1:
                    Round+=1
                clearBoard(Board)
                destroyLabels()
                createLabels()
                scoreboard= Label(master, bg='black', fg='white', text=('Round '+str(Round)+ '--> X: '+str(winners['X'])+' , O: '+ str(winners['O'])))
                scoreboard.grid(row=0, column=n+1, rowspan=1)

           
           if winner!=None:
                 winners[winner]+=1
                 update()
            
           info = event.widget.grid_info ()
           dicti={'X':'red', 'O':'blue'}
           coordinates=(info ['row'], info ['column'])
           x,y = coordinates
           liste=master.winfo_children()
           count=0
           
           for widget in liste:
               if widget['text']=='X' and widget['bg']=='red' or widget['text']=='O' and widget['bg']=='blue':
                   count+=1
               if (x,y) not in turned:
                   turned.update({(x,y):0})       
           if cTf()==1:
               master.unbind('<Button 1>', buttonCommand)

           if turned[(x,y)]==0:
                    if t==1:
                       flag='X'
                       t=0
                       Label(master, bg='red', text='X', borderwidth=10, relief="groove", width=30, height=10).grid(row=x, column= y)
                       Board[x][y]='X'
                        
                    else:
                        flag='O'
                        t=1
                        Label(master, bg='blue', text='O', borderwidth=10, relief="groove", width=30, height=10).grid(row=x, column= y)
                        Board[x][y]='O' 
                    turned[(x,y)]=1  
           

           winner=ch.checkIfSomeoneWon(Board) 
           
           
           if winner!=None:
                winners[winner]+=1
                update()
           
           


               
           if draw()=='draw':
               winners['O']+=1
               winners['X']+=1
               update()



    def createLabels():
        wid=0
        het=0
        for i in range(n**2):
            a=Label(master, text='?', fg='white', bg='black', borderwidth=10, relief="groove", width=30, height=10)
            a.bind ("<Button-1>", buttonCommand) 
            a.grid(row=wid, column= het)
            if wid==n-1:
                wid=0
                het+=1
            else:
                wid+=1
            t=0
        for e in turned:
            turned[e]=0
    def destroyLabels():
            liste=master.winfo_children()
            for widget in liste:
                if widget['text']=='X' or widget['text']=='O' or widget['text']=='?':
                    widget.destroy()
                    
    def draw():
        liste=master.winfo_children()
        count=0
        for i in liste:
            if i['text']=='O' or i['text']=='X':
                count+=1
        if count==n**2 and ch.checkIfSomeoneWon(Board)==None:
            return 'draw'
    
    def cTf():
        global Round
        def congrats(e):
            global Round
            
            if e=='X':
                Label(master, bg='black', fg='white' ,text= ('Game Over, X won '+ str(winners['X'])+ ' to '+ str(winners['O'])+ ' in '+ str(Round)+ ' rounds ')).grid(row=1, column=n+1)
            elif e=='d':
                Label(master, text= 'Game Over, Draw').grid(row=1, column=n+1)
            else:
                Label(master, text= 'Game Over, O won '+ str(winners['O'])+ ' to '+ str(winners['X'])+ ' in '+ str(Round)+ ' rounds ').grid(row=1, column=n+1)
        if winners['O']==3 and winners['X']==3:
            congrats('d')
            return 1
        if winners['X']==3 and winners['O']<3:
            congrats('X')
            
            return 1
        if winners['O']==3 and winners['X']<3:
            congrats('O')
            return 1

            
        
    createLabels()
    scoreboard.grid(row=0, column=n+1, rowspan=1)
    
    def rematch():
        if cTf()==1:
            master.destroy()
            play(n)


        else:
            warning=Tk()
            warning.title('Warning')
            warning.geometry('200x40')
            Label(warning, text='Please first finish this round').pack()

    def Quit():
        master.destroy()
        master.quit()
    def back():
        master.destroy()
        from MainPage import mainPLay
        mainPLay()
    Button(master, text='Rematch', command=rematch).grid(row=n+1, column=0)
    Button(master, text='Quit', command=Quit).grid(row=n+1, column=1)
    Button(master, text='Back', command=back).grid(row=n+1 ,column=2)
    
    mainloop()



