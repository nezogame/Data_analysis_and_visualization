import numpy as np
import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class EmpiricalDistributionPlot(BasePlot):
    def __init__(self, frame, title, data):
        super().__init__(frame, title, data)

    def plot(self):
        self.ax.step(self.data[0] , self.data[1], where="pre")
        self.ax.set_title(self.title)
        self.figure.set_dpi(85)
        self.figure.set_size_inches(5, 5)
        plt.xlabel('Data Values')
        plt.ylabel('Empirical Distribution Function (EDF)')
        plt.grid(True)

    def create_plot(self,canvas):
        plt.tight_layout()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self.frame)
        toolbar.update()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def get_frame(self):
        return self.frame