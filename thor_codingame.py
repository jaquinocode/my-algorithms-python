import sys
import math


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = None
        self.target_y = None
        self.xy_changes = {
            "N": (0, -1),
            "NE": (1, -1),
            "E": (1, 0),
            "SE": (1, 1),
            "S": (0, 1),
            "SW": (-1, 1),
            "W": (-1, 0),
            "NW": (-1, -1),
        }

    def move(self, dir):
        remaining_energy = int(input())
        print(dir)

        # update position
        x_change, y_change = self.xy_changes[dir]
        self.x += x_change
        self.y += y_change

    # from curr location, return direction where target is, from 8 options: north,
    # northeast, south, etc
    # e.g. returns "NE" if target is NE of curr location, "N" if target directly north
    def general_direction_to_target(self):
        # moves needed to get to target, negative or positive to denote direction
        x_moves_to_target = self.target_x - self.x
        y_moves_to_target = self.target_y - self.y

        general_dir = ""
        if y_moves_to_target > 0:
            general_dir += "S"
        elif y_moves_to_target < 0:
            general_dir += "N"

        if x_moves_to_target > 0:
            general_dir += "E"
        elif x_moves_to_target < 0:
            general_dir += "W"

        return general_dir

    def set_target_loc(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y


light_x, light_y, initial_tx, initial_ty = map(int, input().split())

thor = Character(initial_tx, initial_ty)
thor.set_target_loc(light_x, light_y)
while True:
    dir_to_target = thor.general_direction_to_target()
    thor.move(dir_to_target)
