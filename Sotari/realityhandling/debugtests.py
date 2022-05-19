from realityobjects.itemframework import *

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


    print(" > Creating 'Sword' example object, inherits Weapon class")
    sword = Weapon("sword")
    print(" > > Sword Name: " + sword.name)
    print(" > > Sword Value: " + str(sword.value))
