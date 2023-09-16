import tkinter as tk
import numpy as np
from tkinter import ttk
from FrequencyTable import FrequencyTable
from FrequencyDistributionTable import FrequencyDistributionTable
from Graph import Graph

class Controller:
    def __init__(self, root):
        self.__graph_table = Graph(root)
        self.class_width = None

    def create_table_tab(self, data):
        self.create_frequency_table(data)
        self.create_frequency_distribution_table(data)
        self.create_kernel_density_estimation_table(data)

    def create_frequency_table(self, data):
        __table = FrequencyTable(data, self.__graph_table)
        if not (__table is None or np.array_equiv(__table.get_data(), data)):
            __table.set_data(data)
        __table.display()

    def create_frequency_distribution_table(self, data):
        __dist_table = FrequencyDistributionTable(data, self.__graph_table)
        if not (__dist_table is None or np.array_equiv(__dist_table.get_data(), data)):
            __dist_table.set_data(data)
            __dist_table.set_number_of_classes(__dist_table.find_number_of_classes(len(data)))
        __dist_table.display()
        self.class_width = __dist_table.get_class_width()

    def create_kernel_density_estimation_table(self, data):
        self.__graph_table.display_kernal_density(data, "KDE", self.class_width)