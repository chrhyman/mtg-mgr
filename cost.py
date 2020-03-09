import re
from const import *

class Cost:
    """
    An object that contains all cost information for a spell or ability.
    See MTG rule 118.
    Should be able to take a cost string and convert it to a useable object
    Should be able to print the object into a readable comma-delimited string
    """
    def __init__(self, cost_str=None):
        self.mana = BASE_MANA_DICT  # a dict of quantities of mana in the cost
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

## TODO: Cost.__str__()
## TODO: account for paying life as a cost
