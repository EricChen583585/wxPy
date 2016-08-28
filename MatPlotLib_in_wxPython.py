
"""
Python 2.7 | wxPython Classic | MatPlotLib: 1.5.1
This script demo how to embed matplotlib figure into a wxPython GUI.


Author's url: www.UmarYusuf.com


Blog explanation of the script:
http://umar-yusuf.blogspot.com/2016/08/embedding-matplotlib-figure-in-wxpython.html

"""


import wx


# ###########################################################################
# Class for GUI MainFrame
# ###########################################################################

# plotting variables declared outside MainFrame class
# a = [ 0.25, 0.97, 0.59, 0.84, 0.93]
# b = [ 0.52, 0.83, 0.98, 0.28, 0.31, 0.013, 0.29, 0.49, 0.85, 0.80]

class MainFrame(wx.Frame):
    """docstring for MainFrame"""
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title=">>>> by www.UmarYusuf.com", size=(800, 580))

# Add SplitterWindow panels
        self.split_win = wx.SplitterWindow(self)
        # self.top_split = wx.Panel(self.split_win, style=wx.SUNKEN_BORDER)
        self.top_split = MatplotPanel(self.split_win) # This call/link the MatplotPanel and MainFrame classes which replaces the above line
        self.bottom_split = wx.Panel(self.split_win, style=wx.SUNKEN_BORDER)
        self.split_win.SplitHorizontally(self.top_split, self.bottom_split, 480)

# plotting variables declared within MainFrame class
        self.a = [ 0.25, 0.97, 0.59, 0.84, 0.93, 0.83, 0.98, 0.28, 0.31, 0.67]
        self.b = [ 0.52, 0.83, 0.98, 0.28, 0.31, 0.03, 0.29, 0.49, 0.85, 0.80]

# Add some contrls/widgets (StaticText and Buttons)
# Add Text control to the bottom_split window
        self.text1 = wx.StaticText(self.bottom_split, -1, u"You can also plot from file", size=(250, 30), pos=(510, 10), style=wx.ALIGN_CENTER)
        self.text1.SetBackgroundColour('Gray')
        font = wx.Font(15, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.text1.SetFont(font)

# Add Buttons to the bottom_split window and bind them to plot functions
        self.Button1 = wx.Button(self.bottom_split, -1, "Plot1", size=(80, 40), pos=(10, 10))
        self.Button1.Bind(wx.EVT_BUTTON, self.plot1)

        self.Button2 = wx.Button(self.bottom_split, -1, "Plot2", size=(80, 40), pos=(110, 10))
        self.Button2.Bind(wx.EVT_BUTTON, self.plot2)

        self.Button3 = wx.Button(self.bottom_split, -1, "Plot3", size=(80, 40), pos=(210, 10))
        self.Button3.Bind(wx.EVT_BUTTON, self.plot3)

        self.Button4 = wx.Button(self.bottom_split, -1, "Plot4", size=(80, 40), pos=(310, 10))
        self.Button4.Bind(wx.EVT_BUTTON, self.plot4)

        self.Button5 = wx.Button(self.bottom_split, -1, "Plot5", size=(80, 40), pos=(410, 10))
        self.Button5.Bind(wx.EVT_BUTTON, self.plot5)

    def plot1(self, event):
    	self.fig1 = Figure()

        self.ax1f1 = self.fig1.add_subplot(111)
        self.ax1f1.plot(self.a)

        self.ax1f1.set_title("Simple Plot by Button One")
        self.canvas = FigureCanvas(self, -1, self.fig1)



    def plot2(self, event):
    	self.fig2 = Figure()

        self.ax1f2 = self.fig2.add_subplot(121)
        self.ax1f2.plot(self.a)
        self.ax1f2.set_title("First Plot by Button Two")

        self.ax2f2 = self.fig2.add_subplot(122)
        self.ax2f2.plot(self.b)
        self.ax2f2.set_title("Second Plot by Button Two")

        self.canvas = FigureCanvas(self, -1, self.fig2)



    def plot3(self, event):
    	# Pcolormesh for a 10x10 matrix/array
        import numpy as np

        matrix = np.random.rand(10, 10)

        self.fig3 = Figure()
        self.ax1f3 = self.fig3.add_subplot(111)
        self.ax1f3.pcolormesh(matrix)
        self.ax1f3.set_title("Pcolormesh Plot by Button Three")

        self.canvas = FigureCanvas(self, -1, self.fig3)



    def plot4(self, event):
    	self.fig4 = Figure()

        self.ax1f4 = self.fig4.add_subplot(111)
        self.ax1f4.bar(self.a, self.b, 0.05)

        self.ax1f4.set_title("Bar Plot by Button Four")
        self.canvas = FigureCanvas(self, -1, self.fig4)



    def plot5(self, event):
    	self.fig5 = Figure()

        self.ax1f5 = self.fig5.add_subplot(111)
        self.ax1f5.scatter(self.a, self.b, 300)
        
        self.ax1f5.set_title("Scatter Plot by Button Five")
        self.canvas = FigureCanvas(self, -1, self.fig5)



# ###########################################################################
# Class for MatPlotLib Panel
# ###########################################################################

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class MatplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,-1,size=(50,50))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        t = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        s = [0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 1.0, 2.0, 1.0, 0.0]

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)







app = wx.App()
frame = MainFrame(None).Show()
app.MainLoop()
