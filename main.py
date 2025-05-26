import tkinter as tk
from gui import GUI
from queue import Queue

class NIDS:
    def __init__(self, root):
        self.root = root
        self.packet_queue = Queue()
        self.analysis_queue = Queue()
        self.gui = GUI(self.root, self.packet_queue, self.analysis_queue)

if __name__ == "__main__":
    root = tk.Tk()
    nids = NIDS(root)
    root.mainloop()
