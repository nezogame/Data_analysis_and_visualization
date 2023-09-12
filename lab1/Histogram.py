import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
import numpy as np
from tkinter import ttk
from collections import OrderedDict
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BarPlot(BasePlot):
    def __init__(self, frame, title, data):
        super().__init__(frame, title, data)

    def plot(self):
        self.ax.bar(self.data[0], self.data[1])
        self.ax.set_title(self.title)


    def create_plot(self,frame):
        canvas = FigureCanvasTkAgg(self.figure, master=frame)

        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



    def get_frame(self):
        return self.frame


