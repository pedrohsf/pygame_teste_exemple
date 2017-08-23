#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from Mapa import Mapa, Sqm
from Player import Player
from random import randrange
from WalkPlayer import WalkPlayer, WalkDirection

map_x_sqms_count = 11
map_y_sqms_count = 11

screen_dimension_game = {
    'x' : 32 * map_x_sqms_count,
    'y' : 32 * map_y_sqms_count
}


pygame.init()
font_name = pygame.font.get_default_font()
name_font = pygame.font.SysFont(font_name, 16)


screen = pygame.display.set_mode((screen_dimension_game['x'], screen_dimension_game['y']), 0, 32)


clock = pygame.time.Clock()
mapa = Mapa(map_x_sqms_count,map_y_sqms_count)
player = Player(randrange(0 , map_x_sqms_count ),randrange(0,map_y_sqms_count),'Arrois')


walk_player = WalkPlayer(player, 1)
player_walking = False

def player_walk_for(direction : WalkDirection, speed):
    global walk_player
    try:
        walk_player.speed = speed
        walk_player.set_direction_to_walk(direction)
        walk_player.start()
    except RuntimeError:
        walk_player = WalkPlayer(player,speed)

def get_speed_of_this_sqm(x,y):
    print(mapa.get_string_by_pos(int(x),int(y)))
    return mapa.map_dic[mapa.get_string_by_pos(int(x),int(y))][0].get_speed()


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()



    if not walk_player.is_alive():

        if pressed_keys[K_UP]:
            if (player.pos_y-1 >= 0):
                player_walk_for(WalkDirection.NORTH,
                                get_speed_of_this_sqm(player.pos_x,player.pos_y-1)
                                )
        elif pressed_keys[K_DOWN]:
            if (player.pos_y+1 < map_y_sqms_count):
                player_walk_for(WalkDirection.SOUTH,
                                get_speed_of_this_sqm(player.pos_x,player.pos_y+1)
                                )
        if pressed_keys[K_LEFT]:
            if (player.pos_x - 1 >= 0):
                player_walk_for(WalkDirection.WEST,
                                get_speed_of_this_sqm(player.pos_x-1,player.pos_y)
                                )
        elif pressed_keys[K_RIGHT]:
            if (player.pos_x + 1 < map_x_sqms_count):
                player_walk_for(WalkDirection.EAST,
                                get_speed_of_this_sqm(player.pos_x+1,player.pos_y)
                                )


    for print_map_key , value in mapa.map_dic.items():
        screen.blit( pygame.image.load( value[0].sqms_type[value[0].type_sqm]['surface']).convert_alpha() , (value[0].pos_x * 32 , value[0].pos_y * 32) )

    screen.blit(pygame.image.load(player.player_info['surface']).convert_alpha(),(player.pos_x*32,player.pos_y*32))

    name_text = name_font.render(player.name, 1, (0, 0, 0))

    screen.blit(name_text, (player.pos_x*32, player.pos_y*32 - 10))

    pygame.display.update()
    time_passed = clock.tick(30)

