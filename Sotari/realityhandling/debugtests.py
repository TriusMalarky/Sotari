from realityobjects.itemframework import *
from realityobjects.worldframework import *
from realityobjects.player import *
from realityobjects.nonplayercharacter import *

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
    hat.set_suspicious(5)
    print(" > > Hat Sus after setting it to 5: " + str(hat.sus))


    print(" > Creating 'Sword' example object, inherits Weapon class")
    sword = Weapon("sword")
    print(" > > Sword Name: " + sword.name)
    print(" > > Sword Value: " + str(sword.value))
    sword.set_suspicious(7)
    print(" > > Sword Sus: " + str(sword.sus))

    # World Tests
    print(" -- World Tests --")
    world = World("ham", False)
    print(" > Number of Continents: " + str(len(world.continents)))
    print(" > Printing Continent Names")
    for i in world.continents:
        print(i.name)
        print("No. Regions: " + str(len(i.regions)))

    # Player Tests
    print(" -- Player Tests --")
    player = Player()
    print(" > Player's default name: " + player.name)
    player.set_name("Tergrid")
    print(" > Player's name after setting it to Tergrid: " + player.name)
    print(" > Player's initial physical stat: " + str(player.get_stat('physical')))
    player.increment_stat('physical')
    print(" > Player's physical stat after incrementing: " + str(player.get_stat('physical')))
    player.increment_stat('physical')
    player.increment_stat('physical')
    player.increment_stat('physical')
    player.increment_stat('physical')
    print(" > Player's physical stat after incrementing several times: " + str(player.get_stat('physical')))
    player.set_stat('physical', 3)
    print(" > Player's physical stat after setting it to 3: " + str(player.get_stat('physical')))
