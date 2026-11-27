class LifeChest():
    name: str
    offset: int
    byte: int
    checked: bool = False
    
    def __init__(self, name, offset, bit):
        self.name = name
        self.offset = offset
        self.bit = bit
        

class Level():
    name: str
    internelID: int
    isHub: bool = False
    complete: bool = False
    nameOffset: int
    gemsOffset: int
    gemsTotal: int = 0
    gemsMax: int
    dragonsOffset: int
    dragonsMax: int
    dragonsTotal: int = 0
    eggsOffset: int
    eggsMax: int
    eggsTotal: int = 0
    connectedLevelIDs: list[int] = []
    connectedLevelIDOffsets : list[int] = []
    life_chests: list[LifeChest] = []
    
    def __init__(self, name, internalID, nameOffset, gemsOffset, gemsMax, dragonsOffset = 0, dragonsMax = 0, eggsOffset = 0, eggsMax = 0):
        self.name = name
        self.internalID = internalID
        self.nameOffset = nameOffset
        self.gemsOffset = gemsOffset
        self.gemsMax = gemsMax
        self.dragonsOffset = dragonsOffset
        self.dragonsMax = dragonsMax
        self.eggsOffset = eggsOffset
        self.eggsMax = eggsMax
        
        
levels: dict = {}

levels[10] = Level("ARTISANS", 10, 0x1006C, 0x77420, 100, 0x772d8, 4)
levels[11] = Level("STONE HILL", 11, 0x101FC, 0x77424, 200, 0x772dc, 4, 0x76FEC, 1)
levels[12] = Level("DARK HOLLOW", 12, 0x101F0, 0x77428, 100, 0x772e0, 3)
levels[13] = Level("TOWN SQUARE", 13, 0x101E4, 0x7742c, 200, 0x772e4, 4, 0x76FF4, 1)
levels[14] = Level("TOASTY", 14, 0x75570, 0x77430, 100, 0x772e8, 1)
levels[15] = Level("SUNNY FLIGHT", 15, 0x101D4, 0x77434, 300)
levels[20] = Level("PEACE KEEPERS", 20, 0x1005C, 0x77438, 200, 0x772f0, 3, 0x77000, 1)
levels[21] = Level("DRY CANYON", 21, 0x101C8, 0x7743c, 400, 0x772f4, 4, 0x77004, 1)
levels[22] = Level("CLIFF TOWN", 22, 0x101BC, 0x77440, 400, 0x772f8, 3, 0x77008, 1)
levels[23] = Level("ICE CAVERN", 23, 0x101B0, 0x77444, 400, 0x772fc, 5)
levels[24] = Level("DOCTOR SHEMP", 24, 0x101A0, 0x77448, 300, 0x77300, 1)
levels[25] = Level("NIGHT FLIGHT", 25, 0x10190, 0x7744c, 300)
levels[30] = Level("MAGIC CRAFTERS", 30, 0x1004C, 0x77450, 300, 0x77308, 3, 0x77018, 2)
levels[31] = Level("ALPINE RIDGE", 31, 0x10180, 0x77454, 500, 0x7730c, 4, 0x7701C, 1)
levels[32] = Level("HIGH CAVES", 32, 0x10174, 0x77458, 500, 0x77310, 3, 0x77020, 2)
levels[33] = Level("WIZARD PEAK", 33, 0x10168, 0x7745c, 500, 0x77314, 3, 0x77024, 2)
levels[34] = Level("BLOWHARD", 34, 0x1015C, 0x77460, 400, 0x77318, 1)
levels[35] = Level("CRYSTAL FLIGHT", 35, 0x1014C, 0x77464, 300)
levels[40] = Level("BEAST MAKERS", 40, 0x1003C, 0x77468, 300, 0x77320, 2)
levels[41] = Level("TERRACE VILLAGE", 41, 0x1013C, 0x7746c, 400, 0x77324, 2)
levels[42] = Level("MISTY BOG", 42, 0x10130, 0x77470, 500, 0x77328, 4)
levels[43] = Level("TREE TOPS", 43, 0x10124, 0x77474, 500, 0x7732c, 3)
levels[44] = Level("METALHEAD", 44, 0x10118, 0x77478, 500, 0x77330, 1)
levels[45] = Level("WILD FLIGHT", 45, 0x1010C, 0x7747c, 300)
levels[50] = Level("DREAM WEAVERS", 50, 0x1002C, 0x77480, 300, 0x77338, 3)
levels[51] = Level("DARK PASSAGE", 51, 0x100FC, 0x77484, 500, 0x7733c, 5)
levels[52] = Level("LOFTY CASTLE", 52, 0x100EC, 0x77488, 400, 0x77340, 3)
levels[53] = Level("HAUNTED TOWERS", 53, 0x100DC, 0x7748c, 500, 0x77344, 3)
levels[54] = Level("JACQUES", 54, 0x75568, 0x77490, 500, 0x77348, 2)
levels[55] = Level("ICY FLIGHT", 55, 0x100D0, 0x77494, 300)
levels[60] = Level("GNORC GNEXUS", 60, 0x100C0, 0x77498, 200, 0x77350, 2)
levels[61] = Level("GNORC COVE", 61, 0x100B4, 0x7749c, 400, 0x77354, 2)
levels[62] = Level("TWILIGHT HARBOR", 62, 0x100A4, 0x774a0, 400, 0x77358, 2)
levels[63] = Level("GNASTY GNORC", 63, 0x10094, 0x774A4, 500)
levels[64] = Level("GNASTYS LOOT", 64, 0x10084, 0x774A8, 2000)
        
for level in levels:
    level = levels[level]
    if level.internalID % 10 == 0:
        level.isHub = True
        if level.internalID == 10:
            level.connectedLevelIDs = [11, 12, 13, 14, 15]
            level.connectedLevelIDOffsets = [0xc12b4, 0xc12a8, 0xc12c0, 0xc129c, 0xc12cc]
        elif level.internalID == 20:
            level.connectedLevelIDs = [21, 22, 23, 24, 25]
            level.connectedLevelIDOffsets = [0xbfc48, 0xbfc54, 0xbfc60, 0xbfc6c, 0xbfc78]
        elif level.internalID == 30:
            level.connectedLevelIDs = [31, 32, 33, 34, 35]
            level.connectedLevelIDOffsets = [0xc627c, 0xc6294, 0xc6288, 0xc6264, 0xc6270]
        elif level.internalID == 40:
            level.connectedLevelIDs = [41, 42, 43, 44, 45]
            level.connectedLevelIDOffsets = [0xb558c, 0xb5574, 0xb5580, 0xb5568, 0xb5598]
        elif level.internalID == 50:
            level.connectedLevelIDs = [51, 52, 53, 54, 55]
            level.connectedLevelIDOffsets = [0xc5ecc, 0xc5ee4, 0xc5efc, 0xc5ed8, 0xc5ef0]
        else:
            level.connectedLevelIDs = [61, 62, 63, 64]
            level.connectedLevelIDOffsets = [0xa69d8, 0xa69b4, 0xa69c0, 0xa69cc]
            
levels[10].life_chests = [LifeChest("Artisans: life chest near Dark Hollow portal", 0x77913, 0x40)]
levels[11].life_chests = [LifeChest("Stone Hill: life chest near vortex", 0x7793D, 0x40)]
levels[12].life_chests = [LifeChest("Dark Hollow: life chest glide after staircase", 0x77956, 0x10)]
levels[13].life_chests = [LifeChest("Town Square: life chest near Devlin", 0x77975, 0x04)]
levels[20].life_chests = [LifeChest("Peace Keppers: life chest behind balloonist", 0x779D3, 0x04)]
levels[21].life_chests = [LifeChest("Dry Canyon: life chest near vortex", 0x779FA, 0x04),
                          LifeChest("Dry Canyon: life chest near Ivor",0x779FE, 0x01)]
levels[22].life_chests = [LifeChest("Cliff Town: life chest under double bridge", 0x77A1A, 0x08)]
levels[23].life_chests = [LifeChest("Ice Cavern: life chest group of 3 #2", 0x77A3E, 0x10),
                          LifeChest("Ice Cavern: life chest group of 3 #1", 0x77A3F, 0x04),
                          LifeChest("Ice Cavern: life chest group of 3 #3", 0x77A3F, 0x08),
                          LifeChest("Ice Cavern: life chest near Andor", 0x77A41, 0x20),
                          LifeChest("Ice Cavern: life chest near vortex", 0x77A41, 0x40)]
levels[30].life_chests = [LifeChest("Magic Crafters: life chest glide from High Caves portal", 0x77A8E, 0x40)]
levels[31].life_chests = [LifeChest("Alpine Ridge: life chest in cave near vortex", 0x77ABB, 0x04)]
levels[33].life_chests = [LifeChest("Wizard Peak: life chest top of first supercharge ramp", 0x77AFA, 0x80)]
levels[40].life_chests = [LifeChest("Beast Makers: life chest below Metalhead portal", 0x77B5B, 0x01)]
levels[41].life_chests = [LifeChest("Terrace Village: life chest near Cyprin", 0x77B6F, 0x20),
                          LifeChest("Terrace Village: life chest near Claude", 0x77B7C, 0x02)]
levels[42].life_chests = [LifeChest("Misty Bog: life chest near start behind wall", 0x77B94, 0x40),
                          LifeChest("Misty Bog: life chest near start", 0x77B94, 0x80)]
levels[43].life_chests = [LifeChest("Tree Tops: life chest before Lyle", 0x77BB5, 0x02),
                          LifeChest("Tree Tops: life chest after Issak", 0x77BBD, 0x40),
                          LifeChest("Tree Tops: life chest before vortex", 0x77BBE, 0x01),
                          LifeChest("Tree Tops: life chest after Lyle", 0x77BBE, 0x02)]
levels[44].life_chests = [LifeChest("Metalhead: life chest in sewers", 0x77BD8, 0x80),
                          LifeChest("Metalhead: life chest above start", 0x77BE0, 0x02)]
levels[50].life_chests = [LifeChest("Dream Weavers: life chest near Mazi", 0x77C18, 0x80),
                          LifeChest("Dream Weavers: life chest near Icy Flight portal", 0x77C19, 0x08)]
levels[51].life_chests = [LifeChest("Dark Passage: life chest near vortex", 0x77C34, 0x04),
                          LifeChest("Dark Passage: life chest near Apara", 0x77C36, 0x20)]
levels[52].life_chests = [LifeChest("Lofty Castle: life chest near Mudada", 0x77C5E, 0x02),
                          LifeChest("Lofty Castle: life chest near Useni",0x77C60, 0x10)]
levels[53].life_chests = [LifeChest("Haunted Towers: life chest near second fire fairy", 0x77C7C, 0x01),
                          LifeChest("Haunted Towers: life chest near Lutalo", 0x77C7C, 0x02)]
levels[54].life_chests = [LifeChest("Jacques: life chest near Unika", 0x77C8E, 0x40),
                          LifeChest("Jacques: life chest near Revilo", 0x77C92, 0x01)]
levels[61].life_chests = [LifeChest("Gnorc Cove: life chest near Lateef", 0x77CF6, 0x80),
                          LifeChest("Gnorc Cove: life chest near Tomas", 0x77CFF, 0x20)]
levels[62].life_chests = [LifeChest("Twilight Harbor: life chest near start", 0x77D0C, 0x80),
                          LifeChest("Twilight Harbor: life chest top of supercharge ramp", 0x77D10, 0x20),
                          LifeChest("Twilight Harbor: life chest after supercharge jump", 0x77D16, 0x80)]

index = 269
for level in levels:
    level = levels[level]
    for life_chest in level.life_chests:
        print(f'"{life_chest.name}": {index},')
        index += 1
