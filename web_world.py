from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups

class SpyroWebWorld(WebWorld):
    game = "Spyro the Dragon"
    
    theme = "grassFlowers"
    
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Spyro for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Jennifer"],
    )
    
    tutorials = [setup_en]