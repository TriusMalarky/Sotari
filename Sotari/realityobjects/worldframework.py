from realityhandling.naming import regionname
from realityhandling.naming import continentname
import random
import wx
from realityhandling.saves import *

class World:
    def __init__(self, name, custom):
        self.name = name
        self.continents = []

        if not custom:
            regionsleft = 1000
            for i in range(random.randint(5, 11)):
                continentsize = random.randint(5, 50)
                while continentsize > regionsleft:
                    continentsize -= 1
                regionsleft -= continentsize
                self.continents.append(Continent(continentname(), continentsize))

    def wizard(self, screen):
        if wx.MessageBox(
            "Testthing"
            , "World Wizard",
            wx.YES_NO | wx.NO_DEFAULT, screen) == wx.NO:
            pass
        self.wizard_continents(screen)

    def wizard_continents(self, screen):
        nument = wx.NumberEntryDialog(screen, "How many continents are in " + self.name + "?", "", "World Wizard", 3, 1, 20)
        value = 1
        if nument.ShowModal() == wx.ID_OK:
            value = nument.GetValue()

        for i in range(value):
            getcontname = wx.TextEntryDialog(screen, 'What is the name for continent #' + str(i+1) + "?", 'World Wizard')
            getcontname.SetValue("")
            contname = ""
            if getcontname.ShowModal() == wx.ID_OK:
                contname = getcontname.GetValue()

            getcontsize = wx.NumberEntryDialog(screen, "How many regions are in " + contname + "?", "", "World Wizard",
                                          15, 1, 50)
            contsize = 15
            if getcontsize.ShowModal() == wx.ID_OK:
                contsize = getcontsize.GetValue()

            self.continents.append(Continent(contname, contsize))


class Continent:
    def __init__(self, name, size):
        self.name = name
        self.regions = []
        for i in range(size):
            self.regions.append(Region(regionname()))

class Island:
    def __init__(self, name):
        self.name = name
        self.region = Region(name)

class Region:
    def __init__(self, name):
        self.name = name

class Nation:
    def __init__(self, name):
        self.name = name