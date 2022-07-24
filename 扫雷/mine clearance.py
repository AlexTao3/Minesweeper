import pygame
import time
import random
import sys

pygame.init()

white = (255,255,255)
black = (0,0,0)
purple = (120,65,255)
bluegreen = (40,164,159)
grey = (192,192,192)
light_grey = (214,214,214)

red = (170,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

display_width = 1200
display_height = 700

clock = pygame.time.Clock()

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mine clearance')

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)



def buttons(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Quit":
                pygame.quit()
                sys.exit()
                quit()

            if action == "Controls":
                game_controls()

            if action == "Play":
                game_control()

            if action == "Main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_buttons(text,black,x,y,width,height)

def game_controls():

    
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()


        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -100,
                          "large")

        message_to_screen("Click Right to put flag on mine",
                         black,
                         -30)

        message_to_screen("Click left to show whether a mine",
                          black,
                          10)
        
        message_to_screen("Pause: P",
                          black,
                          50)
        
        message_to_screen("Good luck!",
                          black,
                          90)

        buttons("Play", 300,500,100,50, grey, light_grey, action="Play")
        buttons("Main", 550,500,100,50, grey, light_grey, action="Main")
        buttons("Quit", 800,500,100,50, grey, light_grey, action="Quit")
        
      
        pygame.display.update()
        clock.tick(15)

def game_intro():

    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Mine Clearance!",
                          green,
                          -100,
                          "large")

        message_to_screen("The objective is to find mine",
                         black,
                         -30)

        message_to_screen("Don't click mine",
                          black,
                          10)
        
        message_to_screen("Find out all the mine and you win!",
                          black,
                          50)
        
        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          90)

        buttons("Play", 300,500,100,50, grey, light_grey, action="Play")
        buttons("Controls", 550,500,100,50, grey, light_grey, action="Controls")
        buttons("Quit", 800,500,100,50, grey, light_grey, action="Quit")
        
      
        pygame.display.update()
        clock.tick(15)

def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_buttons(msg, color, buttonsx, buttonsy, buttonswidth, buttonsheight, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = ((buttonsx+(buttonswidth/2)), buttonsy+(buttonsheight/2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)



def gameLoop():
    gameExit = False
    gameOver = False

    while not gameExit:
        space9X = display_width* 0.9
        space9Y = display_height * 0.9

        pygame.display.update()
    pygame.quit()
    sys.exit()
    quit()   

game_intro()
gameLoop()


























