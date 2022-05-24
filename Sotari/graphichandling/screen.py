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

        self.Show()

    def on_press_worlds(self, event):
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