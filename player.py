import pygame
from pygame.locals import *

PLAYER_SIZE = 30 #A constant, for now...

class Player:

    def __init__(self, num, tcolor_main, tcolor_secondary, window, pos, font):
        self.num = num
        self.tcolor_main = tcolor_main
        self.tcolor_secondary = tcolor_secondary
        self.window = window
        self.pos = pos
        self.font = font
        self.render(num, self.tcolor_main, self.tcolor_secondary, self.window, self.pos, self.font)
        
    def render(self, num=None, tcolor_main=None, tcolor_secondary=None, window=None, pos=None, font=None):
        #If any of the above variables are NOT none, replace variable values
        if(num is not None):
            self.num = num
        if(tcolor_main is not None):
            self.tcolor_main = tcolor_main
        if(tcolor_secondary is not None):
            self.tcolor_secondary = tcolor_secondary
        if(window is not None):
            self.window = window
        if(pos is not None):
            self.pos = pos
        if(font is not None):
            self.font = font

        #Draw the player circle
        pygame.draw.circle(self.window, self.tcolor_main, self.pos, PLAYER_SIZE)
        #Draw the number on top of the circle
        pos_mod = [self.pos[0]-20, self.pos[1]-20]
        self.window.blit(self.font.render(str(self.num), False, self.tcolor_secondary, None), pos_mod, None)