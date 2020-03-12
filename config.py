# configurable constant values or other preferences and settings

# FOUR COLOR NAMING
# -----------------

# Pick your naming scheme from these options
# 0: "WUBRG", i.e. WUBR or BRGW or whatever
# 1: "c16-theme", i.e. Growth or Aggression
# 2: "neph-short", i.e. Glint
# 3: "neph-long", i.e. Glint-Eye
# "not": "the color it isn't" i.e. not-blue or blueless
FOURC_NAMING_CONVENTION = 0
if FOURC_NAMING_CONVENTION == "not":
    FOURC_USE_PREFIX = True # change to false if you want to use suffix instead

FOURC_NO_X_PREF = "not-"
FOURC_X_LESS_SUFF = "less"
