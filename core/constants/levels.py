# core/constants/levels.py

LEVEL_XP_BASE = 100

# Calculate level from XP
def get_level_for_xp(xp):
    return (xp // LEVEL_XP_BASE) + 1
