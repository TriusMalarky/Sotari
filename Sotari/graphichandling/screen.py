import wx
from realityhandling.saves import *
import subprocess
import sys
import pickle
import os
import tkinter
from tkinter import filedialog



class MyFrame(wx.Frame):
    def __init__(self, save):
        self.save = save
        save.Log("Initializing Screen")
        super().__init__(parent=None, title='Unnamed TTRPG System')
        panel = wx.Panel(self)

        #self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        worlds_button = wx.Button(panel, label='Worlds', pos=(5, 5))
        worlds_button.Bind(wx.EVT_BUTTON, self.on_press_worlds)

        settings_button = wx.Button(panel, label='Settings', pos=(85, 5))
        settings_button.Bind(wx.EVT_BUTTON, self.on_press_settings)

        export_button = wx.Button(panel, label='Export', pos=(165, 5))
        export_button.Bind(wx.EVT_BUTTON, self.on_press_export)

        import_button = wx.Button(panel, label='Import', pos=(245, 5))
        import_button.Bind(wx.EVT_BUTTON, self.on_press_import)


        self.Show()

    def on_press_worlds(self, event):
        try:
            pass
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open worlds dialogue:")
            self.save.lof(e)

    def on_press_settings(self, event):
        try:
            pass
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open settings dialogue:")
            self.save.lof(e)

    def on_press_export(self, event):
        try:
            # Following Code borrowed from user Simimic
            # https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python
            tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
            folder_path = filedialog.askdirectory()

            with open(folder_path + "\\testsave.txt", 'wb') as config_dictionary_file:
                pickle.dump(self.save, config_dictionary_file)

        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to export save file:")
            self.save.lof(e)

    def on_press_import(self, event):
        try:
            pass
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to import save file:")
            self.save.lof(e)




class Application:

    save = Load()
    for i in save.log:
        print(i)
    Dump(save)

    app = wx.App()
    frame = MyFrame(save)
    frame.Show()




    app.MainLoop()