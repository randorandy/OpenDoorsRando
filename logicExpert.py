from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places. 
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    Varia, GravitySuit, Wave, SpeedBooster, Spazer, Ice,
    Plasma, Screw, Charge, Grapple, SpaceJump, Energy, Reserve, Xray
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 1
)) 

energy300 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 6
))
energy800 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 7
))
energy900 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve)) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    (loadout.count(Items.Energy) + loadout.count(Items.Reserve))  >= 14
))
hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun7 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))


missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile20 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 20
))


super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 10
))
super30 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 5 >= 30
))
powerBomb15 = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    loadout.count(Items.PowerBomb) *5 >= 15
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and 
    (PowerBomb in loadout)
))
canCF = LogicShortcut(lambda loadout: (
    (missile10 in loadout) and
    (super10 in loadout) and
    (powerBomb15 in loadout)
))

canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout)
))
canHighSBJ = LogicShortcut(lambda loadout: (
    (Springball in loadout) and
    (Morph in loadout) and
    (HiJump in loadout)
))
canFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout)
))
canSpeedOrFly = LogicShortcut(lambda loadout: (
    (canIBJ in loadout) or
    (SpaceJump in loadout) or
    (SpeedBooster in loadout)
))
phantoon = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (
        (Missile in loadout) or
        (Charge in loadout) or
        (Super in loadout) #evil
    )
))
lnRefill = LogicShortcut(lambda loadout: (
    (
        (Varia in loadout) or
        (
            (energy900 in loadout) and
            (canCF in loadout)
        )
        #this is just to have enough energy
    ) and
    (
        (GravitySuit in loadout) or
        (
            (HiJump in loadout) and
            (Energy in loadout)
        )
    )
))
lnBackdoor = LogicShortcut(lambda loadout: (
    (hellrun6 in loadout) and
    (Morph in loadout)
))
maridia = LogicShortcut(lambda loadout: (
    (GravitySuit in loadout) or
    (
        (HiJump in loadout) and
        (
            (Ice in loadout) or
            (canHighSBJ in loadout)
        )
    )
))
aqueduct = LogicShortcut(lambda loadout: (
    (maridia in loadout) or
    (
        (Morph in loadout) and
        (Grapple in loadout) and
        (HiJump in loadout)
    )
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}

location_logic: LocationLogicType = {
    "Crateria Power Bomb": lambda loadout: (
        (canSpeedOrFly in loadout)
    ),
    "Ocean Underwater Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Ocean Sky Missile": lambda loadout: (
        True
    ),
    "Ocean Maze Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Moat Missile": lambda loadout: (
        True
    ),
    "Gauntlet Energy Tank": lambda loadout: (
        True
    ),
    "Old Mother Brain Missile": lambda loadout: (
        True
    ),
    "Bombs": lambda loadout: (
        (Morph in loadout)
    ),
    "Terminator Energy Tank": lambda loadout: (
        True
    ),
    "Gauntlet Right Missile": lambda loadout: (
        True
    ),
    "Gauntlet Left Missile": lambda loadout: (
        True
    ),
    "Climb Super Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "230 Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Etecoons Power Bomb": lambda loadout: (
        (Morph in loadout)
    ),
    "Spore Spawn Super Missile": lambda loadout: (
        (Morph in loadout) or
        (
            (Screw in loadout)
            #more?
        )
    ),
    "Early Supers Bridge Missile": lambda loadout: (
        True
    ),
    "Early Super Missile": lambda loadout: (
        True
    ),
    "Brinstar Reserve Tank": lambda loadout: (
        True
    ),
    "Ron Popeil Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Brinstar Reserve Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Mission Impossible Missile": lambda loadout: (
        True
    ),
    "Charge Missile": lambda loadout: (
        True
    ),
    "Charge Beam": lambda loadout: (
        (Morph in loadout)
    ),
    "Mission Impossible Power Bomb": lambda loadout: (
        True
    ),
    "Green Hill Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Morph Ball": lambda loadout: (
        True
    ),
    "Meme Route Power Bomb": lambda loadout: (
        True
    ),
    "Beta Missile": lambda loadout: (
        True
    ),
    "Brinstar Ceiling Energy Tank": lambda loadout: (
        True
    ),
    "Etecoons Energy Tank": lambda loadout: (
        True
    ),
    "Etecoons Super Missile": lambda loadout: (
        True
    ),
    "Waterway Energy Tank": lambda loadout: (
        (Morph in loadout)
    ),
    "Alpha Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Wave Gate Energy Tank": lambda loadout: (
        True
    ),
    "Billy Mays Missile": lambda loadout: (
        True
    ),
    "Billy Mays More Missile": lambda loadout: (
        True
    ),
    "Xray": lambda loadout: (
        (Morph in loadout)
    ),
    "Beta Power Bomb": lambda loadout: (
        True
    ),
    "Alpha Power Bomb": lambda loadout: (
        True
    ),
    "Alpha Power Bomb Missile": lambda loadout: (
        True
    ),
    "Spazer": lambda loadout: (
        (Morph in loadout)
    ),
    "Kraid Energy Tank": lambda loadout: (
        True
    ),
    "Kraid Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (Morph in loadout) and
        (
            (pinkDoor in loadout) or
            (Charge in loadout)
        )
    ),
    "Cathedral Missile": lambda loadout: (
        (Morph in loadout) and
        (hellrun3 in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (Morph in loadout)
    ),
    "Crumble Shaft Missile": lambda loadout: (
        True
    ),
    "Croc Energy Tank": lambda loadout: (
        (Charge in loadout) or
        (pinkDoor in loadout)
    ),
    "HiJump": lambda loadout: (
        (Morph in loadout)
    ),
    "Croc Escape Missile": lambda loadout: (
        True
    ),
    "HiJump Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "HiJump Energy Tank": lambda loadout: (
        True
    ),
    "Croc Power Bomb": lambda loadout: (
        (Charge in loadout) or
        (pinkDoor in loadout)
    ),
    "Cosine Room Missile": lambda loadout: (
        (Morph in loadout) and
        (
            (Charge in loadout) or
            (pinkDoor in loadout)
        )
    ),
    "Indiana Jones Missile": lambda loadout: (
        (
            (Grapple in loadout) or
            (canSpeedOrFly in loadout) or
            (Morph in loadout)
        ) and
        (
            (Charge in loadout) or
            (pinkDoor in loadout)
        )
    ),
    "Grapple Beam": lambda loadout: (
        (Charge in loadout) or
        (pinkDoor in loadout)
    ),
    "Norfair Reserve Tank": lambda loadout: (
        (Morph in loadout) and
        (hellrun3 in loadout)
    ),
    "Norfair Reserve Missile": lambda loadout: (
        (Morph in loadout) and
        (hellrun3 in loadout)
    ),
    "Norfair Reserve Front Missile": lambda loadout: (
        True
    ),
    "Bubble Mountain Missile": lambda loadout: (
        True
    ),
    "Speed Missile": lambda loadout: (
        (hellrun3 in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (hellrun3 in loadout)
    ),
    "Wave Missile": lambda loadout: (
        (hellrun3 in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (
            (Morph in loadout) or
            (Grapple in loadout) or
            (SpaceJump in loadout)
        ) and
        (hellrun4 in loadout)
    ),
    "Gold Torizo Missile": lambda loadout: (
        (lnRefill in loadout)
    ),
    "Gold Torizo Super Missile": lambda loadout: (
        (lnRefill in loadout)
    ),
    "Mickey Mouse Missile": lambda loadout: (
        (lnRefill in loadout)
    ),
    "Hotarubi Missile": lambda loadout: (
        (lnBackdoor in loadout)
    ),
    "Jail Power Bomb": lambda loadout: (
        (lnBackdoor in loadout) 
    ),
    "Wasteland Power Bomb": lambda loadout: (
        (lnBackdoor in loadout)
    ),
    "Three Musketeers Missile": lambda loadout: (
        (lnBackdoor in loadout)
    ),
    "Ridley Energy Tank": lambda loadout: (
        (lnBackdoor in loadout) and
        (lnRefill in loadout) and
        (
            (
                (Charge in loadout) and
                (Varia in loadout)
            ) or
            (super30 in loadout)
        )      
    ),
    "Screw Attack": lambda loadout: (
        (lnRefill in loadout)
    ),
    "Firefleas Energy Tank": lambda loadout: (
        (lnBackdoor in loadout)
    ),
    "Spooky Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Wrecked Ship Reserve Tank": lambda loadout: (
        (Morph in loadout)
    ),
    "Gravity Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Attic Missile": lambda loadout: (
        (phantoon in loadout)
    ),
    "Wrecked Ship Energy Tank": lambda loadout: (
        (phantoon in loadout)
    ),
    "Wrecked Ship Left Super Missile": lambda loadout: (
        (phantoon in loadout)
    ),
    "Wrecked Ship Right Super Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Gravity Suit": lambda loadout: (
        (phantoon in loadout)
    ),
    "Main Street Missile": lambda loadout: (
        (maridia in loadout) or
        (
            (Morph in loadout) and
            (Grapple in loadout) and
            (HiJump in loadout)
        )
    ),
    "Crab Super Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Mama Turtle Energy Tank": lambda loadout: (
        (maridia in loadout) or
        (
            (Morph in loadout) and
            (HiJump in loadout) and
            (
                (Grapple in loadout) or
                (canIBJ in loadout) or
                (SpeedBooster in loadout)
            )        
        )
    ),
    "Mama Turtle Missile": lambda loadout: (
        (maridia in loadout) or
        (
            (Morph in loadout) and
            (HiJump in loadout)
        )
    ),
    "Watering Hole Super Missile": lambda loadout: (
        (maridia in loadout) and
        (aqueduct in loadout) and
        (Morph in loadout)
    ),
    "Watering hole Missile": lambda loadout: (
        (aqueduct in loadout) and
        (maridia in loadout) and
        (Morph in loadout)
    ),
    "Beach Missile": lambda loadout: (
        (maridia in loadout) and
        (aqueduct in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (maridia in loadout) and
        (
            (canSpeedOrFly in loadout) or
            (HiJump in loadout)
        )
    ),
    "Left Sand Pit Missile": lambda loadout: (
        (aqueduct in loadout) and
        (Morph in loadout)
    ),
    "Maridia Reserve Tank": lambda loadout: (
        (aqueduct in loadout) and
        (Morph in loadout)
    ),
    "Right Sand Pit Missile": lambda loadout: (
        (aqueduct in loadout)
    ),
    "Right Sand Pit Power Bomb": lambda loadout: (
        (aqueduct in loadout) and
        (Morph in loadout) and
        (
            (GravitySuit in loadout) or
            (canHighSBJ in loadout)
        )
    ),
    "Aqueduct Missile": lambda loadout: (
        (aqueduct in loadout)
    ),
    "Aqueduct Super Missile": lambda loadout: (
        (aqueduct in loadout)
    ),
    "Springball": lambda loadout: (
        (Morph in loadout) and
        (
            (
                (HiJump in loadout) and
                (Springball in loadout) 
            ) or
            (
                (GravitySuit in loadout) and
                (canUseBombs in loadout)
            )
        ) and
        (
            (
                (HiJump in loadout) and
                (Ice in loadout)
            ) or
            (GravitySuit in loadout)
        )
    ),
    "Precious Missile": lambda loadout: (
        (maridia in loadout) and
        (aqueduct in loadout) and
        (
            (Morph in loadout) or
            (GravitySuit in loadout)
        )
    ),
    "Botwoon Energy Tank": lambda loadout: (
        (maridia in loadout) and
        (aqueduct in loadout) and
        (Morph in loadout) and
        (
            (Charge in loadout) or
            (super10 in loadout)
        )
    ),
    "Space Jump": lambda loadout: (
        (maridia in loadout) and
        (Morph in loadout) and
        (
            (GravitySuit in loadout) or
            (
                (Grapple in loadout) and
                (canCF in loadout)
            ) or
            (canHighSBJ in loadout)
        )
    ),

}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
