import random
import sys
import pygame
import pygame.locals
FPS=32
screenwidth=289
screenheight=511
screen=pygame.display.set_mode((screenwidth,screenheight))
groundy=screenheight*0.8
game_sprites={}
game_sound={}
player='C:\Users\hp\Downloads\flappy bird\bird.jpg'
background='C:\Users\hp\Downloads\flappy bird\background.jpg'
pipe='C:\Users\hp\Downloads\flappy bird\download.png'
#mainloop
if __name__=='__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    game_sprites["numbers"]=(
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\0.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\1.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\2.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\3.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\4.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\5.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\6.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\7.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\8.png').convert_alpha(),
    pygame.image.load('C:\Users\hp\Downloads\flappy bird\9.png').convert_alpha()
)
    game_sprites["message"]=(pygame.image.load("C:\Users\hp\Downloads\flappy bird\message.png").convert_alpha()
    game_sprites["base"]=(pygame.image.load("C:\Users\hp\Downloads\flappy bird\message.png").convert_alpha()


