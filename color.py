class Color:
    pass

class White(Color):
    def __str__(self):
        return "white"

class Blue(Color):
    def __str__(self):
        return "blue"

class Black(Color):
    def __str__(self):
        return "black"

class Red(Color):
    def __str__(self):
        return "red"

class Green(Color):
    def __str__(self):
        return "green"

class Guild:
    def __init__(self, c1, c2):
        if type(c1) is type(c2):
            raise ValueError("Colors cannot match.")
        self.c1 = c1
        self.c2 = c2
        self.guild = self.get_guild()

    def get_guild(self):
        if isinstance(self.c1, White):
            if isinstance(self.c2, )
