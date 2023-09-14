import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

from tkinter import ttk
from collections import OrderedDict
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Window import Singleton

class BarPlot(BasePlot):
    def __init__(self, frame, title, data):
        super().__init__(frame, title, data)

    def plot(self):
        self.ax.bar(self.data[0] , self.data[1], width =0.5, zorder=2)
        self.figure.set_dpi(85)
        self.figure.set_size_inches(5, 5)
        plt.xticks(rotation=30, ha='right')
        plt.grid(axis='y', zorder=0)
        self.ax.set_title(self.title)

    def create_plot(self,canvas):
        plt.tight_layout()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.frame)
        toolbar.update()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_frame(self):
        return self.frame