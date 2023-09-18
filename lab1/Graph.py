import tkinter as tk
from tkinter import ttk

from EDF import EmpiricalDistributionPlot
from Histogram import BarPlot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, root):
        self.controller_window = tk.Toplevel(root)
        self.controller_window.withdraw()
        self.controller_window.title("Plot Controller")
        self.controller_window.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.current_bandwidth = tk.StringVar(self.controller_window)
        self.bandwidth_entry = tk.Entry(self.controller_window, textvariable=self.current_bandwidth)
        self.bandwidth_entry.pack(side=tk.TOP)
        self.bandwidth_button = tk.Button(self.controller_window, text="Update Bandwidth", command=self.update_bandwidth )
        self.bandwidth_button.pack(side=tk.TOP)
        self.container = ttk.Frame(self.controller_window)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.distribution_data = None
        self.frequncy_data = None
        self.__histogram: ttk.Frame = None
        self.__histogram_plot: ttk.Frame = None
        self.__empirical_function: ttk.Frame = None
        self.__kernal_density: ttk.Frame = None
        self.__kernal_density_plot: ttk.Frame = None

    def create_histogram(self, title, original_data, class_width):
        if self.__histogram:
            for widget in self.__histogram.winfo_children():
                widget.destroy()
        self.__histogram = self.create_graph(BarPlot, title, self.distribution_data,[0, 0],True, original_data, class_width)
        print(self.__histogram_plot.get_bandwidth())
        self.current_bandwidth.set(self.__histogram_plot.get_bandwidth())

    def update_bandwidth(self):
        new_bandwidth = float(self.current_bandwidth.get())
        self.update_kde_bandwidth(new_bandwidth)

    def update_kde_bandwidth(self, new_bandwidth):
        for widget in self.__histogram.winfo_children():
            widget.destroy()
        print(new_bandwidth)
        canvas = FigureCanvasTkAgg(self.__histogram_plot.figure, master=self.__histogram)
        self.__histogram_plot.set_bandwidth(new_bandwidth, canvas)

    def create_empirical_distribution_function(self, title):
        if self.__empirical_function:
            for widget in self.__empirical_function.winfo_children():
                widget.destroy()
        self.__empirical_function = self.create_graph(EmpiricalDistributionPlot, title, self.frequncy_data, [0, 1])

    def create_graph(self, plot_type, title, data, place, save_plot:bool = False, original_data = None, class_width = None):
        frame = ttk.Frame(self.container)
        frame.grid(row=place[0], column=place[1])

        if not save_plot:
            plot = plot_type(frame, title, data)
        else:
            plot = plot_type(frame, title, data, original_data, class_width)
            self.__histogram_plot = plot
        canvas = FigureCanvasTkAgg(plot.figure, master=frame)
        plot.create_plot(canvas)
        return frame

    def hide_window(self):
        self.controller_window.withdraw()

    def destroy_window(self):
        self.controller_window.destroy()
        self.controller_window.quit()

    def display_histogram(self, title, original_data, class_width):
        self.create_histogram(title, original_data, class_width)
        self.controller_window.deiconify()

    def display_empirical_function(self, title):
        self.create_empirical_distribution_function(title)
        self.controller_window.deiconify()

    def display_kernal_density(self, data, title, class_width):
        self.create_kde(data, title, class_width)
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
