import tkinter as tk
import numpy as np
from tkinter import ttk
from FrequencyTable import FrequencyTable
from FrequencyDistributionTable import FrequencyDistributionTable
from Graph import Graph
from QuantitativeCharacteristics import QuantitativeCharacteristics

class Controller:
    def __init__(self, root):
        self.__graph_table = Graph(root)
        self.__characteristic = QuantitativeCharacteristics(root)
        self.__quant_table = QuantitativeCharacteristics(root)

    def create_table_tab(self, data):
        self.create_frequency_table(data)
        self.create_frequency_distribution_table(data)
        self.create_quantitative_characteristics(data)
        self.create_quantitative_table(data)

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

    def create_quantitative_characteristics(self,data):
        self.__characteristic.set_data(data)
        self.__characteristic.add_characteristics()

    def create_quantitative_table(self, data):
        if not (np.array_equiv(self.__quant_table.get_data(), data)):
            self.__quant_table.set_data(data)
        self.__quant_table.display()