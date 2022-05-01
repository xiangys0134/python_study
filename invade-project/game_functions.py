#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from settings import Settings
from ship import Ship

def check_events():
    '''
    响应按键和鼠标事件
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blime()
    pygame.display.flip()
