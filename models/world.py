import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import random
import json
from models.room import Room
from models.objects import Object

class World(object):
    def __init__(self):
         with open("assets/objects.json") as f:
             objects = json.loads(f.read())
         self.all_objects = [Object(*item) for item in objects]
         self.world_size = 4
         self.starting_index = (random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1))

         self.world = [
             [
                 Room("Generic Room", "its a 15 foot by 15 foot by 15 foot box", 4, random.choice(objects))
                 for i in range(self.world_size)
             ]
             for i in range(self.world_size)
         ]

if __name__ == "__main__":
    world = World()
    print(world.world)
