from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import SpyroWorld
    
def set_all_rules(world: SpyroWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_rules(world: SpyroWorld) -> None:
    Artisans_to_Peace_Keepers = world.get_entrance("Artisans to Peace Keepers")
    Peace_Keepers_to_Magic_Crafters = world.get_entrance("Peace Keepers to Magic Crafters")
    Magic_Crafters_to_Beast_Makers = world.get_entrance("Magic Crafters to Beast Makers")
    Beast_Makers_to_Dream_Weavers = world.get_entrance("Beast Makers to Dream Weavers")
    Dream_Weavers_to_Gnorc_Gnexus = world.get_entrance("Dream Weavers to Gnorc Gnexus")
    
    world.set_rule(Artisans_to_Peace_Keepers, Has("Dragon", 10))
    world.set_rule(Peace_Keepers_to_Magic_Crafters, Has("100 Gems", 12))
    world.set_rule(Magic_Crafters_to_Beast_Makers, Has("Egg", 5))
    world.set_rule(Beast_Makers_to_Dream_Weavers, Has("Dragon", 50))
    world.set_rule(Dream_Weavers_to_Gnorc_Gnexus, Has("100 Gems", 60))
    
    if world.options.portal_locks:
        Artisans_to_Stone_Hill = world.get_entrance("Artisans to Stone Hill")
        Artisans_to_Dark_Hollow = world.get_entrance("Artisans to Dark Hollow")
        Artisans_to_Town_Square = world.get_entrance("Artisans to Town Square")
        Artisans_to_Toasty = world.get_entrance("Artisans to Toasty")
        Artisans_to_Sunny_Flight = world.get_entrance("Artisans to Sunny Flight")
        Peace_Keepers_to_Dry_Canyon = world.get_entrance("Peace Keepers to Dry Canyon")
        Peace_Keepers_to_Cliff_Town = world.get_entrance("Peace Keepers to Cliff Town")
        Peace_Keepers_to_Ice_Cavern = world.get_entrance("Peace Keepers to Ice Cavern")
        Peace_Keepers_to_Doctor_Shemp = world.get_entrance("Peace Keepers to Doctor Shemp")
        Peace_Keepers_to_Night_Flight = world.get_entrance("Peace Keepers to Night Flight")
        Magic_Crafters_to_Alpine_Ridge = world.get_entrance("Magic Crafters to Alpine Ridge")
        Magic_Crafters_to_High_Caves = world.get_entrance("Magic Crafters to High Caves")
        Magic_Crafters_to_Wizard_Peak = world.get_entrance("Magic Crafters to Wizard Peak")
        Magic_Crafters_to_Blowhard = world.get_entrance("Magic Crafters to Blowhard")
        Magic_Crafters_to_Crystal_Flight = world.get_entrance("Magic Crafters to Crystal Flight")
        Beast_Makers_to_Terrace_Village = world.get_entrance("Beast Makers to Terrace Village")
        Beast_Makers_to_Misty_Bog = world.get_entrance("Beast Makers to Misty Bog")
        Beast_Makers_to_Tree_Tops = world.get_entrance("Beast Makers to Tree Tops")
        Beast_Makers_to_Metalhead = world.get_entrance("Beast Makers to Metalhead")
        Beast_Makers_to_Wild_Flight = world.get_entrance("Beast Makers to Wild Flight")
        Dream_Weavers_to_Dark_Passage = world.get_entrance("Dream Weavers to Dark Passage")
        Dream_Weavers_to_Lofty_Castle = world.get_entrance("Dream Weavers to Lofty Castle")
        Dream_Weavers_to_Haunted_Towers = world.get_entrance("Dream Weavers to Haunted Towers")
        Dream_Weavers_to_Jacques = world.get_entrance("Dream Weavers to Jacques")
        Dream_Weavers_to_Icy_Flight = world.get_entrance("Dream Weavers to Icy Flight")
        Gnorc_Gnexus_to_Gnorc_Cove = world.get_entrance("Gnorc Gnexus to Gnorc Cove")
        Gnorc_Gnexus_to_Twilight_Harbor = world.get_entrance("Gnorc Gnexus to Twilight Harbor")
        Gnorc_Gnexus_to_Gnasty_Gnorc = world.get_entrance("Gnorc Gnexus to Gnasty Gnorc")
        
        world.set_rule(Artisans_to_Stone_Hill, Has("Stone Hill Unlocked"))
        world.set_rule(Artisans_to_Dark_Hollow, Has("Dark Hollow Unlocked"))
        world.set_rule(Artisans_to_Town_Square, Has("Town Square Unlocked"))
        world.set_rule(Artisans_to_Toasty, Has("Toasty Unlocked") & (Has("Stone Hill Unlocked") | Has("Dark Hollow Unlocked") | Has("Town Square Unlocked") | Has("Sunny Flight Unlocked")))
        world.set_rule(Artisans_to_Sunny_Flight, Has("Sunny Flight Unlocked"))
        world.set_rule(Peace_Keepers_to_Dry_Canyon, Has("Dry Canyon Unlocked"))
        world.set_rule(Peace_Keepers_to_Cliff_Town, Has("Cliff Town Unlocked"))
        world.set_rule(Peace_Keepers_to_Ice_Cavern, Has("Ice Cavern Unlocked"))
        world.set_rule(Peace_Keepers_to_Doctor_Shemp, Has("Doctor Shemp Unlocked"))
        world.set_rule(Peace_Keepers_to_Night_Flight, Has("Night Flight Unlocked"))
        world.set_rule(Magic_Crafters_to_Alpine_Ridge, Has("Alpine Ridge Unlocked"))
        world.set_rule(Magic_Crafters_to_High_Caves, Has("High Caves Unlocked"))
        world.set_rule(Magic_Crafters_to_Wizard_Peak, Has("Wizard Peak Unlocked"))
        world.set_rule(Magic_Crafters_to_Blowhard, Has("Blowhard Unlocked"))
        world.set_rule(Magic_Crafters_to_Crystal_Flight, Has("Crystal Flight Unlocked"))
        world.set_rule(Beast_Makers_to_Terrace_Village, Has("Terrace Village Unlocked"))
        world.set_rule(Beast_Makers_to_Misty_Bog, Has("Misty Bog Unlocked"))
        world.set_rule(Beast_Makers_to_Tree_Tops, Has("Tree Tops Unlocked"))
        world.set_rule(Beast_Makers_to_Metalhead, Has("Metalhead Unlocked"))
        world.set_rule(Beast_Makers_to_Wild_Flight, Has("Wild Flight Unlocked"))
        world.set_rule(Dream_Weavers_to_Dark_Passage, Has("Dark Passage Unlocked"))
        world.set_rule(Dream_Weavers_to_Lofty_Castle, Has("Lofty Castle Unlocked"))
        world.set_rule(Dream_Weavers_to_Haunted_Towers, Has("Haunted Towers Unlocked"))
        world.set_rule(Dream_Weavers_to_Jacques, Has("Jacques Unlocked"))
        world.set_rule(Dream_Weavers_to_Icy_Flight, Has("Icy Flight Unlocked"))
        world.set_rule(Gnorc_Gnexus_to_Gnorc_Cove, Has("Gnorc Cove Unlocked"))
        world.set_rule(Gnorc_Gnexus_to_Twilight_Harbor, Has("Twilight Harbor Unlocked") & Has("Gnorc Cove Unlocked"))
        world.set_rule(Gnorc_Gnexus_to_Gnasty_Gnorc, Has("Gnasty Gnorc Unlocked") & Has("Twilight Harbor Unlocked") & Has("Gnorc Cove Unlocked"))
    
def set_all_location_rules(world: SpyroWorld) -> None:
    pass

def set_completion_condition(world: SpyroWorld) -> None:
     world.set_completion_rule(Has("Victory"))