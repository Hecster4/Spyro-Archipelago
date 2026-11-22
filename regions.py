from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SpyroWorld
    
def create_and_connect_regions(world: SpyroWorld) -> None:
    create_all_regions(world)
    connect_regions(world)
    
def create_all_regions(world: SpyroWorld) -> None:
    Artisans = Region("Artisans", world.player, world.multiworld)
    Stone_Hill = Region("Stone Hill", world.player, world.multiworld)
    Dark_Hollow = Region("Dark Hollow", world.player, world.multiworld)
    Town_Square = Region("Town Square", world.player, world.multiworld)
    Toasty = Region("Toasty", world.player, world.multiworld)
    Sunny_Flight = Region("Sunny Flight", world.player, world.multiworld)
    Peace_Keepers = Region("Peace Keepers", world.player, world.multiworld)
    Dry_Canyon = Region("Dry Canyon", world.player, world.multiworld)
    Cliff_Town = Region("Cliff Town", world.player, world.multiworld)
    Ice_Cavern = Region("Ice Cavern", world.player, world.multiworld)
    Doctor_Shemp = Region("Doctor Shemp", world.player, world.multiworld)
    Night_Flight = Region("Night Flight", world.player, world.multiworld)
    Magic_Crafters = Region("Magic Crafters", world.player, world.multiworld)
    Alpine_Ridge = Region("Alpine Ridge", world.player, world.multiworld)
    High_Caves = Region("High Caves", world.player, world.multiworld)
    Wizard_Peak = Region("Wizard Peak", world.player, world.multiworld)
    Blowhard = Region("Blowhard", world.player, world.multiworld)
    Crystal_Flight =  Region("Crystal Flight", world.player, world.multiworld)
    Beast_Makers = Region("Beast Makers", world.player, world.multiworld)
    Terrace_Village = Region("Terrace Village", world.player, world.multiworld)
    Misty_Bog = Region("Misty Bog", world.player, world.multiworld)
    Tree_Tops = Region("Tree Tops", world.player, world.multiworld)
    Metalhead = Region("Metalhead", world.player, world.multiworld)
    Wild_Flight = Region("Wild Flight", world.player, world.multiworld)
    Dream_Weavers = Region("Dream Weavers", world.player, world.multiworld)
    Dark_Passage = Region("Dark Passage", world.player, world.multiworld)
    Lofty_Castle = Region("Lofty Castle", world.player, world.multiworld)
    Haunted_Towers = Region("Haunted Towers", world.player, world.multiworld)
    Jacques = Region("Jacques", world.player, world.multiworld)
    Icy_Flight = Region("Icy Flight", world.player, world.multiworld)
    Gnorc_Gnexus = Region("Gnorc Gnexus", world.player, world.multiworld)
    Gnorc_Cove = Region("Gnorc Cove", world.player, world.multiworld)
    Twilight_Harbor = Region("Twilight Harbor", world.player, world.multiworld)
    Gnasty_Gnorc = Region("Gnasty Gnorc", world.player, world.multiworld)
    
    regions = [
        Artisans,
        Stone_Hill,
        Dark_Hollow,
        Town_Square,
        Toasty,
        Sunny_Flight,
        Peace_Keepers,
        Dry_Canyon,
        Cliff_Town,
        Ice_Cavern,
        Doctor_Shemp,
        Night_Flight,
        Magic_Crafters,
        Alpine_Ridge,
        High_Caves,
        Wizard_Peak,
        Blowhard,
        Crystal_Flight,
        Beast_Makers,
        Terrace_Village,
        Misty_Bog,
        Tree_Tops,
        Metalhead,
        Wild_Flight,
        Dream_Weavers,
        Dark_Passage,
        Lofty_Castle,
        Haunted_Towers,
        Jacques,
        Icy_Flight,
        Gnorc_Gnexus,
        Gnorc_Cove,
        Twilight_Harbor,
        Gnasty_Gnorc
        ]
    
    world.multiworld.regions += regions
    
def connect_regions(world: SpyroWorld) -> None:
    Artisans = world.get_region("Artisans")
    Stone_Hill = world.get_region("Stone Hill")
    Dark_Hollow = world.get_region("Dark Hollow")
    Town_Square = world.get_region("Town Square")
    Toasty = world.get_region("Toasty")
    Sunny_Flight = world.get_region("Sunny Flight")
    Peace_Keepers = world.get_region("Peace Keepers")
    Dry_Canyon = world.get_region("Dry Canyon")
    Cliff_Town = world.get_region("Cliff Town")
    Ice_Cavern = world.get_region("Ice Cavern")
    Doctor_Shemp = world.get_region("Doctor Shemp")
    Night_Flight = world.get_region("Night Flight")
    Magic_Crafters = world.get_region("Magic Crafters")
    Alpine_Ridge = world.get_region("Alpine Ridge")
    High_Caves = world.get_region("High Caves")
    Wizard_Peak = world.get_region("Wizard Peak")
    Blowhard = world.get_region("Blowhard")
    Crystal_Flight = world.get_region("Crystal Flight")
    Beast_Makers = world.get_region("Beast Makers")
    Terrace_Village = world.get_region("Terrace Village")
    Misty_Bog = world.get_region("Misty Bog")
    Tree_Tops = world.get_region("Tree Tops")
    Metalhead = world.get_region("Metalhead")
    Wild_Flight = world.get_region("Wild Flight")
    Dream_Weavers = world.get_region("Dream Weavers")
    Dark_Passage = world.get_region("Dark Passage")
    Lofty_Castle = world.get_region("Lofty Castle")
    Haunted_Towers = world.get_region("Haunted Towers")
    Jacques = world.get_region("Jacques")
    Icy_Flight = world.get_region("Icy Flight")
    Gnorc_Gnexus = world.get_region("Gnorc Gnexus")
    Gnorc_Cove = world.get_region("Gnorc Cove")
    Twilight_Harbor = world.get_region("Twilight Harbor")
    Gnasty_Gnorc = world.get_region("Gnasty Gnorc")
    
    Artisans.connect(Stone_Hill, "Artisans to Stone Hill")
    Artisans.connect(Dark_Hollow, "Artisans to Dark Hollow")
    Artisans.connect(Town_Square, "Artisans to Town Square")
    Artisans.connect(Toasty, "Artisans to Toasty")
    Artisans.connect(Sunny_Flight, "Artisans to Sunny Flight")
    Artisans.connect(Peace_Keepers, "Artisans to Peace Keepers")
    Peace_Keepers.connect(Dry_Canyon, "Peace Keepers to Dry Canyon")
    Peace_Keepers.connect(Cliff_Town, "Peace Keepers to Cliff Town")
    Peace_Keepers.connect(Ice_Cavern, "Peace Keepers to Ice Cavern")
    Peace_Keepers.connect(Doctor_Shemp, "Peace Keepers to Doctor Shemp")
    Peace_Keepers.connect(Night_Flight, "Peace Keepers to Night Flight")
    Peace_Keepers.connect(Magic_Crafters, "Peace Keepers to Magic Crafters")
    Magic_Crafters.connect(Alpine_Ridge, "Magic Crafters to Alpine Ridge")
    Magic_Crafters.connect(High_Caves, "Magic Crafters to High Caves")
    Magic_Crafters.connect(Wizard_Peak, "Magic Crafters to Wizard Peak")
    Magic_Crafters.connect(Blowhard, "Magic Crafters to Blowhard")
    Magic_Crafters.connect(Crystal_Flight, "Magic Crafters to Crystal Flight")
    Magic_Crafters.connect(Beast_Makers, "Magic Crafters to Beast Makers")
    Beast_Makers.connect(Terrace_Village, "Beast Makers to Terrace Village")
    Beast_Makers.connect(Misty_Bog, "Beast Makers to Misty Bog")
    Beast_Makers.connect(Tree_Tops, "Beast Makers to Tree Tops")
    Beast_Makers.connect(Metalhead, "Beast Makers to Metalhead")
    Beast_Makers.connect(Wild_Flight, "Beast Makers to Wild Flight")
    Beast_Makers.connect(Dream_Weavers, "Beast Makers to Dream Weavers")
    Dream_Weavers.connect(Dark_Passage, "Dream Weavers to Dark Passage")
    Dream_Weavers.connect(Lofty_Castle, "Dream Weavers to Lofty Castle")
    Dream_Weavers.connect(Haunted_Towers, "Dream Weavers to Haunted Towers")
    Dream_Weavers.connect(Jacques, "Dream Weavers to Jacques")
    Dream_Weavers.connect(Icy_Flight, "Dream Weavers to Icy Flight")
    Dream_Weavers.connect(Gnorc_Gnexus, "Dream Weavers to Gnorc Gnexus")
    Gnorc_Gnexus.connect(Gnorc_Cove, "Gnorc Gnexus to Gnorc Cove")
    Gnorc_Gnexus.connect(Twilight_Harbor, "Gnorc Gnexus to Twilight Harbor")
    Gnorc_Gnexus.connect(Gnasty_Gnorc, "Gnorc Gnexus to Gnasty Gnorc")