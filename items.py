from __future__ import annotations

from random import choice

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SpyroWorld
    
gemsTotal = 0
dragonsTotal = 0
eggsTotal = 0
    
ITEM_NAME_TO_ID = {
    "100 Gems": 1,
    "Dragon": 2,
    "Egg": 3,
    "Life": 4,
    "Stone Hill Unlocked": 11,
    "Dark Hollow Unlocked": 12,
    "Town Square Unlocked": 13,
    "Toasty Unlocked": 14,
    "Sunny Flight Unlocked": 15,
    "Dry Canyon Unlocked": 21,
    "Cliff Town Unlocked": 22,
    "Ice Cavern Unlocked": 23,
    "Doctor Shemp Unlocked": 24,
    "Night Flight Unlocked": 25,
    "Alpine Ridge Unlocked": 31,
    "High Caves Unlocked": 32,
    "Wizard Peak Unlocked": 33,
    "Blowhard Unlocked": 34,
    "Crystal Flight Unlocked": 35,
    "Terrace Village Unlocked": 41,
    "Misty Bog Unlocked": 42,
    "Tree Tops Unlocked": 43,
    "Metalhead Unlocked": 44,
    "Wild Flight Unlocked": 45,
    "Dark Passage Unlocked": 51,
    "Lofty Castle Unlocked": 52,
    "Haunted Towers Unlocked": 53,
    "Jacques Unlocked": 54,
    "Icy Flight Unlocked": 55,
    "Gnorc Cove Unlocked": 61,
    "Twilight Harbor Unlocked": 62,
    "Gnasty Gnorc Unlocked": 63
    }

DEFAULT_ITEM_CLASSIFICATIONS = {
    "100 Gems" : ItemClassification.progression,
    "Dragon": ItemClassification.progression,
    "Egg": ItemClassification.progression,
    "Life": ItemClassification.filler,
    "Stone Hill Unlocked": ItemClassification.progression,
    "Dark Hollow Unlocked": ItemClassification.progression,
    "Town Square Unlocked": ItemClassification.progression,
    "Toasty Unlocked": ItemClassification.progression,
    "Sunny Flight Unlocked": ItemClassification.progression,
    "Dry Canyon Unlocked": ItemClassification.progression,
    "Cliff Town Unlocked": ItemClassification.progression,
    "Ice Cavern Unlocked": ItemClassification.progression,
    "Doctor Shemp Unlocked": ItemClassification.progression,
    "Night Flight Unlocked": ItemClassification.progression,
    "Alpine Ridge Unlocked": ItemClassification.progression,
    "High Caves Unlocked": ItemClassification.progression,
    "Wizard Peak Unlocked": ItemClassification.progression,
    "Blowhard Unlocked": ItemClassification.progression,
    "Crystal Flight Unlocked": ItemClassification.progression,
    "Terrace Village Unlocked": ItemClassification.progression,
    "Misty Bog Unlocked": ItemClassification.progression,
    "Tree Tops Unlocked": ItemClassification.progression,
    "Metalhead Unlocked": ItemClassification.progression,
    "Wild Flight Unlocked": ItemClassification.progression,
    "Dark Passage Unlocked": ItemClassification.progression,
    "Lofty Castle Unlocked": ItemClassification.progression,
    "Haunted Towers Unlocked": ItemClassification.progression,
    "Jacques Unlocked": ItemClassification.progression,
    "Icy Flight Unlocked": ItemClassification.progression,
    "Gnorc Cove Unlocked": ItemClassification.progression,
    "Twilight Harbor Unlocked": ItemClassification.progression,
    "Gnasty Gnorc Unlocked": ItemClassification.progression
    }

class SpyroItem(Item):
    game = "Spyro the Dragon"

def get_random_filler_item_name(world: SpyroWorld) -> str:
    return "Life"

def create_item_with_correct_classification(world: SpyroWorld, name: str) -> SpyroItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return SpyroItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SpyroWorld) -> None:
    itempool: list[Item] = []
    for i in range(120):
        itempool.append(world.create_item("100 Gems"))
    for i in range(80):
        itempool.append(world.create_item("Dragon"))
    for i in range(12):
        itempool.append(world.create_item("Egg"))
    if world.options.portal_locks:
        levels = ["Stone Hill Unlocked", "Dark Hollow Unlocked", "Town Square Unlocked"]
        for i in range(world.options.starting_levels):
            level = choice(levels)
            levels.remove(level)
            world.push_precollected(world.create_item(f"{level}"))
        if levels != []:
            for level in levels:
                itempool.append(world.create_item(f"{level}"))
        itempool.append(world.create_item("Toasty Unlocked"))
        itempool.append(world.create_item("Sunny Flight Unlocked"))
        itempool.append(world.create_item("Dry Canyon Unlocked"))
        itempool.append(world.create_item("Cliff Town Unlocked"))
        itempool.append(world.create_item("Ice Cavern Unlocked"))
        itempool.append(world.create_item("Doctor Shemp Unlocked"))
        itempool.append(world.create_item("Night Flight Unlocked"))
        itempool.append(world.create_item("Alpine Ridge Unlocked"))
        itempool.append(world.create_item("High Caves Unlocked"))
        itempool.append(world.create_item("Wizard Peak Unlocked"))
        itempool.append(world.create_item("Blowhard Unlocked"))
        itempool.append(world.create_item("Crystal Flight Unlocked"))
        itempool.append(world.create_item("Terrace Village Unlocked"))
        itempool.append(world.create_item("Misty Bog Unlocked"))
        itempool.append(world.create_item("Tree Tops Unlocked"))
        itempool.append(world.create_item("Metalhead Unlocked"))
        itempool.append(world.create_item("Wild Flight Unlocked"))
        itempool.append(world.create_item("Dark Passage Unlocked"))
        itempool.append(world.create_item("Lofty Castle Unlocked"))
        itempool.append(world.create_item("Haunted Towers Unlocked"))
        itempool.append(world.create_item("Jacques Unlocked"))
        itempool.append(world.create_item("Icy Flight Unlocked"))
        itempool.append(world.create_item("Gnorc Cove Unlocked"))
        itempool.append(world.create_item("Twilight Harbor Unlocked"))
        itempool.append(world.create_item("Gnasty Gnorc Unlocked"))
        
    number_of_items = len(itempool)
    
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    world.multiworld.itempool += itempool