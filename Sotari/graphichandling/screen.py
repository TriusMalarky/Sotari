import wx
import wx.lib.scrolledpanel as scrolled
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

        self.SetMinSize(wx.Size(360, 240))


        task_panel = wx.Panel(self, -1, size=(self.Size[0], 50), pos=(0,0), style=wx.SIMPLE_BORDER)
        self.task_panel = task_panel

        worlds_button = wx.Button(task_panel, label='Worlds', pos=(5, 5))
        worlds_button.Bind(wx.EVT_BUTTON, self.on_press_worlds)

        settings_button = wx.Button(task_panel, label='Settings', pos=(85, 5))
        settings_button.Bind(wx.EVT_BUTTON, self.on_press_settings)

        export_button = wx.Button(task_panel, label='Export', pos=(165, 5))
        export_button.Bind(wx.EVT_BUTTON, self.on_press_export)

        import_button = wx.Button(task_panel, label='Import', pos=(245, 5))
        import_button.Bind(wx.EVT_BUTTON, self.on_press_import)


        tSizer = wx.BoxSizer( wx.HORIZONTAL )
        tSizer.Add( worlds_button, 0, wx.ALL, 5 )
        tSizer.Add( settings_button, 0, wx.ALL, 5 )
        tSizer.Add( export_button, 0, wx.ALL, 5 )
        tSizer.Add( import_button, 0, wx.ALL, 5 )
        task_panel.SetSizer( tSizer )


        worlds_scroll = scrolled.ScrolledPanel(self,-1, size=(100,self.Size[1] - 50), pos=(0,50), style=wx.SIMPLE_BORDER)
        self.worlds_scroll = worlds_scroll
        worlds_scroll.SetupScrolling()
        worlds_scroll.SetBackgroundColour('#FFFFFF')


        button1 = wx.Button(worlds_scroll,label="Button 1",pos=(0,50),size=(50,50))
        button2 = wx.Button(worlds_scroll,label="Button 2",pos=(0,100), size=(50,50))
        button3 = wx.Button(worlds_scroll,label="Button 3",pos=(0,150),size=(50,50))
        button4 = wx.Button(worlds_scroll,label="Button 4",pos=(0,200), size=(50,50))
        button5 = wx.Button(worlds_scroll,label="Button 5",pos=(0,250),size=(50,50))
        button6 = wx.Button(worlds_scroll,label="Button 6",pos=(0,300), size=(50,50))
        button7 = wx.Button(worlds_scroll,label="Button 7",pos=(0,350), size=(50,50))
        button8 = wx.Button(worlds_scroll,label="Button 8",pos=(0,400), size=(50,50))



        bSizer = wx.BoxSizer( wx.VERTICAL )
        bSizer.Add( button1, 0, wx.ALL, 5 )
        bSizer.Add( button2, 0, wx.ALL, 5 )
        bSizer.Add( button3, 0, wx.ALL, 5 )
        bSizer.Add( button4, 0, wx.ALL, 5 )
        bSizer.Add( button5, 0, wx.ALL, 5 )
        bSizer.Add( button6, 0, wx.ALL, 5 )
        bSizer.Add( button7, 0, wx.ALL, 5 )
        bSizer.Add( button8, 0, wx.ALL, 5 )
        worlds_scroll.SetSizer( bSizer )

        self.Bind(wx.EVT_SIZE, self.size_change)
        self.Show()

    def size_change(self, event):
        self.task_panel.SetSize(self.Size[0], 50)
        self.worlds_scroll.SetSize(100,self.Size[1] - 50)

    def on_press_worlds(self, event):
        try:
            self.worlds_scroll.Show()
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open worlds dialogue:")
            self.save.lof(e)

    def on_press_settings(self, event):
        try:
            self.worlds_scroll.Hide()
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to open settings dialogue:")
            self.save.lof(e)

    def on_press_export(self, event):
        try:
            pass
        # General exception to get log added to save
        except Exception as e:
            self.save.log(" - Unknown Error when attempting to select exportable world:")
            self.save.lof(e)

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