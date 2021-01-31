
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:56:55 2021

@author: mahir
"""

import time
import tkinter
from tkinter import *

#printing board function
def printBoard(board):
    for i in board:
        row=''
        for t in i:
            row+=str(t)+' '
        print(row) 



    

    

def creatingAmoveBoard(n):
    exampleBoard=[]
    moveList=[]
    board=[]
    numberOfRows=0
    numberOfCols=0
    for i in range(n):
            row=[]
            row2=[]
            for i in range(n):
                row2.append('?')
                if numberOfCols>n-1:
                    numberOfCols=numberOfCols%n
                row.append((numberOfRows,numberOfCols))
                moveList.append((numberOfRows,numberOfCols))
                numberOfCols+=1
            exampleBoard.append(row)
            numberOfRows+=1
            board.append(row2)
    return moveList, exampleBoard, board


#rules
def printRules():
    rules=Tk()
    x=10
    rules.geometry('600x550')
    rules.title('TIC TAC TOE: Rules')
    rules['bg']='black'
    Label(rules, text='               TIC TAC TOE              ', font=('Helvetica',18), bg='black', fg='white').grid(row=0, column=0)
    Label(rules, text='    This game was designed by Mahir Kaya, a coder at ROOT CODE', font=('Helvetica',12), bg='black', fg='white').grid(row=1, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=2, column=0)

    Label(rules, text='In this game, you have 2 options', font=('Helvetica',12), bg='black', fg='white').grid(row=3, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=4, column=0)

    Label(rules, text='  First, you need to set the row and column numbers from left bottom', font=('Helvetica',12), bg='black', fg='white').grid(row=5, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=6, column=0)

    Label(rules, text='Recommended number of Rows and Columns: 3', font=('Helvetica',12), bg='black', fg='white').grid(row=7, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=8, column=0)

    Label(rules, text=' Then, you will either choose playing against computer or playing with your friend', font=('Helvetica',12), bg='black', fg='white').grid(row=9, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=10, column=0)

    Label(rules, text='If you choose playing against the computer, you will randomly be assigned X or O', font=('Helvetica',12), bg='black', fg='white').grid(row=11, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=12, column=0)

    Label(rules, text='Then, you will play according to your turns', font=('Helvetica',12), bg='black', fg='white').grid(row=13, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=14, column=0)

    Label(rules, text='For both modes, you need to reach 3 wins in order to win', font=('Helvetica',12), bg='black', fg='white').grid(row=15, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=16, column=0)

    Label(rules, text='If you want to go back to the main page, click the button "Back"', font=('Helvetica',12), bg='black', fg='white').grid(row=17, column=0)
    Label(rules, text='                           ', font=('Helvetica',12), bg='black', fg='white').grid(row=18, column=0)

    Label(rules, text='ENJOY', font=('Helvetica',18), bg='black', fg='white').grid(row=19, column=0)

    def a():

        rules.destroy()
        from MainPage import mainPLay
        mainPLay()
    Button(rules, text='back', command=a, fg='white', bg='black').grid(row=20, column=0)

    mainloop()