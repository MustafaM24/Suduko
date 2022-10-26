import random
from typing import Text
import pygame
pygame.font.init() 
from pygame import mixer
import os

#

clock = pygame.time.Clock()

# main_window

screen = pygame.display.set_mode((1000, 700)) 

# launch page

pygame.display.set_caption("SUDOKU") 
background = pygame.image.load("sudoku.jpg")
lst = []
def settable(lst):
    initial_b = lst

    board = [[] for i in range(len(initial_b[0]))]
    for i in range(len(initial_b[0])):
        for j in range(len(initial_b)):
            board[i].append(initial_b[j][i])
    return board

# functions

#def sound_display():
#    # initialize
#    pygame.mixer.pre_init()
#    pygame.mixer.init()
#    # start playing the background music
#    pygame.mixer.music.load('mustafa_music.mp3')
#    pygame.mixer.music.set_volume(0.8)
#    pygame.mixer.music.play(loops=-1)
#    pygame.event.wait()
#sound_display()


def boxes(): 
    for i in range(2): 
        pygame.draw.line(screen, (255, 0, 0), (x_axis * (500/9)-3+30, (y_axis + i)*(500/9)+30), (x_axis * (500/9) + (500/9) + 3+30, (y_axis + i)*(500/9)+30), 7) 
        pygame.draw.line(screen, (255, 0, 0), ( (x_axis + i)* (500/9)+30, y_axis * (500/9)+30 ), ((x_axis + i) * (500/9)+30, y_axis * (500/9) + (500/9)+30), 7) 

def board_maker(): 
    for i in range (9): 
        for j in range (9):
            if board[i][j] != 0: 

#pre given num
                screen.blit(pygame.font.SysFont("Times New Roman", 35) .render(str(board[i][j]), 1, (0, 0, 0)), (i * (500/9) + 15+30, j * (500/9) + 15+30)) 


#line draw
    count = 0
    a = (500/9)
    for i in range(10):
        if count % 3 == 0 and i != 0 and i != 9:
            count += 1 
            widthL = 5
        else: 
            count += 1
            widthL = 2
        pygame.draw.line(screen, (0, 0, 0), (30, i*a+30), (530, i*a+30), widthL) 
        pygame.draw.line(screen, (0, 0, 0), (i*a+30, 30), (i*a+30, 530), widthL)
    return board	
   
#intro screen

def start_game():
    global game
    game = True
    screen.blit(background, (0,0))
    greet = pygame.font.SysFont("monsterret", 60).render('SUDUKO', True, (0,0,0))
    screen.blit(greet, [418,250])
    instructions = pygame.font.SysFont("monsterret", 30).render('Press Any Key To Enter', True, (0,0,0))
    screen.blit(instructions, [390,300])
    pygame.display.update()
    # global game
    # game = True
    # screen.blit(background, (0,0))
    # greet = pygame.font.SysFont("Times New Roman", 60).render('SUDUKO', True, (0,0,0))
    # screen.blit(greet, [350,250])
    # instructions = pygame.font.SysFont("Times New Roman", 30).render('Press Any Key To Enter', True, (0,0,0))
    # screen.blit(instructions, [335,360])
    # pygame.display.update()
	# time duration of splash screen
    clock.tick(15)
    delay = True
    while delay:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                game = True
                delay = False
            if event.type == pygame.QUIT: 
                game = False
                delay = False

# levels screen
 
def levels():
    global game
    game = True
    screen.blit(background, (0,0))
    greet = pygame.font.SysFont("monsterret", 60).render('SUDUKO', True, (0,0,0))
    screen.blit(greet, [418,250])
    level = pygame.font.SysFont("monsterret", 30).render('Press 1 to Start Level 1', True, (0,0,0))
    level2 = pygame.font.SysFont("monsterret", 30).render('Press 2 to Start Level 2', True, (0,0,0))
    level3 = pygame.font.SysFont("monsterret", 30).render('Press 3 to Start Level 3', True, (0,0,0))
    screen.blit(level, [390,350])
    screen.blit(level2, [390,400])
    screen.blit(level3, [390,450])
    pygame.display.update()
	# time duration of splash screen
    clock.tick(15)
    delay = True
    while delay:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game = False	
                delay = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    return 1
                if event.key == pygame.K_2: 
                    return 2    
                if event.key == pygame.K_3:
                    return 3

# row and column checker

def row_column_checker(board, i, j, test_val):
    subg_1 = i//3 * 3
    subg_2 = j//3 * 3
    for k in range(9): 
        col = board[i][k]
        row = board[k][j]
        if col== test_val: 
            return False
        if row== test_val: 
            return False
    for i in range(subg_1, subg_1 + 3): 
        for j in range (subg_2, subg_2 + 3):
            boardLocation =  board[i][j]
            if boardLocation== test_val: 
                return False
            else:
                return True

# input
 
def valid_option():
    global userInput
    if userInput != 0:             
        inputVal = pygame.font.SysFont("monsterret", 35).render(str(userInput), 1, (0, 0, 0))
        screen.blit(inputVal, (x_axis * 500/9 + 45, y_axis * 500/9 + 45)) 
        if row_column_checker(board, int(x_axis), int(y_axis), userInput)== True:
            board[int(x_axis)][int(y_axis)]= userInput
        else: 
            board[int(x_axis)][int(y_axis)]= 0
    userInput = 0

# # win loss
# def win():
#     global game
#     game = True
#     screen.blit(background, (0,0))
#     greet = pygame.font.SysFont("monsterret", 60).render('SUDUKO', True, (0,0,0))
#     screen.blit(greet, [418,250])
#     Win = pygame.font.SysFont("monsterret", 30).render('You Win!', True, (0,0,0))
#     #Loss = pygame.font.SysFont("monsterret", 30).render('You Lost, Try Again!', True, (0,0,0))
#     screen.blit(Win, [390,350])
#     #screen.blit(Loss, [390,400])
#     pygame.display.update()
# 	# time duration of splash screen
#     clock.tick(15)
#     delay = True

# def loss():
#     global game
#     game = True
#     screen.blit(background, (0,0))
#     greet = pygame.font.SysFont("monsterret", 60).render('SUDUKO', True, (0,0,0))
#     screen.blit(greet, [418,250])
#     #Win = pygame.font.SysFont("monsterret", 30).render('You Win!', True, (0,0,0))
#     Loss = pygame.font.SysFont("monsterret", 30).render('You Lost, Try Again!', True, (0,0,0))
#     #screen.blit(Win, [390,350])
#     screen.blit(Loss, [390,400])
#     pygame.display.update()
# 	# time duration of splash screen
#     clock.tick(15)
#     delay = True

# check ans
# def check():
#     test_board = board
#     board = settable(lst)
#     board_maker()
#     auto_solver_algorithm(board, 0, 0)
#     if test_board == board:
#         win()
#     else:
#         loss()


# algorithm to solve suduko table

def auto_solver_algorithm(board, i, j): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            os._exit(1)
    while board[i][j]!= 0: 
        if i < (len(board)-1): 
            i+= 1
        elif i == (len(board)-1) and j < (len(board)-1): 
            i = 0
            j+= 1
        elif i == (len(board)-1) and j == (len(board)-1): 
            return True
    pygame.event.pump()     
    for boardPos in range(1, 10): 
        if row_column_checker(board, i, j, boardPos)== True: 
            board[i][j]= boardPos
            screen.blit(background, (0,0))
            solving = pygame.font.SysFont("Times New Roman", 50).render('Backtracking', True, (0,0,0))
            screen.blit(solving, [540,60])
            board_maker() 
            boxes() 
            pygame.display.update() 
            pygame.time.delay(20) 
            if auto_solver_algorithm(board, i, j)== True: 
                return True
            else: 
                board[i][j]= 0
            screen.blit(background, (0,0))
            solving = pygame.font.SysFont("Times New Roman", 50).render('Backtracking', True, (0,0,0))
            screen.blit(solving, [540,60])
            board_maker() 
            boxes() 
            pygame.display.update() 
            pygame.time.delay(50)    
    return False

x_axis = 0
y_axis = 0

# main game run code
# val is user input
Num = 0
start_game()
Num = levels()
if Num == 1:
    lst = [
            [3, 0, 5, 4, 0, 2, 0, 6, 0], 
            [4, 9, 0, 7, 6, 0, 1, 0, 8], 
            [6, 0, 0, 1, 0, 3, 2, 4, 5], 
            [0, 0, 3, 9, 0, 0, 5, 8, 0], 
            [9, 6, 0, 0, 5, 8, 7, 0, 3], 
            [0, 8, 1, 3, 0, 4, 0, 9, 2], 
            [0, 5, 0, 6, 0, 1, 4, 0, 0], 
            [2, 0, 0, 5, 4, 9, 0, 7, 0], 
            [1, 4, 9, 0, 0, 7, 3, 0, 6]
        ]
elif Num == 2:
    lst = [
            [0, 0, 5, 2, 6, 0, 7, 0, 1], 
            [6, 8, 0, 0, 7, 0, 0, 9, 0], 
            [1, 9, 0, 0, 0, 4, 5, 0, 0], 
            [8, 2, 0, 1, 0, 0, 0, 4, 0], 
            [0, 0, 4, 6, 0, 2, 9, 0, 0], 
            [0, 5, 0, 0, 0, 3, 0, 2, 8], 
            [0, 0, 9, 3, 0, 0, 0, 7, 4], 
            [0, 4, 0, 0, 5, 0, 0, 3, 6], 
            [7, 6, 3, 0, 1, 8, 2, 0, 9]
        ]
else:
    lst = [ 
            [7, 8, 0, 4, 0, 0, 1, 2, 0], 
            [6, 0, 0, 0, 7, 5, 0, 0, 9], 
            [0, 0, 0, 6, 0, 1, 0, 7, 8], 
            [0, 0, 7, 0, 4, 0, 2, 6, 0], 
            [0, 0, 1, 0, 5, 0, 9, 3, 0], 
            [9, 0, 4, 0, 6, 0, 0, 0, 5], 
            [0, 7, 0, 3, 0, 0, 0, 1, 2], 
            [1, 2, 0, 0, 0, 7, 4, 0, 0], 
            [0, 4, 9, 2, 0, 6, 0, 0, 7] 
        ]
board = settable(lst)
userInput = 0
boxSelected = False
while game == True: 
	# background color 
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    instructions = pygame.font.SysFont("monsterret", 37).render('Instructions:', True, (0,0,0))
    instructions1 = pygame.font.SysFont("monsterret", 30).render('the values you input can not already exist in that row, column or subgrid', True, (0,0,0))
    instructions2 = pygame.font.SysFont("monsterret", 60).render("SUDOKU", True, (0,0,0))
    instructions3 = pygame.font.SysFont("monsterret", 30).render("Press 'R' to Restart", True, (0,0,0))
    instructions4 = pygame.font.SysFont("monsterret", 30).render("Press 'S' to see the Answers", True, (0,0,0))
    instructions5 = pygame.font.SysFont("monsterret", 30).render("Press 'X' to End Game", True, (0,0,0))
    #instructions6 = pygame.font.SysFont("monsterret", 30).render("Press 'C' to Check", True, (0,0,0))
    screen.blit(instructions,  [60,570]) 
    screen.blit(instructions1, [90,600])
    screen.blit(instructions2, [540,70]) 
    screen.blit(instructions3, [540,180]) 
    screen.blit(instructions4, [540,220]) 
    screen.blit(instructions5, [540,260]) 
    #screen.blit(instructions6, [540,280]) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game = False	 
        if event.type == pygame.KEYDOWN:
            boxSelected = True
            if event.key == pygame.K_LEFT:
                x_axis = x_axis - 1
            if event.key == pygame.K_RIGHT:
                x_axis = x_axis + 1
            if event.key == pygame.K_UP:
                y_axis = y_axis - 1
            if event.key == pygame.K_DOWN:
                y_axis = y_axis + 1
            if event.key == pygame.K_1: 
                userInput = 1
            if event.key == pygame.K_2: 
                userInput = 2    
            if event.key == pygame.K_3:
                userInput = 3
            if event.key == pygame.K_4: 
                userInput = 4
            if event.key == pygame.K_5: 
                userInput = 5
            if event.key == pygame.K_6: 
                userInput = 6 
            if event.key == pygame.K_7: 
                userInput = 7
            if event.key == pygame.K_8: 
                userInput = 8
            if event.key == pygame.K_9: 
                userInput = 9 
            if event.key == pygame.K_x:
                os._exit(1) 
            #if event.key == pygame.K_c:
            #    check()
            if event.key == pygame.K_r:
                board = settable(lst)
                board_maker()
            if event.key == pygame.K_s:
                board = settable(lst)
                board_maker()
                auto_solver_algorithm(board, 0, 0)
    board_maker() 
    
    if userInput != 0:
        valid_option()
        
    if boxSelected:
        boxes()
    pygame.display.update()  
pygame.quit()	 
