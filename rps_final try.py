# File created by Dominic Grizelj
# 
 
# import libraries with specific fucntions they can do

from time import sleep

from random import randint 

import pygame as pg

import os
# setup asset folders - images and sounds... path is module and directery name pulls from file (tells where image is)
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings that give the size of pop up screen and the frames per second (30)
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
# tuples are like x y varaibles
#  define color (data type)
# RGB: Red Green Blue: All is white: none is black, first is red, second is green, third is blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# these are the chioecs for upcoming variavles
choices = ["rock", "paper", "scissors"]
# this defines draw text. First it defines the color, then coordinates. It then has more code that allows it to actually print on screen with a font of your choosing
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('aleo')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
# This defines cpu choices, which assigns certain integers (0-2) with the choices (rock paper scissors) above and uses the random integer library to randomly decide a choice
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice
# init pygame and create a window: init initializes all of it
pg.init()
pg.mixer.init()

# This defines all of the images with certain names, like "rock" and pulls them from my other fules. It also gets geometry of shape, and allows it to work/be visable on screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()
rock = pg.image.load(os.path.join(game_folder, 'rock.png')).convert()
rock_rect = rock.get_rect()
cpu_rock = pg.image.load(os.path.join(game_folder, 'rock_rock.png')).convert()
cpu_rock_rect = cpu_rock.get_rect()
cpu_paper = pg.image.load(os.path.join(game_folder, 'paper_paper.png')).convert()
cpu_paper_rect = cpu_paper.get_rect()
cpu_scissors = pg.image.load(os.path.join(game_folder, 'scissors_scissors.png')).convert()
cpu_scissors_rect = cpu_scissors.get_rect()
paper = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
paper_rect = paper.get_rect()
scissors = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissors_rect = scissors.get_rect()

# starting screen is running
start_screen = True
# This defines player_choiec and cpu_choice
player_choice = ""
cpu_choice = ""
# The code is now running  
running = True

while running:
    clock.tick(FPS)
    #  pretty much means that if use clicks the red x, the program closes
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # Essentially says that if you hit the spacebar (but we could also change it to any key or clicking with the mouse or finger) that the starting screen is false, so it goes aways and moves on to the next commands
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                start_screen = False
        # This says when you click down and the mouse goes up, the computer finds the specific spot/coordinates of the mouse
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()

            # if the mouse is on the rock image while clicking, it will define player choices as "rock"... also deines cpu choice as cpu random chioce
            if rock_rect.collidepoint(mouse_coords):
                print("you clicked on rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            # if the mouse is on the paper image while clicking, it will define player choices as "paper"... also deines cpu choice as cpu random chioce
            elif paper_rect.collidepoint(mouse_coords):
                print("you clicked on paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            # if the mouse is on the scissors image while clicking, it will define player choices as "scissors"... also deines cpu choice as cpu random chioce
            elif scissors_rect.collidepoint(mouse_coords):
                print("you clicked on scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()      
            # if the mouse is not on anything above (rock paper scissors image) while clicked, it will print you missed everything in the terminal            
            else:
                print("you missed everything")
    
    
    

    ############ draw ###################
    # makes screen black
    screen.fill(BLACK)

    # This sets the start screen to running which putting the text define above with certain words, color, and position
    if start_screen == True:
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)

    # allows player to choose rock paper or scissors
    # It draws the images defined above at certain specified locations
    if not start_screen and player_choice == "":
        rock_rect.x = 50
        paper_rect.x = 350
        scissors_rect.x = 550
        screen.blit(scissors, scissors_rect)
        screen.blit(paper, paper_rect)
        screen.blit(rock, rock_rect)

    # Essentially what all of these lines are setting the user choice based on the image the user clicked previously. It then draws that specific image under a certain location
    # It then takes the randomized computer choice, and draws a seperate image of its choice at a certain location
    # It then declares if the user won or lost to the computer based on the combination of choices (paper beats rock, scissors beats paper, rock beats scissors etc..), and uses the earlier draw text function to declare the winner at a certain loctaion
    # It also uses the draw text function to print and label the computer choice and the user choice to make it clear which is which
    # Finally, It also includes an explanation for the loss, win, or tie if it is not clear by saying things like "paper beats rock" or "rock ties with paper"
    # By the way, I felt it would be repetitive if I put all of this text above each scenario... hope this is ok
    if player_choice == "rock":
        if cpu_choice == "rock":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            cpu_rock_rect.x = 500
            screen.blit(rock, rock_rect)
            screen.blit(cpu_rock, cpu_rock_rect)
            draw_text("You tied", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("rock ties with rock", 22, WHITE, WIDTH/2, HEIGHT/1.5)
    if player_choice == "rock":
        if cpu_choice == "paper":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            cpu_paper_rect.x = 500
            screen.blit(rock, rock_rect)
            screen.blit(cpu_paper, cpu_paper_rect)
            draw_text("You Lose ;(", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("rock loses to paper", 22, WHITE, WIDTH/2, HEIGHT/1.5)
    if player_choice == "rock":
        if cpu_choice == "scissors":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            cpu_scissors_rect.x = 500
            screen.blit(rock, rock_rect)
            screen.blit(cpu_scissors, cpu_scissors_rect)
            draw_text("You Win :D", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("rock beats scissors", 22, WHITE, WIDTH/2, HEIGHT/1.5)
    if player_choice == "paper":
        if cpu_choice == "rock":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            paper_rect.x = 100
            cpu_rock_rect.x = 500
            screen.blit(paper, paper_rect)
            screen.blit(cpu_rock, cpu_rock_rect)
            draw_text("You Win :D", 22, WHITE, WIDTH/2, HEIGHT/10)
            draw_text("paper beats rock", 22, WHITE, WIDTH/2, HEIGHT/1.5)

    if player_choice == "paper":
        if cpu_choice == "paper":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            draw_text("paper ties with paper", 22, WHITE, WIDTH/2, HEIGHT/1.5)
            paper_rect.x = 100
            cpu_paper_rect.x = 500
            screen.blit(paper, paper_rect)
            screen.blit(cpu_paper, cpu_paper_rect)
            draw_text("You Tied", 22, WHITE, WIDTH/2, HEIGHT/10)

    if player_choice == "paper":
        if cpu_choice == "scissors":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            draw_text("paper loses to sicssors", 22, WHITE, WIDTH/2, HEIGHT/1.5)
            paper_rect.x = 100
            cpu_scissors_rect.x = 500
            screen.blit(paper, paper_rect)
            screen.blit(cpu_scissors, cpu_scissors_rect)
            draw_text("You Lose ;(", 22, WHITE, WIDTH/2, HEIGHT/10)
    if player_choice == "scissors":
        if cpu_choice == "rock":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            draw_text("scissors loses to rock", 22, WHITE, WIDTH/2, HEIGHT/1.5)
            scissors_rect.x = 100
            cpu_rock_rect.x = 500
            screen.blit(scissors, scissors_rect)
            screen.blit(cpu_rock, cpu_rock_rect)
            draw_text("You Lose ;(", 22, WHITE, WIDTH/2, HEIGHT/10)
    if player_choice == "scissors":
        if cpu_choice == "paper":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            draw_text("scissors beats paper", 22, WHITE, WIDTH/2, HEIGHT/1.5)
            scissors_rect.x = 100
            cpu_paper_rect.x = 500
            screen.blit(scissors, scissors_rect)
            screen.blit(cpu_paper, cpu_paper_rect)
            draw_text("You Win :D", 22, WHITE, WIDTH/2, HEIGHT/10)
    if player_choice == "scissors":
        if cpu_choice == "scissors":
            draw_text("Computer's choice", 22, WHITE, WIDTH/1.4, HEIGHT/2)
            draw_text("Your Choice", 22, WHITE, WIDTH/4, HEIGHT/2)
            draw_text("scissors ties with scissors", 22, WHITE, WIDTH/2, HEIGHT/1.5)
            scissors_rect.x = 100
            cpu_scissors_rect.x = 500
            screen.blit(scissors, scissors_rect)
            screen.blit(cpu_scissors, cpu_scissors_rect)
            draw_text("You Tied", 22, WHITE, WIDTH/2, HEIGHT/10)

# once the user hits red x, the program quits
    pg.display.flip()

pg.quit()





