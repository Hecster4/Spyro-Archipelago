from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SpyroWorld
    
LOCATION_NAME_TO_ID = {
    "Artisans: 100 Gems": 1,
    "Artisans: Nestor": 2,
    "Artisans: Delbin": 3,
    "Artisans: Argus": 4,
    "Artisans: Tomas": 5,
    "Artisans: 100% Complete": 6,
    "Stone Hill: 100 Gems": 7,
    "Stone Hill: 200 Gems": 8,
    "Stone Hill: Gavin": 9,
    "Stone Hill: Lindar": 10,
    "Stone Hill: Astor": 11,
    "Stone Hill: Gildas": 12,
    "Stone Hill: Egg #1": 13,
    "Stone Hill: 100% Complete": 14,
    "Dark Hollow: 100 Gems": 15,
    "Dark Hollow: Alban": 16,
    "Dark Hollow: Oswin": 17,
    "Dark Hollow: Darius": 18,
    "Dark Hollow: 100% Complete": 19,
    "Town Square: 100 Gems": 20,
    "Town Square: 200 Gems": 21,
    "Town Square: Nils": 22,
    "Town Square: Devlin": 23,
    "Town Square: Alvar": 24,
    "Town Square: Thor": 25,
    "Town Square: Egg #1": 26,
    "Town Square: 100% Complete": 27,
    "Toasty: 100 Gems": 28,
    "Toasty: 100% Gems": 29,
    "Toasty: Nevin": 30,
    "Toasty: 100% Complete": 31,
    "Sunny Flight: 100 Gems": 32,
    "Sunny Flight: 200 Gems": 33,
    "Sunny Flight: 300 Gems": 34,
    "Sunny Flight: 100% Complete": 35,
    "Peace Keepers: 100 Gems": 36,
    "Peace Keepers: 200 Gems": 37,
    "Peace Keepers: Titan": 38,
    "Peace Keepers: Magnus": 39,
    "Peace Keepers: Gunnar": 40,
    "Peace Keepers: Egg #1": 41,
    "Peace Keepers: 100% Complete": 42,
    "Dry Canyon: 100 Gems": 43,
    "Dry Canyon: 200 Gems": 44,
    "Dry Canyon: 300 Gems": 45,
    "Dry Canyon: 400 Gems": 46,
    "Dry Canyon: Conan": 47,
    "Dry Canyon: Ivor": 48,
    "Dry Canyon: Boris": 49,
    "Dry Canyon: Maximos": 50,
    "Dry Canyon: Egg #1": 51,
    "Dry Canyon: 100% Complete": 52,
    "Cliff Town: 100 Gems": 53,
    "Cliff Town: 200 Gems": 54,
    "Cliff Town: 300 Gems": 55,
    "Cliff Town: 400 Gems": 56,
    "Cliff Town: Halvor": 57,
    "Cliff Town: Enzo": 58,
    "Cliff Town: Marco": 59,
    "Cliff Town: Egg #1": 60,
    "Cliff Town: 100% Complete": 61,
    "Ice Cavern: 100 Gems": 62,
    "Ice Cavern: 200 Gems": 63,
    "Ice Cavern: 300 Gems": 64,
    "Ice Cavern: 400 Gems": 65,
    "Ice Cavern: Ulric": 66,
    "Ice Cavern: Todor": 67,
    "Ice Cavern: Andor": 68,
    "Ice Cavern: Asher": 69,
    "Ice Cavern: Ragnar": 70,
    "Ice Cavern: 100% Complete": 71,
    "Doctor Shemp: 100 Gems": 72,
    "Doctor Shemp: 200 Gems": 73,
    "Doctor Shemp: 300 Gems": 74,
    "Doctor Shemp: Trondo": 75,
    "Doctor Shemp: 100% Complete": 76,
    "Night Flight: 100 Gems": 77,
    "Night Flight: 200 Gems": 78,
    "Night Flight: 300 Gems": 79,
    "Night Flight: 100% Complete": 80,
    "Magic Crafters: 100 Gems": 81,
    "Magic Crafters: 200 Gems": 82,
    "Magic Crafters: 300 Gems": 83,
    "Magic Crafters: Cosmos": 84,
    "Magic Crafters: Zantor": 85,
    "Magic Crafters: Boldar": 86,
    "Magic Crafters: Egg #1": 87,
    "Magic Crafters: Egg #2": 88,
    "Magic Crafters: 100% Complete": 89,
    "Alpine Ridge: 100 Gems": 90,
    "Alpine Ridge: 200 Gems": 91,
    "Alpine Ridge: 300 Gems": 92,
    "Alpine Ridge: 400 Gems": 93,
    "Alpine Ridge: 500 Gems": 94,
    "Alpine Ridge: Zane": 95,
    "Alpine Ridge: Eldrid": 96,
    "Alpine Ridge: Zander": 97,
    "Alpine Ridge: Kelvin": 98,
    "Alpine Ridge: Egg #1": 99,
    "Alpine Ridge: 100% Complete": 100,
    "High Caves: 100 Gems": 101,
    "High Caves: 200 Gems": 102,
    "High Caves: 300 Gems": 103,
    "High Caves: 400 Gems": 104,
    "High Caves: 500 Gems": 105,
    "High Caves: Ajax": 106,
    "High Caves: Cyrus": 107,
    "High Caves: Cedric": 108,
    "High Caves: Egg #1": 109,
    "High Caves: Egg #2": 110,
    "High Caves: 100% Complete": 111,
    "Wizard Peak: 100 Gems": 112,
    "Wizard Peak: 200 Gems": 113,
    "Wizard Peak: 300 Gems": 114,
    "Wizard Peak: 400 Gems": 115,
    "Wizard Peak: 500 Gems": 116,
    "Wizard Peak: Jarvis": 117,
    "Wizard Peak: Hexus": 118,
    "Wizard Peak: Lucas": 119,
    "Wizard Peak: Egg #1": 120,
    "Wizard Peak: Egg #2": 121,
    "Wizard Peak: 100% Complete": 122,
    "Blowhard: 100 Gems": 123,
    "Blowhard: 200 Gems": 124,
    "Blowhard: 300 Gems": 125,
    "Blowhard: 400 Gems": 126,
    "Blowhard: Altair": 127,
    "Blowhard: 100% Complete": 128,
    "Crystal Flight: 100 Gems": 129,
    "Crystal Flight: 200 Gems": 130,
    "Crystal Flight: 300 Gems": 131,
    "Crystal Flight: 100% Complete": 132,
    "Beast Makers: 100 Gems": 133,
    "Beast Makers: 200 Gems": 134,
    "Beast Makers: 300 Gems": 135,
    "Beast Makers: Bruno": 136,
    "Beast Makers: Cleetus": 137,
    "Beast Makers: 100% Complete": 138,
    "Terrace Village: 100 Gems": 139,
    "Terrace Village: 200 Gems": 140,
    "Terrace Village: 300 Gems": 141,
    "Terrace Village: 400 Gems": 142,
    "Terrace Village: Claude": 143,
    "Terrace Village: Cyprin": 144,
    "Terrace Village: 100% Complete": 145,
    "Misty Bog: 100 Gems": 146,
    "Misty Bog: 200 Gems": 147,
    "Misty Bog: 300 Gems": 148,
    "Misty Bog: 400 Gems": 149,
    "Misty Bog: 500 Gems": 150,
    "Misty Bog: Rosco": 151,
    "Misty Bog: Damon": 152,
    "Misty Bog: Zeke": 153,
    "Misty Bog: Bubba": 154,
    "Misty Bog: 100% Complete": 155,
    "Tree Tops: 100 Gems": 156,
    "Tree Tops: 200 Gems": 157,
    "Tree Tops: 300 Gems": 158,
    "Tree Tops: 400 Gems": 159,
    "Tree Tops: 500 Gems": 160,
    "Tree Tops: Lyle": 161,
    "Tree Tops: Jed": 162,
    "Tree Tops: Isaak": 163,
    "Tree Tops: 100% Complete": 164,
    "Metalhead: 100 Gems": 165,
    "Metalhead: 200 Gems": 166,
    "Metalhead: 300 Gems": 167,
    "Metalhead: 400 Gems": 168,
    "Metalhead: 500 Gems": 169,
    "Metalhead: Sadiki": 170,
    "Metalhead: 100% Complete": 171,
    "Wild Flight: 100 Gems": 172,
    "Wild Flight: 200 Gems": 173,
    "Wild Flight: 300 Gems": 174,
    "Wild Flight: 100% Complete": 175,
    "Dream Weavers: 100 Gems": 176,
    "Dream Weavers: 200 Gems": 177,
    "Dream Weavers: 300 Gems": 178,
    "Dream Weavers: Mazi": 179,
    "Dream Weavers: Lateef": 180,
    "Dream Weavers: Zikomo": 181,
    "Dream Weavers: 100% Complete": 182,
    "Dark Passage: 100 Gems": 183,
    "Dark Passage: 200 Gems": 184,
    "Dark Passage: 300 Gems": 185,
    "Dark Passage: 400 Gems": 186,
    "Dark Passage: 500 Gems": 187,
    "Dark Passage: Kasiya": 188,
    "Dark Passage: Azizi": 189,
    "Dark Passage: Bakari": 190,
    "Dark Passage: Apara": 191,
    "Dark Passage: Obasi": 192,
    "Dark Passage: 100% Complete": 193,
    "Lofty Castle: 100 Gems": 194,
    "Lofty Castle: 200 Gems": 195,
    "Lofty Castle: 300 Gems": 196,
    "Lofty Castle: 400 Gems": 197,
    "Lofty Castle: Mudada": 198,
    "Lofty Castle: Baruti": 199,
    "Lofty Castle: Useni": 200,
    "Lofty Castle: 100% Complete": 201,
    "Haunted Towers: 100 Gems": 202,
    "Haunted Towers: 200 Gems": 203,
    "Haunted Towers: 300 Gems": 204,
    "Haunted Towers: 400 Gems": 205,
    "Haunted Towers: 500 Gems": 206,
    "Haunted Towers: Kosoko": 207,
    "Haunted Towers: Lutalo": 208,
    "Haunted Towers: Copano": 209,
    "Haunted Towers: 100% Complete": 210,
    "Jacques: 100 Gems": 211,
    "Jacques: 200 Gems": 212,
    "Jacques: 300 Gems": 213,
    "Jacques: 400 Gems": 214,
    "Jacques: 500 Gems": 215,
    "Jacques: Unika": 216,
    "Jacques: Revilo": 217,
    "Jacques: 100% Complete": 218,
    "Icy Flight: 100 Gems": 219,
    "Icy Flight: 200 Gems": 220,
    "Icy Flight: 300 Gems": 221,
    "Icy Flight: 100% Complete": 222,
    "Gnorc Gnexus: 100 Gems": 223,
    "Gnorc Gnexus: 200 Gems": 224,
    "Gnorc Gnexus: Delbin": 225,
    "Gnorc Gnexus: Magnus": 226,
    "Gnorc Gnexus: 100% Complete": 227,
    "Gnorc Cove: 100 Gems": 228,
    "Gnorc Cove: 200 Gems": 229,
    "Gnorc Cove: 300 Gems": 230,
    "Gnorc Cove: 400 Gems": 231,
    "Gnorc Cove: Lateef": 232,
    "Gnorc Cove: Tomas": 233,
    "Gnorc Cove: 100% Complete": 234,
    "Twilight Harbor: 100 Gems": 235,
    "Twilight Harbor: 200 Gems": 236,
    "Twilight Harbor: 300 Gems": 237,
    "Twilight Harbor: 400 Gems": 238,
    "Twilight Harbor: Cosmos": 239,
    "Twilight Harbor: Cleetus": 240,
    "Twilight Harbor: 100% Complete": 241,
    "Gnasty Gnorc: 100 Gems": 242,
    "Gnasty Gnorc: 200 Gems": 243,
    "Gnasty Gnorc: 300 Gems": 244,
    "Gnasty Gnorc: 400 Gems": 245,
    "Gnasty Gnorc: 500 Gems": 246,
    "Gnasty Gnorc: 100% Complete": 247
    }

class SpyroLocation(Location):
    game = "Spyro the Dragon"
    
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SpyroWorld) -> None:
    create_regular_locations(world)
    create_events(world)
    
def create_regular_locations(world: SpyroWorld) -> None:
    Artisans = world.get_region("Artisans")
    Peace_Keepers = world.get_region("Peace Keepers")
    Magic_Crafters = world.get_region("Magic Crafters")
    Beast_Makers = world.get_region("Beast Makers")
    Dream_Weavers = world.get_region("Dream Weavers")
    Gnorc_Gnexus = world.get_region("Gnorc Gnexus")
    Stone_Hill = world.get_region("Stone Hill")
    Dark_Hollow = world.get_region("Dark Hollow")
    Town_Square = world.get_region("Town Square")
    Toasty = world.get_region("Toasty")
    Sunny_Flight = world.get_region("Sunny Flight")
    Dry_Canyon = world.get_region("Dry Canyon")
    Cliff_Town = world.get_region("Cliff Town")
    Ice_Cavern = world.get_region("Ice Cavern")
    Doctor_Shemp = world.get_region("Doctor Shemp")
    Night_Flight = world.get_region("Night Flight")
    Alpine_Ridge = world.get_region("Alpine Ridge")
    High_Caves = world.get_region("High Caves")
    Wizard_Peak = world.get_region("Wizard Peak")
    Blowhard = world.get_region("Blowhard")
    Crystal_Flight = world.get_region("Crystal Flight")
    Terrace_Village = world.get_region("Terrace Village")
    Misty_Bog = world.get_region("Misty Bog")
    Tree_Tops = world.get_region("Tree Tops")
    Metalhead = world.get_region("Metalhead")
    Wild_Flight = world.get_region("Wild Flight")
    Dark_Passage = world.get_region("Dark Passage")
    Lofty_Castle = world.get_region("Lofty Castle")
    Haunted_Towers = world.get_region("Haunted Towers")
    Jacques = world.get_region("Jacques")
    Icy_Flight = world.get_region("Icy Flight")
    Gnorc_Cove = world.get_region("Gnorc Cove")
    Twilight_Harbor = world.get_region("Twilight Harbor")
    Gnasty_Gnorc = world.get_region("Gnasty Gnorc")
    
    Artisans_locations = get_location_names_with_ids([
        "Artisans: 100 Gems",
        "Artisans: Nestor",
        "Artisans: Delbin",
        "Artisans: Argus",
        "Artisans: Tomas",
        "Artisans: 100% Complete",
        ])
    Artisans.add_locations(Artisans_locations, SpyroLocation)
    
    Stone_Hill_Locations = get_location_names_with_ids([
        "Stone Hill: 100 Gems",
        "Stone Hill: 200 Gems",
        "Stone Hill: Gavin",
        "Stone Hill: Lindar",
        "Stone Hill: Astor",
        "Stone Hill: Gildas",
        "Stone Hill: Egg #1",
        "Stone Hill: 100% Complete"
        ])
    Stone_Hill.add_locations(Stone_Hill_Locations, SpyroLocation)
    
    Dark_Hollow_Locations = get_location_names_with_ids([
        "Dark Hollow: 100 Gems",
        "Dark Hollow: Alban",
        "Dark Hollow: Oswin",
        "Dark Hollow: Darius",
        "Dark Hollow: 100% Complete"
        ])
    Dark_Hollow.add_locations(Dark_Hollow_Locations, SpyroLocation)
    
    Town_Square_Locations = get_location_names_with_ids([
        "Town Square: 100 Gems",
        "Town Square: 200 Gems",
        "Town Square: Nils",
        "Town Square: Devlin",
        "Town Square: Alvar",
        "Town Square: Thor",
        "Town Square: Egg #1",
        "Town Square: 100% Complete"
        ])
    Town_Square.add_locations(Town_Square_Locations, SpyroLocation)
    
    Toasty_Locations = get_location_names_with_ids([
        "Toasty: 100 Gems",
        "Toasty: Nevin",
        "Toasty: 100% Complete"
        ])
    Toasty.add_locations(Toasty_Locations, SpyroLocation)
    
    Sunny_Flight_Locations = get_location_names_with_ids([
        "Sunny Flight: 100 Gems",
        "Sunny Flight: 200 Gems",
        "Sunny Flight: 300 Gems",
        "Sunny Flight: 100% Complete"
        ])
    Sunny_Flight.add_locations(Sunny_Flight_Locations, SpyroLocation)
    
    Peace_Keepers_locations = get_location_names_with_ids([
        "Peace Keepers: 100 Gems",
        "Peace Keepers: 200 Gems",
        "Peace Keepers: Titan",
        "Peace Keepers: Magnus",
        "Peace Keepers: Gunnar",
        "Peace Keepers: Egg #1",
        "Peace Keepers: 100% Complete"
        ])
    Peace_Keepers.add_locations(Peace_Keepers_locations, SpyroLocation)
    
    Dry_Canyon_Locations = get_location_names_with_ids([
        "Dry Canyon: 100 Gems",
        "Dry Canyon: 200 Gems",
        "Dry Canyon: 300 Gems",
        "Dry Canyon: 400 Gems",
        "Dry Canyon: Conan",
        "Dry Canyon: Ivor",
        "Dry Canyon: Boris",
        "Dry Canyon: Maximos",
        "Dry Canyon: Egg #1",
        "Dry Canyon: 100% Complete"
        ])
    Dry_Canyon.add_locations(Dry_Canyon_Locations, SpyroLocation)
    
    Cliff_Town_Locations = get_location_names_with_ids([
        "Cliff Town: 100 Gems",
        "Cliff Town: 200 Gems",
        "Cliff Town: 300 Gems",
        "Cliff Town: 400 Gems",
        "Cliff Town: Halvor",
        "Cliff Town: Enzo",
        "Cliff Town: Marco",
        "Cliff Town: Egg #1",
        "Cliff Town: 100% Complete"
        ])
    Cliff_Town.add_locations(Cliff_Town_Locations, SpyroLocation)
    
    Ice_Cavern_Locations = get_location_names_with_ids([
        "Ice Cavern: 100 Gems",
        "Ice Cavern: 200 Gems",
        "Ice Cavern: 300 Gems",
        "Ice Cavern: 400 Gems",
        "Ice Cavern: Ulric",
        "Ice Cavern: Todor",
        "Ice Cavern: Andor",
        "Ice Cavern: Asher",
        "Ice Cavern: Ragnar",
        "Ice Cavern: 100% Complete"
        ])
    Ice_Cavern.add_locations(Ice_Cavern_Locations, SpyroLocation)
    
    Doctor_Shemp_Locations = get_location_names_with_ids([
        "Doctor Shemp: 100 Gems",
        "Doctor Shemp: 200 Gems",
        "Doctor Shemp: 300 Gems",
        "Doctor Shemp: Trondo",
        "Doctor Shemp: 100% Complete"
        ])
    Doctor_Shemp.add_locations(Doctor_Shemp_Locations, SpyroLocation)
    
    Night_Flight_Locations = get_location_names_with_ids([
        "Night Flight: 100 Gems",
        "Night Flight: 200 Gems",
        "Night Flight: 300 Gems",
        "Night Flight: 100% Complete"
    ])
    Night_Flight.add_locations(Night_Flight_Locations, SpyroLocation)
    
    Magic_Crafters_locations = get_location_names_with_ids([
        "Magic Crafters: 100 Gems",
        "Magic Crafters: 200 Gems",
        "Magic Crafters: 300 Gems",
        "Magic Crafters: Cosmos",
        "Magic Crafters: Zantor",
        "Magic Crafters: Boldar",
        "Magic Crafters: Egg #1",
        "Magic Crafters: Egg #2",
        "Magic Crafters: 100% Complete"
        ])
    Magic_Crafters.add_locations(Magic_Crafters_locations, SpyroLocation)
    
    Alpine_Ridge_Locations = get_location_names_with_ids([
        "Alpine Ridge: 100 Gems",
        "Alpine Ridge: 200 Gems",
        "Alpine Ridge: 300 Gems",
        "Alpine Ridge: 400 Gems",
        "Alpine Ridge: 500 Gems",
        "Alpine Ridge: Zane",
        "Alpine Ridge: Eldrid",
        "Alpine Ridge: Zander",
        "Alpine Ridge: Kelvin",
        "Alpine Ridge: Egg #1",
        "Alpine Ridge: 100% Complete"
        ])
    Alpine_Ridge.add_locations(Alpine_Ridge_Locations, SpyroLocation)
    
    High_Caves_Locations = get_location_names_with_ids([
        "High Caves: 100 Gems",
        "High Caves: 200 Gems",
        "High Caves: 300 Gems",
        "High Caves: 400 Gems",
        "High Caves: 500 Gems",
        "High Caves: Ajax",
        "High Caves: Cyrus",
        "High Caves: Cedric",
        "High Caves: Egg #1",
        "High Caves: Egg #2",
        "High Caves: 100% Complete"
        ])
    High_Caves.add_locations(High_Caves_Locations, SpyroLocation)
    
    Wizard_Peak_Locations = get_location_names_with_ids([
        "Wizard Peak: 100 Gems",
        "Wizard Peak: 200 Gems",
        "Wizard Peak: 300 Gems",
        "Wizard Peak: 400 Gems",
        "Wizard Peak: 500 Gems",
        "Wizard Peak: Jarvis",
        "Wizard Peak: Hexus",
        "Wizard Peak: Lucas",
        "Wizard Peak: Egg #1",
        "Wizard Peak: Egg #2",
        "Wizard Peak: 100% Complete"
        ])
    Wizard_Peak.add_locations(Wizard_Peak_Locations, SpyroLocation)
    
    Blowhard_Locations = get_location_names_with_ids([
        "Blowhard: 100 Gems",
        "Blowhard: 200 Gems",
        "Blowhard: 300 Gems",
        "Blowhard: 400 Gems",
        "Blowhard: Altair",
        "Blowhard: 100% Complete"
        ])
    Blowhard.add_locations(Blowhard_Locations, SpyroLocation)
    
    Crystal_Flight_Locations = get_location_names_with_ids([
        "Crystal Flight: 100 Gems",
        "Crystal Flight: 200 Gems",
        "Crystal Flight: 300 Gems",
        "Crystal Flight: 100% Complete"
        ])
    Crystal_Flight.add_locations(Crystal_Flight_Locations, SpyroLocation)
    
    Beast_Makers_locations = get_location_names_with_ids([
        "Beast Makers: 100 Gems",
        "Beast Makers: 200 Gems",
        "Beast Makers: 300 Gems",
        "Beast Makers: Bruno",
        "Beast Makers: Cleetus",
        "Beast Makers: 100% Complete"
        ])
    Beast_Makers.add_locations(Beast_Makers_locations, SpyroLocation)
    
    Terrace_Village_Locations = get_location_names_with_ids([
        "Terrace Village: 100 Gems",
        "Terrace Village: 200 Gems",
        "Terrace Village: 300 Gems",
        "Terrace Village: 400 Gems",
        "Terrace Village: Claude",
        "Terrace Village: Cyprin",
        "Terrace Village: 100% Complete"
        ])
    Terrace_Village.add_locations(Terrace_Village_Locations, SpyroLocation)
    
    Misty_Bog_Locations = get_location_names_with_ids([
        "Misty Bog: 100 Gems",
        "Misty Bog: 200 Gems",
        "Misty Bog: 300 Gems",
        "Misty Bog: 400 Gems",
        "Misty Bog: 500 Gems",
        "Misty Bog: Rosco",
        "Misty Bog: Damon",
        "Misty Bog: Zeke",
        "Misty Bog: Bubba",
        "Misty Bog: 100% Complete"
        ])
    Misty_Bog.add_locations(Misty_Bog_Locations, SpyroLocation)
    
    Tree_Tops_Locations = get_location_names_with_ids([
        "Tree Tops: 100 Gems",
        "Tree Tops: 200 Gems",
        "Tree Tops: 300 Gems",
        "Tree Tops: 400 Gems",
        "Tree Tops: 500 Gems",
        "Tree Tops: Lyle",
        "Tree Tops: Jed",
        "Tree Tops: Isaak",
        "Tree Tops: 100% Complete"
        ])
    Tree_Tops.add_locations(Tree_Tops_Locations, SpyroLocation)
    
    Metalhead_Locations = get_location_names_with_ids([
        "Metalhead: 100 Gems",
        "Metalhead: 200 Gems",
        "Metalhead: 300 Gems",
        "Metalhead: 400 Gems",
        "Metalhead: 500 Gems",
        "Metalhead: Sadiki",
        "Metalhead: 100% Complete"
        ])
    Metalhead.add_locations(Metalhead_Locations, SpyroLocation)
    
    Wild_Flight_Locations = get_location_names_with_ids([
        "Wild Flight: 100 Gems",
        "Wild Flight: 200 Gems",
        "Wild Flight: 300 Gems",
        "Wild Flight: 100% Complete"
        ])
    Wild_Flight.add_locations(Wild_Flight_Locations, SpyroLocation)

    Dream_Weavers_locations = get_location_names_with_ids([
        "Dream Weavers: 100 Gems",
        "Dream Weavers: 200 Gems",
        "Dream Weavers: 300 Gems",
        "Dream Weavers: Mazi",
        "Dream Weavers: Lateef",
        "Dream Weavers: Zikomo",
        "Dream Weavers: 100% Complete"
        ])
    Dream_Weavers.add_locations(Dream_Weavers_locations, SpyroLocation)
    
    Dark_Passage_Locations = get_location_names_with_ids([
        "Dark Passage: 100 Gems",
        "Dark Passage: 200 Gems",
        "Dark Passage: 300 Gems",
        "Dark Passage: 400 Gems",
        "Dark Passage: 500 Gems",
        "Dark Passage: Kasiya",
        "Dark Passage: Azizi",
        "Dark Passage: Bakari",
        "Dark Passage: Apara",
        "Dark Passage: Obasi",
        "Dark Passage: 100% Complete"
        ])
    Dark_Passage.add_locations(Dark_Passage_Locations, SpyroLocation)
    
    Lofty_Castle_Locations = get_location_names_with_ids([
        "Lofty Castle: 100 Gems",
        "Lofty Castle: 200 Gems",
        "Lofty Castle: 300 Gems",
        "Lofty Castle: 400 Gems",
        "Lofty Castle: Mudada",
        "Lofty Castle: Baruti",
        "Lofty Castle: Useni",
        "Lofty Castle: 100% Complete"
        ])
    Lofty_Castle.add_locations(Lofty_Castle_Locations, SpyroLocation)
    
    Haunted_Towers_Locations = get_location_names_with_ids([
        "Haunted Towers: 100 Gems",
        "Haunted Towers: 200 Gems",
        "Haunted Towers: 300 Gems",
        "Haunted Towers: 400 Gems",
        "Haunted Towers: 500 Gems",
        "Haunted Towers: Kosoko",
        "Haunted Towers: Lutalo",
        "Haunted Towers: Copano",
        "Haunted Towers: 100% Complete"
        ])
    Haunted_Towers.add_locations(Haunted_Towers_Locations, SpyroLocation)
    
    Jacques_Locations = get_location_names_with_ids([
        "Jacques: 100 Gems",
        "Jacques: 200 Gems",
        "Jacques: 300 Gems",
        "Jacques: 400 Gems",
        "Jacques: 500 Gems",
        "Jacques: Unika",
        "Jacques: Revilo",
        "Jacques: 100% Complete"
        ])
    Jacques.add_locations(Jacques_Locations, SpyroLocation)
    
    Icy_Flight_Locations = get_location_names_with_ids([
        "Icy Flight: 100 Gems",
        "Icy Flight: 200 Gems",
        "Icy Flight: 300 Gems",
        "Icy Flight: 100% Complete"
        ])
    Icy_Flight.add_locations(Icy_Flight_Locations, SpyroLocation)
    
    Gnorc_Gnexus_locations = get_location_names_with_ids([
        "Gnorc Gnexus: 100 Gems",
        "Gnorc Gnexus: 200 Gems",
        "Gnorc Gnexus: Delbin",
        "Gnorc Gnexus: Magnus",
        "Gnorc Gnexus: 100% Complete"
        ])
    Gnorc_Gnexus.add_locations(Gnorc_Gnexus_locations, SpyroLocation)
    
    Gnorc_Cove_Locations = get_location_names_with_ids([
        "Gnorc Cove: 100 Gems",
        "Gnorc Cove: 200 Gems",
        "Gnorc Cove: 300 Gems",
        "Gnorc Cove: 400 Gems",
        "Gnorc Cove: Lateef",
        "Gnorc Cove: Tomas",
        "Gnorc Cove: 100% Complete"
        ])
    Gnorc_Cove.add_locations(Gnorc_Cove_Locations, SpyroLocation)
    
    Twilight_Harbor_Locations = get_location_names_with_ids([
        "Twilight Harbor: 100 Gems",
        "Twilight Harbor: 200 Gems",
        "Twilight Harbor: 300 Gems",
        "Twilight Harbor: 400 Gems",
        "Twilight Harbor: Cosmos",
        "Twilight Harbor: Cleetus",
        "Twilight Harbor: 100% Complete"
        ])
    Twilight_Harbor.add_locations(Twilight_Harbor_Locations, SpyroLocation)
    
    Gnasty_Gnorc_Locations = get_location_names_with_ids([
        "Gnasty Gnorc: 100 Gems",
        "Gnasty Gnorc: 200 Gems",
        "Gnasty Gnorc: 300 Gems",
        "Gnasty Gnorc: 400 Gems",
        "Gnasty Gnorc: 500 Gems",
        "Gnasty Gnorc: 100% Complete"
        ])
    Gnasty_Gnorc.add_locations(Gnasty_Gnorc_Locations, SpyroLocation)
    
def create_events(world: SpyroWorld) -> None:
    Gnasty_Gnorc = world.get_region("Gnasty Gnorc")
    
    Gnasty_Gnorc.add_event(
        "Gnasty Defeated", "Victory", location_type = SpyroLocation, item_type = items.SpyroItem
        )