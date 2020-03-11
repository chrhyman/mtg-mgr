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
        self.colors = [w, u, b, r, g]
        color_count = self.colors.count(True)

        if color_count == 0:
            self.colorless = True
        else:
            self.colorless = False
        if color_count == 1:
            self.monocolored = True
            self.monocolor = Color.COLORS[self.colors.index(True)]
        else:
            self.monocolored = False
            self.monocolor = None
        if color_count > 1:
            self.multicolored = True
            self.multi = Multicolor(self)
        else:
            self.multicolored = False
            self.multi = None

        if color_count == 2:
            self.colorpair = True
            self.guild = self.multi.name
        else:
            self.colorpair = False
            self.guild = None
        if color_count == 3:
            self.tricolored = True
            self.triname = self.multi.name
            self.tritype = self.multi.type
        else:
            self.tricolored = False
            self.triname = None
        if color_count == 4:
            self.fourcolor = True
            self.fourname = self.multi.name
            self.fourtype = self.multi.type
        else:
            self.fourcolor = False
            self.fourname = None
        if color_count == 5:
            self.fivecolor = True
        else:
            self.fivecolor = False

    def __str__(self):
        return str(self.__dict__)

    def update(self, w=None, u=None, b=None, r=None, g=None):
        w2 = w if w is not None else self.white
        u2 = u if u is not None else self.blue
        b2 = b if b is not None else self.black
        r2 = r if r is not None else self.red
        g2 = g if g is not None else self.green
        self.__init__(w2, u2, b2, r2, g2)

class Multicolor:
    GUILD = "guild"
    SHARD = "shard"
    WEDGE = "wedge"
    FOURC = "four-color"
    FIVEC = "five-color"
    def __init__(self, color_obj):
        self.color = color_obj
        color_count = self.color.colors.count(True)
        if color_count <= 1:
            raise RuleError(
                "arg:color_obj isn't a valid Multicolor object. Dumping data: "
                + str(self.color.__dict__))
        elif color_count == 2:
            self.name = self.get_guild()
            self.type = Multicolor.GUILD

    def __str__(self):
        if self.name:
            return self.name
        return "None"

    def get_guild(self):
        if self.color.white:
            if self.color.blue:
                return AZORIUS
            elif self.color.black:
                return ORZHOV
            elif self.color.red:
                return BOROS
            elif self.color.green:
                return SELESNYA
        elif self.color.blue:
            if self.color.black:
                return DIMIR
            elif self.color.red:
                return IZZET
            elif self.color.green:
                return SIMIC
        elif self.color.black:
            if self.color.red:
                return RAKDOS
            elif self.color.green:
                return GOLGARI
        elif self.color.red:
            if self.color.green:
                return GRUUL
