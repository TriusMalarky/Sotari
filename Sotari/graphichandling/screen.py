import wx
from realityhandling.saves import *

class MyFrame(wx.Frame):
    def __init__(self, save):
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
        pass

    def on_press_settings(self, event):
        pass

    def on_press_export(self, event):
        pass

    def on_press_import(self, event):
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