#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:36:07 2020

@author: mahir

"""

import Rules
import Checking as ch
#board,mode,moveList=Rules.printRules()
board=[['?',"?","?"],['?',"?","?"],['?',"?","?"]]
#print(moveList)

#game
numberOfRounds=0
while True:
    #X plays
    Xinput=tuple(input('It is your turn x, enter your location in format of 1,2: '))
    if Xinput=='quit':
        break
    
    try:
        rowloc,columnloc=int(Xinput[0]),int(Xinput[2])
    except:
        print('Invalid input, you wasted your turn')
    try:
        if board[rowloc][columnloc]=='?':
            board[rowloc][columnloc]='X'
        else:
            print('That location is already full, you wasted your turn.')
    except:
        print('That location is not in the board, you wasted your turn.')

    a=ch.checkIfSomeoneWon(board,numberOfRounds)
    if a!='?':
        break
    #O plays
    Oinput=(input('It is your turn o, enter your location in format of 1,2: '))
    if Oinput=='quit':
        break
    try:
        rowloc,columnloc=int(Oinput[0]),int(Oinput[2])
    except:
        print('Invalid input, you wasted your turn')
    try:
        if board[rowloc][columnloc]=='?':
            board[rowloc][columnloc]='O'
        else:
            print('That location is already full, you wasted your turn.')
    except:
        print('That location is not in the board, you wasted your turn.')
    numberOfRounds+=1
    a=ch.checkIfSomeoneWon(board,numberOfRounds)
    if a!='?':
        break

    Rules.printBoard(board)    


  
    
    