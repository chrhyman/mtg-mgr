# ---
# MTG Constants
# ---

ARTIFACT = "Artifact"
CONSPIRACY = "Conspiracy"
CREATURE = "Creature"
ENCHANTMENT = "Enchantment"
INSTANT = "Instant"
LAND = "Land"
PHENOMENON = "Phenomenon"
PLANE = "Plane"
PLANESWALKER = "Planeswalker"
SCHEME = "Scheme"
SORCERY = "Sorcery"
TRIBAL = "Tribal"
VANGUARD = "Vanguard"
CARD_TYPES = [ARTIFACT, CONSPIRACY, CREATURE, ENCHANTMENT, INSTANT, LAND, PHENOMENON, PLANE, PLANESWALKER, SCHEME, SORCERY, TRIBAL, VANGUARD]

# MANA SYMBOLS
def generic(n): return "{" + str(int(n)) + "}"
WHITE = "{W}"
BLUE = "{U}"
BLACK = "{B}"
RED = "{R}"
GREEN = "{G}"
COLORLESS = "{C}"
SNOW = "{S}"
PHYREXIAN = "{P}"
XMANA = "{X}"
YMANA = "{Y}"
ZMANA = "{Z}"
# hybrid
HY_WU = "{W/U}"
HY_WB = "{W/B}"
HY_UB = "{U/B}"
HY_UR = "{U/R}"
HY_BR = "{B/R}"
HY_BG = "{B/G}"
HY_RG = "{R/G}"
HY_RW = "{R/W}"
HY_GW = "{G/W}"
HY_GU = "{G/U}"
# mono-color hybrid
MHY_W = "{2/W}"
MHY_U = "{2/U}"
MHY_B = "{2/B}"
MHY_R = "{2/R}"
MHY_G = "{2/G}"
# phyrexian
PH_W = "{W/P}"
PH_U = "{U/P}"
PH_B = "{B/P}"
PH_R = "{R/P}"
PH_G = "{G/P}"
MANA_SYMBOLS = [WHITE, BLUE, BLACK, RED, GREEN,
    COLORLESS, SNOW, PHYREXIAN, XMANA, YMANA, ZMANA,
    HY_WU, HY_WB, HY_UB, HY_UR, HY_BR, HY_BG, HY_RG, HY_RW, HY_GW, HY_GU,
    MHY_W, MHY_U, MHY_B, MHY_R, MHY_G, PH_W, PH_U, PH_B, PH_R, PH_G]
MANA_CMC_0 = [XMANA, YMANA, ZMANA]
MANA_CMC_1 = [WHITE, BLUE, BLACK, RED, GREEN, COLORLESS, SNOW, PHYREXIAN,
    HY_WU, HY_WB, HY_UB, HY_UR, HY_BR, HY_BG, HY_RG, HY_RW, HY_GW, HY_GU,
    PH_W, PH_U, PH_B, PH_R, PH_G]
MANA_CMC_2 = [MHY_W, MHY_U, MHY_B, MHY_R, MHY_G]

# OTHER SYMBOLS
TAP = "{T}"
UNTAP = "{Q}"
ENERGY = "{E}"
def saga_ch(n): return "{rN" + str(int(n)) + "}"   # saga chapter symbol

# GUILDS
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
