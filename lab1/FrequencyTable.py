import tkinter as tk
from tkinter import ttk
from collections import OrderedDict
from Window import BaseWindow

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class FrequencyTable(BaseWindow,    metaclass=Singleton):
    def __init__(self,data):
        self.frequency_table_dictionary = dict()
        self.__data = data
        self.__root = tk.Tk()

    def add_to_dictionary(self,column_name,data):
        self.frequency_table_dictionary.update({column_name:data})

    def display(self):
        self.add_frequency()
        self.create_table()
        self.__root.mainloop()

    def add_frequency(self):
        freqency_map = self.count_frequency()
        self.add_number_column(len(freqency_map.keys()))
        self.add_value_colum(freqency_map.keys())
        self.add_frequency_column(freqency_map.values())

    def add_number_column(self,numbers):
        sequence = list(range(1,numbers+1))
        self.frequency_table_dictionary.update({"№ option":sequence})

    def add_value_colum(self,data):
        self.frequency_table_dictionary.update({"Values":data})

    def add_frequency_column(self,frequency_data):
        self.frequency_table_dictionary.update({"Frequency": frequency_data})

    def add_relative_frequency_column(self,relative_frequency_data):
        self.frequency_table_dictionary.update({"Relative Frequency": relative_frequency_data})

    def add_relative_frequency_column(self,empirical_distribution_data ):
        self.frequency_table_dictionary.update({"EVDF": empirical_distribution_data })

    def count_frequency(self):
        map = dict()
        print(self.__data)
        for i in range(len(self.__data)):
            if self.__data[i] in map.keys():
                map[self.__data[i]] +=1
            else:
                    map[self.__data[i]] = 1
        return map

    def create_table(self):
        # Create a Treeview widget to display the table
        table = ttk.Treeview(self.__root, columns=list(self.frequency_table_dictionary.keys()), show='headings')
        # Add column headings to the table
        for column in self.frequency_table_dictionary.keys():
            table.heading(column, text=column)
            table.column(column, width=100)  # Adjust the column width as needed

        for row_values in zip(*self.frequency_table_dictionary.values()):
            table.insert("", "end", values=row_values)

        # Pack the table and start the tkinter main loop
        table.pack()