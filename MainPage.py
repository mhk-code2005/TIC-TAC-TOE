#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:10:48 2021

@author: mahir
"""

import tkinter
from tkinter import *
import Rules
def mainPLay():
    main=Tk()
    main.title('Tic Tac Toe')
    main.configure(bg='black')
    def button1v1():
        import Playing1v1 as p1v1
        n=int(a.get())
        main.destroy()
        try:
            p1v1(n)
        except:
            p1v1.play(n)
            
    def button1vpc():
        from againstPC import playvspc as apc
        n=int(a.get())
        main.destroy()
        apc(n)
    def rul():
        main.destroy()
        Rules.printRules()
    image2=PhotoImage(file='a.png')
    label=Label(main, image=image2, text='a').grid(row=1, columnspan=10)
    Button(main, text='1V1', width=30, height=5, command=button1v1).grid(row=2, column=1)
    Button(main, text='Against a computer', command=button1vpc, width=37, height=5).grid(row=2, column=3, columnspan=2)
    Button(main, text='rules', command=rul, width=10, height=5).grid(row=2, column=2)
    Label(main, text='Rows And Columns:', bg='black', fg='white').grid(row=4, column=2, columnspan=4)
    a=Entry(main, width=10, bg='black', fg='white')
    a.insert(END, 3)
    a.grid(row=4,column=4, columnspan=2)
    def quit():
        main.destroy()
        main.quit()
    Button(main, text="Quit", bg='black',command=quit, fg='white').grid(row=4, column=1)
    mainloop()
    
    
mainPLay()



