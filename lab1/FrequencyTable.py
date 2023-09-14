import tkinter as tk
import numpy as np
from tkinter import ttk
from collections import OrderedDict
from Window import BaseWindow
from Window import Singleton
from Graph import Graph

class FrequencyTable(BaseWindow,    metaclass=Singleton):
    def __init__(self, data, graph):
        super().__init__(data)
        self.frequency_table_dictionary = dict()
        self.get_root().title("Frequency Table")
        self.__table: ttk.Treeview = None
        self.__empirical_distribution_table : Graph = graph

    def add_to_dictionary(self,column_name, column_data):
        self.frequency_table_dictionary.update({column_name:column_data})

    def display(self):
        self.add_frequency()
        self.create_table()
        self.get_root().deiconify()
        self.create_step_EDF()

    def create_step_EDF(self):
        __ECDF_data = [self.get_dictionary().get("Values"),
                       self.get_dictionary().get("ECDF")]
        if not (self.get_empirical_distribution_table() is None
        or np.array_equiv(self.get_empirical_distribution_table().get_distribution_data(), __ECDF_data)):
            self.__empirical_distribution_table.hide_window()
        self.__empirical_distribution_table.set_frequncy_data(__ECDF_data)
        self.__empirical_distribution_table.display_empirical_function("Empirical Distribution Function")
    def add_frequency(self):
        freqency_map = self.calculate_frequency()
        self.add_to_dictionary("№ option",list(range(1,len(freqency_map.items())+1)))
        self.add_to_dictionary("Values",freqency_map.keys())
        self.add_to_dictionary("Frequency",freqency_map.values())
        relative_frequency = self.calculate_relative_frequency(freqency_map.values())
        self.add_to_dictionary("Relative Frequency",relative_frequency)
        self.add_to_dictionary("ECDF",self.calculate_empirical_distribution(relative_frequency,len(freqency_map.items())))

    def calculate_frequency(self):
        map = dict()
        for i in range(len(self.get_data())):
            if self.get_data()[i] in map.keys():
                map[self.get_data()[i]] +=1
            else:
                    map[self.get_data()[i]] = 1
        #return map
        return OrderedDict(sorted(map.items()))

    def calculate_relative_frequency(self,data):
        return [i/sum(data) for i in data]

    def calculate_empirical_distribution(self, data,n):
        return [sum(data[:i + 1]) for i in range(n)]

    def create_table(self):
        self.set_table(ttk.Treeview(self.get_root(), columns=list(self.frequency_table_dictionary.keys()), show='headings'))

        for column in self.frequency_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=150)
            except Exception as e:
                self.set_table(None)
                print(e)

        for row_values in zip(*self.frequency_table_dictionary.values()):
            self.get_table().insert("", "end", values=row_values)

        self.get_table().grid(row=0, column=0)

        scrollbar = ttk.Scrollbar(self.get_root(), orient=tk.VERTICAL, command=self.get_table().yview)
        self.get_table().configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def set_data(self, data):
        self.get_table().delete(*self.__table.get_children())
        super().set_data(data)

    def get_table(self):
        return self.__table

    def set_table(self,treeview):
        self.__table = treeview

    def get_dictionary(self):
        return self.frequency_table_dictionary

    def get_empirical_distribution_table(self):
        return self.__empirical_distribution_table

    def set_empirical_distribution_table(self, graph_table):
        self.__empirical_distribution_table = graph_table

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()