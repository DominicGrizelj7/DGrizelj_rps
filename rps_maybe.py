# created by Dominic Grizelj

# import libraries: sleep, random integer, and pygame
from time import sleep 
from random import randint
import pygame as pg 
# import operating system
import os

# setup asset folders - images and sounds... path is module and directery name pulls from file (tells where image is)
game_folder = os.path.dirname(__file__)
print(game_folder)

#  game settings
Width = 360
Height = 480
FPS = 30

#  define color (data type)
# RGB: Red Green Blue: All is white: none is black, first is red, second is green, third is blue
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


# init pygame and create a window: init initializes all of it
# too busy copying to take any notes on this:
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((Width, Height))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

global rock_image
global paper_image
global scissors_image
global rock_rect
global paper_rect
global scissors_rect
global mouse_cords 
global choices
global cpu
global cpu_choice

rock_image = pg.image.load(os.path.join(game_folder, 'rock.png')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
choose_fighter = pg.image.load(os.path.join(game_folder, 'choose_fighter.png')).convert()
you_lose = pg.image.load(os.path.join(game_folder, 'you_lose.png')).convert()
rock_rock = pg.image.load(os.path.join(game_folder, 'rock_rock.png')).convert()
paper_paper = pg.image.load(os.path.join(game_folder, 'paper_paper.png')).convert()
scissors_scissors = pg.image.load(os.path.join(game_folder, 'scissors_scissors.png')).convert()
water_gun = pg.image.load(os.path.join(game_folder, 'water_gun.png')).convert()


# # creates transparency 
rock_image.set_colorkey(White)
paper_image.set_colorkey(White)
scissors_image.set_colorkey(White)

# ets geometry of shape
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
scissors_rect = scissors_image.get_rect()
fighter_rect = choose_fighter.get_rect()
lose_rect = you_lose.get_rect()
rock_rock_rect = rock_rock.get_rect()
paper_paper_rect = paper_paper.get_rect()
scissors_scissors_rect = scissors_scissors.get_rect()
water_gun_rect = water_gun.get_rect()


scissors_rect.y = Height/2
rock_rect.x = Width/2
fighter_rect.y=200
fighter_rect.x=100
lose_rect.y=300
lose_rect.x=140
# paper_rect.y = 100 
running = True
while running:
    clock.tick(FPS)
#  this is just saying if you hit the x it quits: If you make running true it will never close
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            #  mousebuttom is when you push down and mouse comes up
        if event.type == pg.MOUSEBUTTONUP:
            # tuple gets position coordinates (x,y)
            # defines mouse cord as the tuple location
            mouse_cords = pg.mouse.get_pos() 

            if rock_rect.collidepoint(mouse_cords):
               print ("you chose Rock")
               running = False


    
            elif paper_rect.collidepoint(mouse_cords):
                print("you chose Paper")
                running = False

            elif scissors_rect.collidepoint(mouse_cords):
                print("you chose Scissors")
                running = False

            # if mouse_coords[0] <= 300 and mouse_coords[1] <= 300:
            # # if mouse_coords == pg.mouse.get_pos():
            #     print("I clicked on the rock...")
            #   if you do not hit thge rock, it will say you missed
            else:
                print("you missed everything")

 


    #  draw
  

    screen.blit(rock_image, rock_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(scissors_image, scissors_rect)
    screen.blit(choose_fighter, fighter_rect)


    



    pg.display.flip()
pg.quit()



game_folder = os.path.dirname(__file__)
print(game_folder)

#  game settings
Width = 360
Height = 480
FPS = 30 
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)


# init pygame and create a window: init initializes all of it
# too busy copying to take any notes on this:
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((Width, Height))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()




from random import randint 

choices = ("rock", "paper", "scissors")   
def cpu_choice():
    return "The computer has chosen " + choices[randint(0,2)]
cpu = cpu_choice
print(cpu_choice())



sleep(0.5)
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # choices = ("rock", "paper", "scissors")   
    # def cpu_choice():
    #     return "The computer has chosen " + choices[randint(0,2)]
    # cpu = cpu_choice


    
        def rps():
            if cpu[0]:
                screen.blit(rock_rock, rock_rock_rect)
                print("hi")
            elif cpu[1]:
                screen.blit(paper_paper, paper_paper_rect)
                print("hi")
            elif cpu[2]:
                screen.blit(scissors_scissors, scissors_scissors_rect)
                print("hi")
    else:
            screen.blit(water_gun, water_gun_rect)
            screen.blit(you_lose, lose_rect)
    # def rps():
    #     if cpu == "rock":
    #         screen.blit(rock_rock, rock_rock_rect)
    #         print("hi")
    #     elif cpu == "paper":
    #         screen.blit(paper_paper, paper_paper_rect)
    #         print("hi")
    #     elif cpu == "scissors":
    #         screen.blit(scissors_scissors, scissors_scissors_rect)
    #     print("hi")

    # def rps():
    #     if cpu == choices[0]:
    #         screen.blit(rock_rock, rock_rock_rect)
    #         print("hi")
    #     elif cpu == choices[1]:
    #         screen.blit(paper_paper, paper_paper_rect)
    #         print("hi")
    #     elif cpu == choices[2]:
    #         screen.blit(scissors_scissors, scissors_scissors_rect)
    #     print("hi")







    pg.display.flip()
pg.quit()


   #     if rock_rect.collidepoint(mouse_cords):
    #         screen.blit(rock_rock, rock_rock_rect)
    # if event.type == pg.MOUSEBUTTONUP:
    #     if paper_rect.collidepoint(mouse_cords):
    #         screen.blit(paper_paper, paper_paper_rect)
    # if event.type == pg.MOUSEBUTTONUP:
    #     if scissors_rect.collidepoint(mouse_cords):
    #         screen.blit(scissors_scissors, scissors_scissors_rect)








