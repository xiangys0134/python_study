#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    # screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasin')

    #设置背景色
    # bg_color = (230,230,230)
    while True:
        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events()
        #每次循环时都重绘屏幕

        # screen.fill(bg_color)
        # screen.fill(ai_settings.bg_color)
        gf.update_screen(ai_settings,screen,ship)
        # ship.blime()
        #让最近绘制的屏幕可见
        # pygame.display.flip()

run_game()