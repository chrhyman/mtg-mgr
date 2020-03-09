from const import *
from util import RuleError

class Color:
    def __init__(self, w=False, u=False, b=False, r=False, g=False):
        self.white = w
        self.blue = u
        self.black = b
        self.red = r
        self.green = g
        self.assign_colors()
        if not any(self.colors):
            self.colorless = True
        else:
            self.colorless = False
        if self.colors.count(True) == 1:
            self.monocolored = True
        else:
            self.monocolored = False
        if self.colors.count(True) > 1:
            self.multicolored = True
        else:
            self.multicolored = False
        if self.colors.count(True) == 2:
            self.colorpair = True
            self.guild = self.get_guild()
        else:
            self.colorpair = False
            self.guild = None
        # if count is 3 handle shards and wedges
        # together or separate?
        # if count is 4 handle 4-color
        if all(self.colors):
            self.fivecolor = True
        else:
            self.fivecolor = False

    def assign_colors(self):
        self.colors = [self.white, self.blue, self.black, self.red, self.green]

    def get_guild(self):
        if self.colors.count(True) != 2:
            raise RuleError("No guild definition exists for this Color object")
        if self.white:
            if self.blue:
                return AZORIUS
            elif self.black:
                return ORZHOV
            elif self.red:
                return BOROS
            elif self.green:
                return SELESNYA
        elif self.blue:
            if self.black:
                return DIMIR
            elif self.red:
                return IZZET
            elif self.green:
                return SIMIC
        elif self.black:
            if self.red:
                return RAKDOS
            elif self.green:
                return GOLGARI
        elif self.red:
            if self.green:
                return GRUUL
        raise RuleError("No guild returned. Dumping object data: " + str(self.__dict__))

    def update(self, w=None, u=None, b=None, r=None, g=None):
        w2 = w if w is not None else self.white
        u2 = u if u is not None else self.blue
        b2 = b if b is not None else self.black
        r2 = r if r is not None else self.red
        g2 = g if g is not None else self.green
        self.__init__(w2, u2, b2, r2, g2)
