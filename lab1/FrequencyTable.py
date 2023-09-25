import tkinter as tk
from tkinter import ttk

import numpy as np
from Graph import Graph
from QuantitativeCharacteristics import QuantitativeCharacteristics
from Window import BaseWindow
from Window import Singleton


class FrequencyTable(BaseWindow, metaclass=Singleton):
    def __init__(self, data, graph, root, controller):
        super().__init__(data)
        self.controller: Controller = controller
        self.frequency_table_dictionary = dict()
        self.btn_find_abnormal = (tk.Button(self.get_root(), text="Find Abnormal Values",
                                            command=lambda: self.create_abnormal_plot()))
        self.btn_find_abnormal.grid(row=0, column=2)
        self.btn_find_abnormal = (tk.Button(self.get_root(), text="DELETE Abnormal Values",
                                            command=lambda: self.delete_abnormal_value()))
        self.btn_find_abnormal.grid(row=0, column=3)
        self.get_root().title("Frequency Table")
        self.__table: ttk.Treeview = None
        self.__quant_table = QuantitativeCharacteristics(root)
        self.__graph_table: Graph = graph

    def add_to_dictionary(self, column_name, column_data):
        self.frequency_table_dictionary.update({column_name: column_data})

    def display(self):
        self.add_frequency()
        self.create_table()
        self.get_root().deiconify()
        self.create_step_EDF()
        self.create_quantitative_table()

    def create_step_EDF(self):
        __ECDF_data = [self.get_dictionary().get("Values"),
                       self.get_dictionary().get("ECDF")]
        if not (self.get_graph_table() is None
                or np.array_equiv(self.get_graph_table().get_distribution_data(), __ECDF_data)):
            self.__graph_table.hide_window()
        self.__graph_table.set_frequncy_data(__ECDF_data)
        self.__graph_table.display_empirical_function("Empirical Distribution Function")

    def create_abnormal_plot(self):
        normal_interval = self.__quant_table.calculate_normal_interval()
        __data_for_abnormal = [self.get_dictionary().get("№ option"),
                               self.get_dictionary().get("Values"),
                               normal_interval[0],
                               normal_interval[1]]
        if not (self.get_graph_table() is None or np.array_equiv(self.get_graph_table().get_abnormal_data(),
                                                                 __data_for_abnormal)):
            self.__graph_table.hide_window()
            self.__graph_table.set_abnormal_data(__data_for_abnormal)
        self.__graph_table.display_abnormal_values("Abnormal Values")

    def delete_abnormal_value(self):
        borders = self.__graph_table.find_normal_border()
        normal_values_indexes = [x for x in range(borders[0], borders[1])]
        self.set_data(self.get_data()[normal_values_indexes])
        self.controller.create_table_tab(self.get_data())

    def create_quantitative_table(self):
        self.__quant_table.set_data(self.get_data())
        self.__quant_table.display()

    def add_frequency(self):
        freqency_map = self.calculate_frequency()
        self.add_to_dictionary("№ option", list(range(1, len(freqency_map.items()) + 1)))
        self.add_to_dictionary("Values", freqency_map.keys())
        self.add_to_dictionary("Frequency", freqency_map.values())
        relative_frequency = self.calculate_relative_frequency(freqency_map.values())
        self.add_to_dictionary("Relative Frequency", relative_frequency)
        self.add_to_dictionary("ECDF",
                               self.calculate_empirical_distribution(relative_frequency, len(freqency_map.items())))

    def calculate_frequency(self):
        map = dict()
        for i in range(len(self.get_data())):
            if self.get_data()[i] in map.keys():
                map[self.get_data()[i]] += 1
            else:
                map[self.get_data()[i]] = 1
        return map

    def calculate_relative_frequency(self, data):
        return [i / sum(data) for i in data]

    def calculate_empirical_distribution(self, data, n):
        return [sum(data[:i + 1]) for i in range(n)]

    def create_table(self):
        self.set_table(
            ttk.Treeview(self.get_root(), columns=list(self.frequency_table_dictionary.keys()), show='headings'))

        for column in self.frequency_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=150)
            except Exception as e:
                self.set_table(None)
                print(e)

        for row_values in zip(*self.frequency_table_dictionary.values()):
            self.get_table().insert("", "end", values=row_values)

        self.get_table().grid(row=1, column=0, columnspan=5)

        scrollbar = ttk.Scrollbar(self.get_root(), orient=tk.VERTICAL, command=self.get_table().yview)
        self.get_table().configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=6, sticky='ns')

    def set_data(self, data):
        self.get_table().delete(*self.__table.get_children())
        super().set_data(data)

    def get_table(self):
        return self.__table

    def set_table(self, treeview):
        self.__table = treeview

    def get_dictionary(self):
        return self.frequency_table_dictionary

    def get_graph_table(self):
        return self.__graph_table

    def set_graph_table(self, graph_table):
        self.__graph_table = graph_table

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()