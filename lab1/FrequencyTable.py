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
        super().__init__(data)
        self.frequency_table_dictionary = dict()
        self.get_root().title("Frequency Table")
        self.__table: ttk.Treeview = None

    def add_to_dictionary(self,column_name,data):
        self.frequency_table_dictionary.update({column_name:data})

    def display(self):
        self.add_frequency()
        self.create_table()
        self.get_root().deiconify()

    def add_frequency(self):
        freqency_map = self.count_frequency()
        self.add_number_column(len(freqency_map.items()))
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
        print(self.get_data())
        for i in range(len(self.get_data())):
            if self.get_data()[i] in map.keys():
                map[self.get_data()[i]] +=1
            else:
                    map[self.get_data()[i]] = 1
        return OrderedDict(sorted(map.items()))

    def create_table(self):


        self.set_table(ttk.Treeview(self.get_root(), columns=list(self.frequency_table_dictionary.keys()), show='headings'))

        for column in self.frequency_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=100)
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

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()