from util import only1, morethan1, exactly2

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
        if only1(self.colors):
            self.monocolored = True
        else:
            self.monocolored = False
        if morethan1(self.colors):
            self.multicolored = True
        else:
            self.multicolored = False
        if exactly2(self.colors):
            self.colorpair = True
            self.guild = self.get_guild()
        else:
            self.colorpair = False

    def assign_colors(self):
        self.colors = [self.white, self.blue, self.black, self.red, self.green]
