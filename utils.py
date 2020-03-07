import re
from mtgconst import *

class Cost:
    """
    An object that contains all cost information for a spell or ability.
    See MTG rule 118.
    Should be able to take a cost string and convert it to a useable object
    Should be able to print the object into a readable comma-delimited string
    """
    def __init__(self, cost_str=None):
        self.mana = {m:0 for m in MANA_SYMBOLS} # a dict of quantities of mana
        self.mana['generic'] = 0                # symbols in the cost
        self.tap = False            # true if cost requires its permanent tap
        self.untap = False          # true if cost requires its permanent untap
        self.energy = 0             # amount of energy counters to pay
        self.life = 0               # amount of life to pay if static
        self.verbose = []   # list of written costs or add'l costs for spells
        self.cmc = None
        if cost_str is not None:
            self.process(cost_str)
            self.cmc = self.get_cmc()

    def process(self, input):   # convert input string to Cost object
        for cost in input.split(','):
            if '{' in cost or '}' in cost:
                for symbol in re.findall("\{.+?\}", cost):
                    if symbol[1:-1].isnumeric():
                        self.mana['generic'] += int(symbol[1:-1])
                    if symbol in MANA_SYMBOLS:
                        self.mana[symbol] += 1
                    if symbol == TAP:
                        self.tap = True
                    if symbol == UNTAP:
                        self.untap = True
                    if symbol == ENERGY:
                        self.energy += 1
            else:
                self.verbose.append(cost.strip())

    def get_cmc(self):
        total = 0
        for key in self.mana:
            if key in MANA_CMC_0:
                pass
            elif key in MANA_CMC_1:
                total += self.mana[key]
            elif key in MANA_CMC_2:
                total += 2 * self.mana[key]
        return total

## TODO: Cost.cmc()
## TODO: Cost.__str__()
## TODO: account for paying life as a cost

def find_cmc(cost):
    """
    Takes a mana cost string and converts it to its converted mana cost
    """
    cmc = 0
    for c in re.findall("\{.+?\}", cost):
        temp = c[1:-1]
        if temp.isnumeric():
            temp = int(temp)
        else:
            if temp in ['X', 'Y', 'Z']:
                temp = 0
            elif (temp in MANA_TYPES
            or temp in ["W/U", "W/B", "U/B", "U/R", "B/R",
                        "B/G", "R/G", "R/W", "G/W", "G/U",
                        "W/P", "U/P", "B/P", "R/P", "G/P"]):
                temp = 1
            elif temp in ["2/W", "2/U", "2/B", "2/R", "2/G"]:
                temp = 2
        cmc += temp
    return cmc

def format_cost(cost):
    """
    Takes a string of mana symbols and formats the cost properly
    i.e. {W}{1}{U}{2}{W} > {3}{W}{W}{U}
    """
    mana = {m:0 for m in MANA_SYMBOLS}
    for m in mana:
        mana[m] = cost.count(m)
    mana['generic'] = 0
    for g in re.findall("\{\d+\}", cost):
        mana['generic'] += int(g[1:-1])
    return mana
