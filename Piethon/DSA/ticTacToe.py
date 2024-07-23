#!/usr/bin/pyhton3
"""
This module uses Dictionary Data Structure to create a 
tic-tac-toe game
"""


Board = {
        "top-L": " ", "top-M": " ", "top-R": " ",
        "mid-L": " ", "mid-M": " ", "mid-R": " ",
        "low-L": " ", "low-M": " ", "low-R": " "}

def printBoard(board):
    """Prints out the game board"""
    print(Board['top-L'] + "|" + Board['top-M'] + "|" + Board['top-R'])
    print("-+-+-")
    print(Board['mid-L'] + "|" + Board['mid-M'] + "|" + Board['mid-R'])
    print("-+-+-")
    print(Board['low-L'] + "|" + Board['low-M'] + "|" + Board['low-R'])

turn = "X"
for i in range(9):
    printBoard(Board)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    Board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
printBoard(Board)
