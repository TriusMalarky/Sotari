from realityobjects.itemframework import *
from realityobjects.worldframework import *

def debugtest():

    print(" ==| Sotari Test Functions |==")

    # Test Items
    print(" -- Item Tests --")
    print(" > Creating 'Chair' example object, inherits Item class")
    chair = Item("chair")
    print(" > > Chair Name: " + chair.name)
    print(" > > Chair Value: " + str(chair.value))


    print(" > Creating 'Hat' example object, inherits Equipment class")
    hat = Equipment("hat")
    print(" > > Hat Name: " + hat.name)
    print(" > > Hat Value: " + str(hat.value))
    print(" > > Hat Sus: " + str(hat.sus))


    print(" > Creating 'Sword' example object, inherits Weapon class")
    sword = Weapon("sword")
    print(" > > Sword Name: " + sword.name)
    print(" > > Sword Value: " + str(sword.value))

    # World Tests
    print(" -- World Tests --")
    world = World("ham", False)
    print(" > Number of Continents: " + str(len(world.continents)))
    print(" > Printing Continent Names")
    for i in world.continents:
        print(i.name)
        print("No. Regions: " + str(len(i.regions)))
