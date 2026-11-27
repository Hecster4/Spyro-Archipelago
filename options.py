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
    Lock portals until you find the unlock portal item.
    """
    display_name = "Portal Locks"
    
    default = 'false'
    
class StartingPortals(Range):
    """
    If level locks is enabled how many unlocked portals to start with.
    """
    display_name = "Starting Levels"
    
    range_start = 0
    range_end = 3
    
    default = 1
    
class IncludeGnastysLoot(Toggle):
    """
    Include all gem checks and 100% completion of Gnasty's Loot as checks, if level
    locks are enabled you can access Gnasty's Loot once Gnasty's Loot Unlocked is received.
    """
    display_name = "Include Gnasty's Loot"
    
    default = 'false'
    
class LifeChestChecks(Toggle):
    """
    Include all 42 life chests in world as checks
    """
    display_name = "Life Chest Checks"
    
    default = 'false'
    
@dataclass
class SpyroOptions(PerGameCommonOptions):
    deathlink: Deathlink
    portal_locks: PortalLocks
    starting_portals: StartingPortals
    include_gnastys_loot: IncludeGnastysLoot
    life_chest_checks: LifeChestChecks
    
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Deathlink, PortalLocks, StartingPortals, IncludeGnastysLoot, LifeChestChecks]
    )]
