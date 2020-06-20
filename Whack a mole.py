# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:46:58 2020

@author: Yash
"""

"""
make a board !@
create the mole !@ 
    show mole on the board !@
    timer functionality
player hit
check the score update the score 
"""

import random


board = ['_','_','_',
         '_','_','_',
         '_','_','_']

mole ="1"

game_running=True

score=0
health = 3
def show_board():
    print(board[0]+'|'+board[1]+'|'+board[2])    
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])


def play():
    
    while game_running:
        print("health is",health,"  ","Your score is",score)
        show_mole()
        
        check_if_hit()
        
        check_health()
        
        reset_board()
    print("You lose, your score was", score)
    
def show_mole():
    
    position = random.randint(0, 8)
    
    board[position]=mole
    
    show_board()
    
    

def check_if_hit():
    global score
    global health
    hitOn=input("WHERE's THE MOLE AT?\n")
    hitOn= int(hitOn)-1
    
    if board[hitOn]=='1':
       
        score+=5
    else:
        health-=1
    board[hitOn]='X'
    show_board()
    
def reset_board():
    global board
    board = ['_','_','_',
             '_','_','_',
             '_','_','_']
    

def check_health():
    global game_running
    if not health>0:
        game_running=False
        
play()