import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

from GaussianKDE import GaussianKDE
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class BarPlot(BasePlot):
    def __init__(self, frame, title, data, original_data, class_width):
        self.bandwidth = np.std(original_data) * len(original_data) ** (-1/5)
        self.class_width = class_width
        self.original_data = original_data
        super().__init__(frame, title, data)

    def plot(self):
        kde = GaussianKDE(self.original_data, self.bandwidth)
        x_values = np.linspace(min(self.original_data), max(self.original_data), 100)
        kde_values = [x * self.class_width for x in kde.estimate_density(x_values)]
        self.ax.clear()
        self.ax.bar(self.data[0] , self.data[1], width =self.class_width, zorder=2)
        self.ax.plot(x_values, kde_values, color='red')
        self.figure.set_dpi(85)
        self.figure.set_size_inches(5, 5)
        plt.grid(axis='y', zorder=0)
        plt.ylabel('Freuency')
        self.ax.set_title(self.title)

    def create_plot(self,canvas):
        plt.tight_layout()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.frame)
        toolbar.update()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def set_bandwidth(self, new_bandwidth, canvas:FigureCanvasTkAgg):
        self.bandwidth = new_bandwidth
        self.plot()
        self.create_plot(canvas)

    def get_bandwidth(self):
        return self.bandwidth

    def get_frame(self):
        return self.frame