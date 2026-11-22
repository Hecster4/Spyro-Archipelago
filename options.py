from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle
   
class Deathlink(Toggle):
    """
    When you die, everyone who enabled death link dies. Of course, the reverse is true too.
    """
    display_name = "Deathlink"
    
    default = "false"

class PortalLocks(Toggle):
    """
    Lock levels until you find the unlock level item.
    """
    display_name = "Portal Locks"
    
    default = 'false'
    
class StartingLevels(Range):
    """
    If level locks is enabled how many unlocked levels to start with.
    """
    display_name = "Starting Levels"
    
    range_start = 0
    range_end = 3
    
    default = 1
    
@dataclass
class SpyroOptions(PerGameCommonOptions):
    portal_locks: PortalLocks
    starting_levels: StartingLevels
    deathlink: Deathlink
    
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Deathlink, PortalLocks, StartingLevels]
    )]