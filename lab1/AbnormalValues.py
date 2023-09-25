import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from Plot import BasePlot
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class AbnormalValues(BasePlot):
    def __init__(self, frame, title, data):
        super().__init__(frame, title, data)

    def plot(self):
        interval_start = self.find_start_index()
        intreval_end = self.find_end_index()
        self.ax.scatter(self.data[0], self.data[1], zorder=2)
        plt.vlines(x=[interval_start, intreval_end], ymin = min(self.data[1])*0.95, ymax = max(self.data[1])*0.95, color='r')
        self.figure.set_dpi(65)
        self.figure.set_size_inches(6, 6)
        plt.grid(True)
        plt.ylabel('value')
        plt.xlabel('index')
        self.ax.set_title(self.title)

    def find_start_index(self):
        for i, value in enumerate(self.data[1]):
            if value > self.data[2]:
                return i - 1

    def find_end_index(self):
        for i, value in enumerate(self.data[1]):
            if value > self.data[3]:
                return i - 1

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
