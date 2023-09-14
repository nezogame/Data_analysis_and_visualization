import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Histogram import BarPlot
from EDF import EmpiricalDistributionPlot

class Graph:
    def __init__(self, root):
        self.controller_window = tk.Toplevel(root)
        self.controller_window.withdraw()
        self.controller_window.title("Plot Controller")
        self.controller_window.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.container = ttk.Frame(self.controller_window)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.distribution_data = None
        self.frequncy_data = None
        self.__histogram: ttk.Frame = None
        self.__empirical_function: ttk.Frame = None

    def create_histogram(self, title):
        if self.__histogram:
            for widget in self.__histogram.winfo_children():
                widget.destroy()
        self.__histogram = self.create_graph(BarPlot, title, self.distribution_data,[0, 0])

    def create_empirical_distribution_function(self, title):
        if self.__empirical_function:
            for widget in self.__empirical_function.winfo_children():
                widget.destroy()
        self.__empirical_function = self.create_graph(EmpiricalDistributionPlot, title, self.frequncy_data,[0, 2])
    def create_graph(self, plot_type, title, data, place):
        frame = ttk.Frame(self.container)
        frame.grid(row=place[0], column=place[1])
        plot = plot_type(frame, title, data)
        canvas = FigureCanvasTkAgg(plot.figure, master=frame)
        plot.create_plot(canvas)
        return frame

    def hide_window(self):
        self.controller_window.withdraw()

    def destroy_window(self):
        self.controller_window.destroy()
        self.controller_window.quit()

    def display_histogram(self, title):
        self.create_histogram(title)
        self.controller_window.deiconify()

    def display_empirical_function(self, title):
        self.create_empirical_distribution_function(title)
        self.controller_window.deiconify()
    def get_distribution_data(self):
        return self.distribution_data

    def set_distribution_data(self, data):
        self.distribution_data = data

    def get_frequncy_data(self):
        return self.frequncy_data

    def set_frequncy_data(self, data):
        self.frequncy_data = data

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()
