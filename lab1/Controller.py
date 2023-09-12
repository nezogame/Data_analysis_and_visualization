import tkinter as tk
import numpy as np
from tkinter import ttk
from FrequencyTable import FrequencyTable
from FrequencyDistributionTable import FrequencyDistributionTable
from Histogram import BarPlot

def create_table_tab(data):
        create_frequency_table(data)
        create_frequency_distribution_table(data)

def create_frequency_table(data):
        __table = FrequencyTable(data)
        if not (__table is None or np.array_equiv(__table.get_data(), data)):
                __table.set_data(data)
        __table.display()

def create_frequency_distribution_table(data):
        __dist_table = FrequencyDistributionTable(data)
        if not (__dist_table is None or np.array_equiv(__dist_table.get_data(), data)):
                __dist_table.set_data(data)
                __dist_table.set_number_of_classes(__dist_table.find_number_of_classes(len(data)))
        __dist_table.display()
        create_histogram([__dist_table.frequency_distribution_table_dictionary.get("Class Width"),
                          __dist_table.frequency_distribution_table_dictionary.get("Relative Frequency")])

def create_histogram(data):

        root = tk.Tk()
        root.title("Plot Controller")

        container = ttk.Frame(root)
        container.pack(fill=tk.BOTH, expand=True)

        frame = ttk.Frame(container)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #разобраться что такое frame and how to display controller window

        plot = BarPlot(frame, "Histogram", data)
        plot.create_plot(frame)
        root.deiconify()

