from util import only1

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
        if

    def assign_colors(self):
        self.colors = [self.white, self.blue, self.black, self.red, self.green]
