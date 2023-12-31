import tkinter as tk
import numpy as np
from tkinter import ttk
from FrequencyTable import FrequencyTable
from FrequencyDistributionTable import FrequencyDistributionTable
from Graph import Graph


class Controller:
    def __init__(self, root):
        self.__root = root
        self.__graph_table = Graph(root)

    def create_table_tab(self, data):
        self.create_frequency_table(data, self)
        self.create_frequency_distribution_table(data)
        if not self.__graph_table.get_abnormal_data() == None:
            self.__graph_table.hide_abnormal_values()

    def create_frequency_table(self, data, controller):
        __table = FrequencyTable(data, self.__graph_table, self.__root, controller)
        if not (__table is None or np.array_equiv(__table.get_data(), data)):
            __table.set_data(data)
        __table.display()

    def create_frequency_distribution_table(self, data):
        __dist_table = FrequencyDistributionTable(data, self.__graph_table)
        if not (__dist_table is None or np.array_equiv(__dist_table.get_data(), data)):
            __dist_table.set_data(data)
            __dist_table.set_number_of_classes(__dist_table.find_number_of_classes(len(data)))
        __dist_table.display()
