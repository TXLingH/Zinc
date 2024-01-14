import ttkbootstrap as ttk

"""
Zinc -- 一个基于 ttkbootstrap 项目的改进版本

项目地址: 
"""

class _baseMetmod:
    def __init__(self, **options):
        self.frameworkObject = None
        self.master = options["master"]
        self.text = options["text"]
        self.length = options["length"]
    
    def packObject(self, side = None):
        self.frameworkObject.pack(side = side)
    
    def createGrid(self, row = None, col = None):
        self.frameworkObject.grid(row = row, column = col)
    
    def placeMetmod(self, **loca):
        x = loca["x"] ; y = loca["y"]
        relx = loca["relx"] ; rely = loca["rely"]
        relwidth = loca["relwidth"] ; relheigh = loca["relheigh"]


class Widgets:
    class Button(_baseMetmod):
        def __init__(self, **options):
            super.__init__()
            self.command = options["command"]
            self.frameworkObject = ttk.Button(master=self.master, text = self.text, width = self.length, command = self.command)
    
    class Label(_baseMetmod):
        def __init__(self, **options):
            super.__init__()
            self.frameworkObject = ttk.Label(master = self.master, text = self.text, width = self.length)
    
    class Frame(_baseMetmod):
        def __init__(self, **options):
            super.__init__()
            self.frameworkObject = ttk.Frame(master = self.master)
    

class Window:
    def __init__(self, titleName = "", themename = "simplex"):
        self.window = ttk.Window(themename = themename)
        self.window.attributes("-fullscreen", True)

        ttk.Button(self.window, text = "Hello").pack()
    
    def windowLaunch(self):
        self.window.mainloop()


window = Window()
window.windowLaunch()