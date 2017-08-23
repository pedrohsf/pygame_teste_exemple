

from random import randrange

random_sqm_type = ['grass','water','earth']

class Sqm():

    sqms_type = {
        'grass': {'speed': 4,
                  'surface': 'images_game/sqm_images/grass.png'
                  },
        'water': {'speed': 2,
                  'surface': 'images_game/sqm_images/water.jpg'},
        'earth': {'speed': 8,
                  'surface': 'images_game/sqm_images/earth.png'}
    }

    def __init__(self,pos_x,pos_y,type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type_sqm = type

    def get_speed(self):
        return self.sqms_type[self.type_sqm]['speed']

    def __str__(self):
        return self.type_sqm

class Mapa():

    def __init__(self,max_x,max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.map_dic = {}

        for x in range(max_x):
            for y in range(max_y):
                self.map_dic[self.get_string_by_pos(x,y)] = [Sqm(x,y,random_sqm_type[randrange(0,3)])]


    def print_map(self):
        for x in range(self.max_x):
            for y in range(self.max_y):
                print( self.get_string_by_pos(x,y)+':' + str(self.map_dic[self.get_string_by_pos(x,y)][0])  )


    def get_string_by_pos(self,x,y):
        return str(x) + ',' + str(y)



#print(new_map.map_dic['0,0'])