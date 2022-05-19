from realityobjects.itemframework import *

def debugtest():

    # Test Items
    chair = Item("chair")
    print(chair.value)

    hat = Equipment("hat")
    print(hat.value)

    sword = Weapon("sword")
    print(sword.value)

    print(chair.name+hat.name+sword.name)