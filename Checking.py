#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:56:56 2021

@author: mahir
"""
from Rules import printBoard
#Check if someone won function
def checkIfSomeoneWon(board):
    
    #Check if elements in the same row are equal
    winner='?'
    for liste in board:
        if liste.count(liste[0])==len(liste):
            winner=liste[0]
        if winner!='?':                
            return winner
    
    flag=False  
    for i in range(len(board[0])):
        #elements in the same row
        x=0
        flag=True
        while x!=len(board[0]):
            try:
                if board[0][i]!=board[x][i]:
                    flag=False
            except:
                pass
            if flag==False:
                break
            x+=1
            
        if flag==True:
            winner=board[0][i]
            if winner!='?':                
                return winner
    for i in range(len(board[0])):
        x=0
        flag=True
        while x!=len(board[0]):
            try:
                if board[0][i]!=board[x][x]:
                    flag=False
            except:
                pass
            if flag==False:
                break
            x+=1
        if flag==True:
            winner=board[0][i]
            if winner!='?':                
                return winner
            break
    
    
    
    x=len(board[0])-1
    i=0
    flag=True
    
    while x!=0:
        try:
            if board[i][x]!=board[i+1][x-1]:
 
                flag=False
        except:
            pass
        
        if flag==False:
            break
        if x!=0:
            x-=1
            i+=1

            
    if flag==True:
            winner=board[0][i]

    if winner!='?':                
        # print(str(winner)+' won the game')
        return winner
    
            
            
            
