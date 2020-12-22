"""
Created on Mon Dec 21 08:21:15 2020

@author: Alex Bianchi
"""



def printBoard(board):
    
    for x in range(len(board)):
        if x % 3 == 0 and x !=0:
            print("= = = = = = = = = = = = = ")
        for y in range(len(board[0])):
            if y % 3 == 0 and y !=0:
                print('| ',end='')
            if y==8:
                 print(board[x][y])
            else:
                print(str(board[x][y]) + ' ',end='')

def findNextEmpty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x,y) #in reverse
            
            
def validate(board,number,pos):
    for x in range(len(board[0])):
        if board[pos[0]][x] == number and pos[0]!= x:
            return False
    for x in range(len(board)):
        if board[x][pos[1]] == number and pos[0]!= x:
            return False
         
    Bx=pos[1]//3
    By=pos[0]//3
    
    for i in range(By*3,By*3+3):
        for j in range(Bx*3,Bx*3+3):
            if board[i][j] == number and (i,j) != pos:
                return False
    return True
    
def solve(board):
    find=findNextEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for x in range(1,10):
        if validate(board, x, (row, col)):
            board[row][col] = x
            
            if solve(board):
                return True
            
            board[row][col] = 0
            
    return False

import random as r


def randomizeBoard():
    board = [[7, 8, 5, 4, 3, 9, 1, 2, 6],
             [6, 1, 2, 8, 7, 5, 3, 4, 9],
             [4, 9, 3, 6, 2, 1, 5, 7, 8],
             [8, 5, 7, 9, 4, 3, 2, 6, 1],
             [2, 6, 1, 7, 5, 8, 9, 3, 4],
             [9, 3, 4, 1, 6, 2, 7, 8, 5],
             [5, 7, 8, 3, 9, 4, 6, 1, 2],
             [1, 2, 6, 5, 8, 7, 4, 9, 3],
             [3, 4, 9, 2, 1, 6, 8, 5, 7]]
    for x in range(5):
        
        r1=r.randrange(0,3)
        r2=r.randrange(0,3)
        board[r1],board[r2]=board[r2],board[r1]
        
        r1=r.randrange(3,6)
        r2=r.randrange(3,6)
        board[r1],board[r2]=board[r2],board[r1]
        
        r1=r.randrange(6,9)
        r2=r.randrange(6,9)
        board[r1],board[r2]=board[r2],board[r1]
    
        
        r1=r.randrange(0,3)
        r2=r.randrange(0,3)
        for x in range(len(board)):
            board[x][r1],board[x][r2]=board[x][r2],board[x][r1]
            
        r1=r.randrange(3,6)
        r2=r.randrange(3,6)
        for x in range(len(board)):
            board[x][r1],board[x][r2]=board[x][r2],board[x][r1]
            
        r1=r.randrange(6,9)
        r2=r.randrange(6,9)
        for x in range(len(board)):
            board[x][r1],board[x][r2]=board[x][r2],board[x][r1]
        
    return board
    #L[::-1] to flip them
    
def radnomDelete(board):
    for x in range(50):
        r1=r.randrange(0,9)
        r2=r.randrange(0,9)
        board[r1][r2]=0
    return board

def createBoard():
    board=randomizeBoard()
    return radnomDelete(board)

solve(createBoard())
