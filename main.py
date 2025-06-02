import pygame
from pygame.locals import *
from player import Player

#Initiate pygame
pygame.init()
#Set a window of size 1024x768
window = pygame.display.set_mode((1024,768))
#Make 'background' of screen green for field
window.fill((0,255,0))
#Set up default font
Font = pygame.font.SysFont('timesnewroman',40)

#Draw a 'player' by using the "Player" class
#   For player's init function: def __init__(num, tcolor_main, tcolor_secondary, window, init_pos, font):
team1_colors = [(255,0,0),(0,0,0)]

pygame.display.update()
player1 = Player(55, team1_colors[0], team1_colors[1], window, [400,300], Font)
players = []
players.append(player1)

#Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Render all players
    for player in players:
        player.render()

    pygame.display.update()
pygame.quit()