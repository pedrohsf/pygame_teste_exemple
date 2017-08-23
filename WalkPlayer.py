
import Player
from pygame.time import Clock
import threading
from enum import Enum


class WalkDirection(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class WalkPlayer(threading.Thread):
    def __init__(self, player: Player, speed):
        threading.Thread.__init__(self)
        self.player = player
        self.speed = speed
        self.clock = Clock()
    def run(self):

        if  self.direction == WalkDirection.NORTH:
            self.walk_north(self.player.pos_y)
        elif self.direction == WalkDirection.SOUTH:
            self.walk_south(self.player.pos_y)
        elif self.direction == WalkDirection.EAST:
            self.walk_east((self.player.pos_x))
        elif self.direction == WalkDirection.WEST:
            self.walk_west(self.player.pos_x)
        del(self)


    def walk_east(self,start_walk_pos):
        while not (self.player.pos_x == (start_walk_pos + 1)):
            if (start_walk_pos + self.speed/32) < (self.player.pos_x + 1):
                self.player.pos_x += self.speed/32
            else:
                self.player.pos_x = start_walk_pos + 1
            self.clock.tick(30)

    def walk_west(self,start_walk_pos):
        while not (self.player.pos_x == (start_walk_pos - 1)):
            if (start_walk_pos - self.speed/32) > (self.player.pos_x - 1):
                self.player.pos_x -= self.speed/32
            else:
                self.player.pos_x = start_walk_pos - 1
            self.clock.tick(30)

    def walk_south(self,start_walk_pos):
        while not (self.player.pos_y == (start_walk_pos + 1)):
            if (start_walk_pos + self.speed/32) < (self.player.pos_y + 1):
                self.player.pos_y += self.speed/32
            else:
                self.player.pos_y = start_walk_pos + 1
            self.clock.tick(30)


    def walk_north(self,start_walk_pos):
        while not (self.player.pos_y == (start_walk_pos - 1)):
            if (start_walk_pos - self.speed/32) > (self.player.pos_y - 1):
                self.player.pos_y -= self.speed/32
            else:
                self.player.pos_y = start_walk_pos - 1
            self.clock.tick(30)

    def set_direction_to_walk(self, direction : WalkDirection):
        self.direction = direction