import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Histogram import BarPlot

class Graph:
    def __init__(self, data):
        self.controller_window = tk.Tk()
        self.controller_window.title("Plot Controller")
        self.controller_window.protocol("WM_DELETE_WINDOW", self.hide_window())
        self.container = ttk.Frame(self.controller_window)
        self.container.pack(fill=tk.BOTH, expand=True)
        self.data = data

    def create_histogram(self, plot_type, title):
        frame = ttk.Frame(self.container)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        plot = plot_type(frame, title, self.data)
        canvas = FigureCanvasTkAgg(plot.figure, master=frame)
        plot.create_plot(canvas)

    def hide_window(self):
        self.controller_window.withdraw()

    def destroy_window(self):
        self.controller_window.destroy()

    def display(self, plot_type, title):
        self.create_histogram(plot_type, title)
        self.controller_window.deiconify()

    def get_data(self):
        return self.data

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()
