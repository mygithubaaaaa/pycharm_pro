import pygame
from pygame import *

pygame.init()
CATONKEYBOARD = USEREVENT + 1
my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
pygame.event.post(my_event)

# 然后获得它
for event in pygame.event.get():
    if event.type == CATONKEYBOARD:
        print(event.message)
