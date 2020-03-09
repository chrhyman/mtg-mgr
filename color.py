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

    def assign_colors(self):
        self.colors = [self.white, self.blue, self.black, self.red, self.green]

    def get_guild(self):
        if not exactly2(self.colors):
            raise RuleError("No guild definition exists for this Color object")
        if self.white:
            if self.blue:
                return AZORIOUS
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
        raise RuleError("No guild assigned.")

    def update(self,
               w=self.white,
               u=self.blue,
               b=self.black,
               r=self.red,
               g=self.green):
        self.__init__(w, u, b, r, g)
