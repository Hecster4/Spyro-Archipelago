from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as spyro_options  # rename due to a name conflict with World.options

class SpyroWorld(World):
    game = "Spyro the Dragon"
    
    web = web_world.SpyroWebWorld()
    
    options_dataclass = spyro_options.SpyroOptions
    options: spyro_options.SpyroOptions
    
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    
    origin_region_name = "Artisans"
    
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)
        
    def create_item(self, name: str) -> items.SpyroItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "deathlink", "portal_locks", "starting_levels", "include_gnastys_loot"
        )
