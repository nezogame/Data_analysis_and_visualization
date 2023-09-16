import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from Plot import BasePlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from scipy import stats
from scipy.stats import gaussian_kde

class KernelDensityEstimatePlot(BasePlot):
    def __init__(self, frame, title, data, class_width):
        self.bandwidth = np.std(data) * len(data) ** (-1/5)
        self.class_width = class_width
        super().__init__(frame, title, data)

    def plot(self):
        kde = gaussian_kde(self.data, bw_method=self.bandwidth)
        x_values = np.linspace(min(self.data), max(self.data), 100)
        kde_values = kde(x_values) * self.class_width
        self.ax.clear()
        self.ax.plot(x_values, kde_values, color='red')
        self.ax.set_title(self.title)
        self.figure.set_dpi(85)
        self.figure.set_size_inches(5, 5)
        plt.xlabel('Data Values')
        plt.ylabel('Kernel density estimation (KDE)')
        plt.grid(True)

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

