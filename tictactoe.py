'''
Name: Gregori Jenkins
Date: June 25, 2016
Finished: July 12, 2016
Version 1

This program will allow players to play tictactoe using a GUI interface using
the pygame library.

pygame library - www.wpygame.org
'''

'''import pygame

class Marker(object):
    def __init__(self, marker_type):
        self.marker_type = marker_type'''
        
from tkinter import *
import tkinter.messagebox

WIDTH = 300
HEIGHT = 300 
tk = Tk()
#current_turn = "x"
player = 0
start = 0
board_token = ["9","9","9","9","9","9","9","9","9"]
position_x_dict = {"0":[0,0,100,100,100,0,0,100], "1":[100,0,200,100,200,0,100,100], 
"2":[200,0,300,100,300,0,200,100], "3":[0,100,100,200,100,100,0,200], 
"4":[100,100,200,200,200,100,100,200], "5":[200,100,300,200,300,100,200,200],
"6":[0,200,100,300,100,200,0,300], "7":[100,200,200,300,200,200,100,300],
"8":[200,200,300,300,300,200,200,300]}
position_o_dict = {"0":[0, 2, 100, 100], "1":[100, 2, 200, 100], "2":[200, 2, 300, 100], 
"3":[0, 100, 100, 200], "4":[100, 100, 200, 200], "5":[200, 100, 300, 200]
, "6":[0, 200, 100, 300], "7":[100, 200, 200, 300], "8":[200, 200, 300, 300]}
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()
#create_line - begin_x_coord, begin_y_coord, end_x_coord, end_y_coord
#create_oval - bagin_x_coord, begin_y_coord, end_x_coord, end_y_coord

def draw_x_mark(x_dict, position):
    #position is one of the boxes in string format. top-left is "0"
    #while the bottom right will be "8"
    if test_occupied_space(position):
        canvas.create_line(x_dict[position][0], x_dict[position][1], x_dict[position][2], x_dict[position][3])
        canvas.create_line(x_dict[position][4], x_dict[position][5], x_dict[position][6], x_dict[position][7])
        board_token[int(position)] = "0"
def draw_o_mark(o_dict, position):
    #position is one of the boxes in string format. top-left is "0"
    #while the bottom right will be "8"
    if test_occupied_space(position):
        canvas.create_oval(o_dict[position][0], o_dict[position][1], o_dict[position][2], o_dict[position][3])
        board_token[int(position)] = "1"
def draw_board():
    #global start
    #Create the board in a tk window
    #upper_line
    canvas.create_line(0, 100, 300, 100)
    #lower_line
    canvas.create_line(0, 200, 300, 200)
    #left_line
    canvas.create_line(100, 0, 100, 300)
    #right_line
    canvas.create_line(200, 0, 200, 300)
    canvas.bind("<Button-1>", track_pick)
    #if start == 0:
        #display_instructions()
    #    start = 1
    tk.mainloop()
def test_tie():
    #should send an alert saying that there's been a tie and ask to restart
    for i in range(len(board_token)):
        if int(board_token[i]) == 9:
            #if there's space left on the board, return True
            return True
    #there's no more space on the board
    return False
def test_occupied_space(position):
    #check to ensure that the space is not occupied
    global player
    #print(position)
    #print(board_token[int(position)])
    #print(type(board_token[int(position)]))
    if int(board_token[int(position)]) == 9:
        #if empty, allow the mark to be made
        #print("There's no mark here")    
        return True   
    else:
        #else the position is occupied and it is that player's turn again
        #print("Will not mark here")  
        player = change_turn(player)
        return False    
        #print(player)
def test_for_winner():
    #function simply tests for the eight conditions of winning 
    #by having three symbols in a row or tests for a draw
    #Check for winning xs top-across
    if board_token[0] == "0" and board_token[1] == "0" and board_token[2] == "0": 
        return 0
    #Check for winning xs middle-across
    elif board_token[3] == "0" and board_token[4] == "0" and board_token[5] == "0": 
        return 0
    #Check for winning xs bottom-across
    elif board_token[6] == "0" and board_token[7] == "0" and board_token[8] == "0": 
        return 0
    #Check for winning xs right-down
    elif board_token[0] == "0" and board_token[3] == "0" and board_token[6] == "0": 
        return 0
    #Check for winning xs middle-down
    elif board_token[1] == "0" and board_token[4] == "0" and board_token[7] == "0": 
        return 0
    #Check for winning xs left-down
    elif board_token[2] == "0" and board_token[5] == "0" and board_token[8] == "0": 
        return 0
    #Check for winning xs top-left to bottom-right diagnally
    elif board_token[0] == "0" and board_token[4] == "0" and board_token[8] == "0": 
        return 0
    #Check for winning xs top-right to bottom-left diagnally
    elif board_token[6] == "0" and board_token[4] == "0" and board_token[2] == "0": 
        return 0
    #Check for winning ys middle-across
    elif board_token[3] == "1" and board_token[4] == "1" and board_token[5] == "1": 
        return 1
    #Check for winning ys bottom-across
    elif board_token[6] == "1" and board_token[7] == "1" and board_token[8] == "1": 
        return 1
    #Check for winning ys right-down
    elif board_token[0] == "1" and board_token[3] == "1" and board_token[6] == "1": 
        return 1
    #Check for winning ys middle-down
    elif board_token[1] == "1" and board_token[4] == "1" and board_token[7] == "1": 
        return 1
    #Check for winning ys left-down
    elif board_token[2] == "1" and board_token[5] == "1" and board_token[8] == "1": 
        return 1
    #Check for winning ys top-left to bottom-right diagnally
    elif board_token[0] == "1" and board_token[4] == "1" and board_token[8] == "1": 
        return 1
    #Check for winning ys top-right to bottom-left diagnally
    elif board_token[6] == "1" and board_token[4] == "1" and board_token[2] == "1": 
        return 1
    #Check for winning ys top-across
    elif board_token[0] == "1" and board_token[1] == "1" and board_token[2] == "1": 
        return 1
    else:
        return 3
def quit():
    tk.destroy()
def clear_board():
    #clears the board so that a new game can be started.
    global board_token
    canvas.delete("all")
    board_token = ["9","9","9","9","9","9","9","9","9"]
    draw_board()
def display_instructions():
    #will display instructions in a new window
    instructions = "The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled. --web.cecs.pdx.edu/~bart/cs541-fall2001/homework/tictactoe-rules.html"
    tkinter.messagebox.showinfo("Instructions", instructions)
def display_winner(winner):
    #creates popup message declaring the winner
    tkinter.messagebox.showinfo("Winner", "The winner is " + winner)
    cont = tkinter.messagebox.askyesno("Game Over", "Continue?")
    if cont == False:
        quit()
    else:
        #clear the board and restart the game. Will leave to code at a later time
        clear_board()
def display_tie():
    #creates popup message declaring that there has been a tie
    tkinter.messagebox.showinfo("Tie", "The game has ended in a tie!")
    cont = tkinter.messagebox.askyesno("Game Over", "Continue?")
    if cont == False:
        quit()
    else:
        #clear the board and restart the game. Will leave to code at a later time
        clear_board()
def change_turn(player):
    #Change the current turn
    if player == 0:
        return 1
    else:
        return 0
def track_pick(event):
    #determines the area picked and returns the area integer
    global player
    if player == 0:
        if event.x > 0 and event.x < 100 and event.y > 0 and event.y < 100:
            draw_x_mark(position_x_dict, "0")
        elif event.x > 100 and event.x < 200 and event.y > 0 and event.y < 100:
            draw_x_mark(position_x_dict, "1")
        elif event.x > 200 and event.x < 300 and event.y > 0 and event.y < 100:
            draw_x_mark(position_x_dict, "2")
        elif event.x > 0 and event.x < 100 and event.y > 100 and event.y < 200:
            draw_x_mark(position_x_dict, "3")
        elif event.x > 100 and event.x < 200 and event.y > 100 and event.y < 200:
            draw_x_mark(position_x_dict, "4")
        elif event.x > 200 and event.x < 300 and event.y > 100 and event.y < 200:
            draw_x_mark(position_x_dict, "5")
        elif event.x > 0 and event.x < 100 and event.y > 200 and event.y < 300:
            draw_x_mark(position_x_dict, "6")
        elif event.x > 100 and event.x < 200 and event.y > 200 and event.y < 300:
            draw_x_mark(position_x_dict, "7")
        elif event.x > 200 and event.x < 300 and event.y > 200 and event.y < 300:
            draw_x_mark(position_x_dict, "8")
    elif player == 1:
        if event.x > 0 and event.x < 100 and event.y > 0 and event.y < 100:
            draw_o_mark(position_o_dict, "0")
        elif event.x > 100 and event.x < 200 and event.y > 0 and event.y < 100:
            draw_o_mark(position_o_dict, "1")
        elif event.x > 200 and event.x < 300 and event.y > 0 and event.y < 100:
            draw_o_mark(position_o_dict, "2")
        elif event.x > 0 and event.x < 100 and event.y > 100 and event.y < 200:
            draw_o_mark(position_o_dict, "3")
        elif event.x > 100 and event.x < 200 and event.y > 100 and event.y < 200:
            draw_o_mark(position_o_dict, "4")
        elif event.x > 200 and event.x < 300 and event.y > 100 and event.y < 200:
            draw_o_mark(position_o_dict, "5")
        elif event.x > 0 and event.x < 100 and event.y > 200 and event.y < 300:
            draw_o_mark(position_o_dict, "6")
        elif event.x > 100 and event.x < 200 and event.y > 200 and event.y < 300:
            draw_o_mark(position_o_dict, "7")
        elif event.x > 200 and event.x < 300 and event.y > 200 and event.y < 300:
            draw_o_mark(position_o_dict, "8")
    if test_for_winner() == 0:
        #print("X is the winner")
        display_winner("X")
    elif test_for_winner() == 1:
        #print("O is the winner")
        display_winner("O")
    elif not test_tie():
        display_tie()
    player = change_turn(player)
draw_board()

