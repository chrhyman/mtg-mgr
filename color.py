from const import *
from util import RuleError

class Color:
    WHITE = "white"
    BLUE = "blue"
    BLACK = "black"
    RED = "red"
    GREEN = "green"
    COLORS = [WHITE, BLUE, BLACK, RED, GREEN]

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
            self.monocolor = Color.COLORS[self.colors.index(True)]
        else:
            self.monocolored = False
            self.monocolor = None
        if self.colors.count(True) > 1:
            self.multicolored = True
        else:
            self.multicolored = False
        if self.colors.count(True) == 2:
            self.colorpair = True
            self.guild = Guild(self)
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

    def update(self, w=None, u=None, b=None, r=None, g=None):
        w2 = w if w is not None else self.white
        u2 = u if u is not None else self.blue
        b2 = b if b is not None else self.black
        r2 = r if r is not None else self.red
        g2 = g if g is not None else self.green
        self.__init__(w2, u2, b2, r2, g2)

class Guild:
    AZORIUS = "Azorius"
    BOROS = "Boros"
    DIMIR = "Dimir"
    GOLGARI = "Golgari"
    GRUUL = "Gruul"
    IZZET = "Izzet"
    ORZHOV = "Orzhov"
    RAKDOS = "Rakdos"
    SELESNYA = "Selesnya"
    SIMIC = "Simic"
    GUILDS = [AZORIUS, BOROS, DIMIR, GOLGARI, GRUUL,
        IZZET, ORZHOV, RAKDOS, SELESNYA, SIMIC]

    def __init__(self, color_obj):
        if color_obj.colors.count(True) != 2:
            err = "No guild definition exists for this Color object: "
            err += str(color_obj.__dict__)
            raise RuleError(err)
        self.color = color_obj
        self.guild = self.get_guild()

    def __str__(self):
        return self.guild

    def get_guild(self):
        if self.color.white:
            if self.color.blue:
                return Guild.AZORIUS
            elif self.color.black:
                return Guild.ORZHOV
            elif self.color.red:
                return Guild.BOROS
            elif self.color.green:
                return Guild.SELESNYA
        elif self.color.blue:
            if self.color.black:
                return Guild.DIMIR
            elif self.color.red:
                return Guild.IZZET
            elif self.color.green:
                return Guild.SIMIC
        elif self.color.black:
            if self.color.red:
                return Guild.RAKDOS
            elif self.color.green:
                return Guild.GOLGARI
        elif self.color.red:
            if self.color.green:
                return Guild.GRUUL
