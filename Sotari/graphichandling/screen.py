import wx
import wx.lib.scrolledpanel as scrolled
from realityhandling.saves import *
import subprocess
import sys
import pickle
import os
import tkinter
from tkinter import filedialog
from realityobjects.itemframework import *
from realityobjects.worldframework import *
from realityobjects.player import *
from realityobjects.nonplayercharacter import *
from realityhandling.saves import *


class MyFrame(wx.Frame):
    def __init__(self, save):
        self.save = save
        save.Log("Initializing Screen")
        super().__init__(parent=None, title='Unnamed TTRPG System')
        panel = wx.Panel(self)
        self.panel = panel

        self.SetMinSize(wx.Size(450, 240))


        task_panel = wx.Panel(self, -1, size=(self.Size[0], 50), pos=(0,0), style=wx.SIMPLE_BORDER)
        self.task_panel = task_panel

        worlds_button = wx.Button(task_panel, label='Worlds', pos=(5, 5))
        worlds_button.Bind(wx.EVT_BUTTON, self.on_press_worlds)

        items_button = wx.Button(task_panel, label='Items', pos=(5, 5))
        items_button.Bind(wx.EVT_BUTTON, self.on_press_items)

        settings_button = wx.Button(task_panel, label='Settings', pos=(85, 5))
        settings_button.Bind(wx.EVT_BUTTON, self.on_press_settings)

        export_button = wx.Button(task_panel, label='Export', pos=(165, 5))
        export_button.Bind(wx.EVT_BUTTON, self.on_press_export)

        import_button = wx.Button(task_panel, label='Import', pos=(245, 5))
        import_button.Bind(wx.EVT_BUTTON, self.on_press_import)


        tSizer = wx.BoxSizer( wx.HORIZONTAL )
        tSizer.Add( worlds_button, 0, wx.ALL, 5 )
        tSizer.Add( items_button, 0, wx.ALL, 5 )
        tSizer.Add( settings_button, 0, wx.ALL, 5 )
        tSizer.Add( export_button, 0, wx.ALL, 5 )
        tSizer.Add( import_button, 0, wx.ALL, 5 )
        task_panel.SetSizer( tSizer )


        worlds_scroll = scrolled.ScrolledPanel(self,-1, size=(110,self.Size[1] - 50), pos=(0,50), style=wx.SIMPLE_BORDER)
        self.worlds_scroll = worlds_scroll
        worlds_scroll.SetupScrolling()
        worlds_scroll.SetBackgroundColour('#FFFFFF')

        export_options = scrolled.ScrolledPanel(self,-1, size=(110,self.Size[1] - 50), pos=(0,50), style=wx.SIMPLE_BORDER)
        self.export_options = export_options
        export_options.SetupScrolling()
        export_options.SetBackgroundColour('#FFFFFF')

        export_options.Hide()

        self.worlds_scroll_options = []
        self.export_options_list = []

        for i in self.save.worlds:
            self.worlds_scroll_options.append(wx.Button(worlds_scroll,label=i.name,pos=(0,50),size=(80,50)))

        for i in self.save.worlds:
            button = wx.Button(export_options,label=i.name,pos=(0,50),size=(80,50))
            button.world = i
            self.export_options_list.append(button)
            button.Bind(wx.EVT_BUTTON, lambda evt, temp = i: self.modal_export(evt, temp))


        self.new_world_button = wx.Button(worlds_scroll,label="New World",pos=(0,50),size=(80,50))
        self.new_world_button.Bind(wx.EVT_BUTTON, self.press_new_world)




        bSizer = wx.BoxSizer( wx.VERTICAL )
        self.bSizer = bSizer
        for i in self.worlds_scroll_options:
            bSizer.Add(i, 0, wx.ALL, 5)
        bSizer.Add(self.new_world_button, 0, wx.ALL, 5)
        worlds_scroll.SetSizer( bSizer )

        exportsizer = wx.BoxSizer( wx.VERTICAL )
        self.exportsizer = exportsizer
        for i in self.export_options_list:
            exportsizer.Add(i, 0, wx.ALL, 5)
        export_options.SetSizer( exportsizer )

        self.Bind(wx.EVT_SIZE, self.size_change)
        self.Show()

    def size_change(self, event):
        self.size_change_call()

    def size_change_call(self):
        self.task_panel.SetSize(self.Size[0], 50)
        self.worlds_scroll.SetSize(110,self.Size[1] - 50)
        self.export_options.SetSize(110,self.Size[1] - 50)

    def press_new_world(self, event):
        try:
            # Get and store world name entry
            dlg = wx.TextEntryDialog(self, 'Enter New World Name', '')
            dlg.SetValue("")
            value = ""

            if dlg.ShowModal() == wx.ID_OK:
                if wx.MessageBox(
                    "Would you like to build this world from scratch?"
                    , "World Wizard",
                     wx.YES_NO | wx.NO_DEFAULT, self) == wx.NO:

                    self.save.worlds.append(World(dlg.GetValue(), False))
                else:
                    pass
                value = dlg.GetValue()
                Dump(self.save)
            dlg.Destroy()

            button = wx.Button(self.worlds_scroll, label=value, pos=(0, 50), size=(80, 50))
            self.worlds_scroll_options.append(button)
            self.bSizer.Add(button, 0, wx.ALL, 5)

            button2 = wx.Button(self.export_options, label=value, pos=(0, 50), size=(80, 50))
            self.export_options_list.append(button2)
            self.exportsizer.Add(button2, 0, wx.ALL, 5)

            self.size_change_call()

        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to create new world:")
            self.save.lof(e)

    def on_press_worlds(self, event):
        try:
            self.worlds_scroll.Show()
            self.export_options.Hide()
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open worlds dialogue:")
            self.save.lof(e)

    def on_press_settings(self, event):
        try:
            self.worlds_scroll.Hide()
            self.export_options.Hide()
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open settings dialogue:")
            self.save.lof(e)

    def modal_export(self, event, world):
        # Following Code borrowed from user Simimic
        # https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python
        tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
        folder_path = filedialog.askdirectory()

        with open(folder_path + "\\" + world.name + ".txt", 'wb') as config_dictionary_file:
            pickle.dump(world, config_dictionary_file)




    def on_press_export(self, event):
        self.worlds_scroll.Hide()
        self.export_options.Show()

    def on_press_import(self, event):
        try:
            self.worlds_scroll.Hide()
            self.export_options.Hide()

            # Following Code borrowed from user Simimic
            # https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python
            tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
            folder_path = filedialog.askopenfile()

            with open(folder_path.name, 'rb') as config_dictionary_file:
                self.save.worlds.append(pickle.load(config_dictionary_file))
            Dump(self.save)
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to import save file:")
            self.save.lof(e)

    def on_press_items(self, event):
        pass


class Application:
    save = Load()
    for i in save.log:
        print(i)
    Dump(save)

    app = wx.App()
    frame = MyFrame(save)
    frame.Show()

    app.MainLoop()