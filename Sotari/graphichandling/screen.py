import wx

class Application:
    app = wx.App()
    frame = wx.Frame(parent=None, title='Sotari')
    frame.Show()
    app.MainLoop()