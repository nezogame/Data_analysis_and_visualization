import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

class ProbabilityPaper(BasePlot):
    def __init__(self, frame, title, data):
        data[0].pop()
        data[1].pop()
        super().__init__(frame, title, data)

    def plot(self):
        self.ax.scatter(self.data[0], self.data[1], zorder=2)
        self.figure.set_dpi(65)
        self.figure.set_size_inches(6, 6)
        plt.grid(True)
        plt.ylabel("Quantile FN(x)")
        plt.xlabel("X value")
        self.ax.set_title(self.title)


    def create_plot(self, canvas):
        plt.tight_layout()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.frame)
        toolbar.update()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_bandwidth(self):
        return self.bandwidth

    def get_frame(self):
        return self.frame