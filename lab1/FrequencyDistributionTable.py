import tkinter as tk
import numpy as np
from tkinter import ttk
from Window import BaseWindow
from Window import Singleton

class FrequencyDistributionTable(BaseWindow, metaclass=Singleton):

    def __init__(self, data):
        super().__init__(data)
        self.frequency_distribution_table_dictionary = dict()
        self.get_root().title("Frequency Distribution Table")
        self.__number_of_classes = self.find_number_of_classes(len(data))
        self.__table: ttk.Treeview = None

    def get_number_of_classes(self):
        return self.__number_of_classes

    def set_number_of_classes(self,number_of_classes):
        self.__number_of_classes=number_of_classes;

    def set_data(self, data):
        self.get_table().delete(*self.__table.get_children())
        super().set_data(data)

    def get_table(self):
        return self.__table

    def set_table(self, treeview):
        self.__table = treeview

    def add_to_dictionary(self, column_name, column_data):
        self.frequency_distribution_table_dictionary.update({column_name: column_data})

    def find_number_of_classes(self,length):
        num_classes = int(length ** (1 / 2)) if length < 100 else int(length ** (1 / 3))
        return num_classes-1 if length%2==0 else num_classes

    def display(self):
        self.add_frequency()
        self.create_distribution_table()
        self.get_root().deiconify()

    def add_frequency(self):
        freqency_map = self.calculate_frequency_distribution()
        self.add_to_dictionary("№ class", list(range(1,self.get_number_of_classes()+1)))
        self.add_to_dictionary("class Width", freqency_map.keys())
        self.add_to_dictionary("Frequency",freqency_map.values())
        relative_frequency = self.calculate_relative_frequency(freqency_map.values())
        self.add_to_dictionary("Relative Frequency",relative_frequency)
        self.add_to_dictionary("ECDF",self.calculate_empirical_distribution(relative_frequency,len(freqency_map.items())))


    def calculate_frequency_distribution(self):
        # Calculate the range of the data
        data_range = max(self.get_data()) - min(self.get_data())

        # Calculate the class width
        class_width = data_range / self.get_number_of_classes()
        frquency_map = dict()
        for i in range(self.get_number_of_classes()):
            lower_bound = min(self.get_data()) + i * class_width
            upper_bound = lower_bound + class_width
            frequency = len([x for x in self.get_data() if lower_bound <= x <= upper_bound])
            frquency_map[(lower_bound, upper_bound)]=frequency
        return frquency_map

    def calculate_relative_frequency(self,data):
        return [i/sum(data) for i in data]

    def calculate_empirical_distribution(self, data,n):
        return [sum(data[:i + 1]) for i in range(n)]

    def create_distribution_table(self):
        self.set_table(ttk.Treeview(self.get_root(),
                                    columns=list(self.frequency_distribution_table_dictionary.keys()),
                                    show='headings'))

        for column in self.frequency_distribution_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=150)
            except Exception as e:
                self.set_table(None)
                print(e)

        for row_values in zip(*self.frequency_distribution_table_dictionary.values()):
            self.get_table().insert("", "end", values=row_values)

        self.get_table().grid(row=0, column=0)

        scrollbar = ttk.Scrollbar(self.get_root(), orient=tk.VERTICAL, command=self.get_table().yview)
        self.get_table().configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()
