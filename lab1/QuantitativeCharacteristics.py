import tkinter as tk

import numpy as np
from scipy import stats


class QuantitativeCharacteristics:
    def __init__(self, root):
        self.__data = None
        self.quantitative_characteristics_table = tk.Toplevel(root)
        self.quantitative_characteristics_table.withdraw()
        self.quantitative_characteristics_table.title("Quantitative Characteristics")
        self.quantitative_characteristics_table.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.frequency_table_dictionary = dict()

    def add_to_dictionary(self,column_name, column_data):
        self.frequency_table_dictionary.update({column_name:column_data})

    def add_characteristics(self):
        mean = round(np.mean(self.get_data()),4)
        median = round(np.median(self.get_data()),4)
        std_deviation = round(np.std(self.get_data(), ddof=1),4) # ddof=1 для виправлення зсуву вибіркової дисперсії
        skewness = round(stats.skew(self.get_data()),4)
        kurtosis = round(stats.kurtosis(self.get_data()),4)
        minimum = round(min(self.get_data()),4)
        maximum = round(max(self.get_data()),4)

        # Довірчий інтервал для середнього значення (95% довірчий інтервал)
        confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std_deviation / np.sqrt(len(self.get_data())))

        # Вивід результатів
        print(f"Середнє арифметичне: {mean}")
        print(f"Медіана: {median}")
        print(f"Середньоквадратичне відхилення: {std_deviation}")
        print(f"Коефіцієнт асиметрії: {skewness}")
        print(f"Коефіцієнт ексцесу: {kurtosis}")
        print(f"Мінімум: {minimum}")
        print(f"Максимум: {maximum}")
        print(f"95% довірчий інтервал для середнього значення: {confidence_interval}")
        # mean = round(np.mean(self.get_data()),4)
        # median = round(np.median(self.get_data()),4)
        # syd = round(np.std(self.get_data()),4)
        # print("Average: " + str(mean))
        # print("SYD of value: " + str(np.std(mean)))
        # print("Median: " + str(median))
        # print("SYD of value: " + str(np.std(median)))
        # print("SYD: " + str(syd))
        # print("SYD of value: " + str(np.std([1,2,2,1])))

        # freqency_map = self.calculate_frequency()
        # self.add_to_dictionary("№ option",list(range(1,len(freqency_map.items())+1)))
        # self.add_to_dictionary("Values",freqency_map.keys())
        # self.add_to_dictionary("Frequency",freqency_map.values())
        # relative_frequency = self.calculate_relative_frequency(freqency_map.values())
        # self.add_to_dictionary("Relative Frequency",relative_frequency)
        # self.add_to_dictionary("ECDF",self.calculate_empirical_distribution(relative_frequency,len(freqency_map.items())))

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def hide_window(self):
        self.controller_window.withdraw()