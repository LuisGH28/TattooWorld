import tkinter as tk
import tattooists
  
  
class NewWindow(tk.Frame): 

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "Open"
        self.button["command"] = self.open
        self.button.pack()

    def open(self):
        tattooists(self.master)
  
root = tk.Tk()
app = NewWindow(master=root)
app.mainloop()