import tkinter as tk
from tkinter import ttk

import numpy as np
from scipy import stats


class QuantitativeCharacteristics:
    def __init__(self, root):
        self.__data = None
        self.characteristic_fields_map = ["Mean", "Median", "Std", "Skewness", "Kurtosis", "Min", "Max"]
        self.quantitative_characteristics_table = tk.Toplevel(root)
        self.quantitative_characteristics_table.withdraw()
        self.quantitative_characteristics_table.title("Quantitative Characteristics")
        self.quantitative_characteristics_table.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.characteristic_table_dictionary = dict()
        self.__table: ttk.Treeview = None

    def add_to_dictionary(self, column_name, column_data):
        self.characteristic_table_dictionary.update({column_name: column_data})

    def display(self):
        self.add_characteristics()
        self.create_quantitative_table()
        self.quantitative_characteristics_table.deiconify()

    def add_characteristics(self):
        estimation = self.calculate_estimation()
        self.add_to_dictionary("Characteristic", self.characteristic_fields_map)
        self.add_to_dictionary("Estimation", estimation.keys())
        self.add_to_dictionary("SEM", estimation.values())
        self.add_to_dictionary("95% Confidence Interval", estimation.values())

        mean = round(np.mean(self.get_data()), 4)
        median = round(np.median(self.get_data()), 4)
        std_deviation = round(np.std(self.get_data(), ddof=1), 4)
        skewness = round(stats.skew(self.get_data()), 4)
        kurtosis = round(stats.kurtosis(self.get_data()), 4)
        minimum = round(min(self.get_data()), 4)
        maximum = round(max(self.get_data()), 4)

        # Довірчий інтервал для середнього значення (95% довірчий інтервал)
        confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std_deviation / np.sqrt(len(self.get_data())))
        sample_size = len(self.get_data())

        # Calculate the Standard Error of the Mean (SEM)
        sem = std_deviation / np.sqrt(sample_size)

        # Вивід результатів
        print(f"Середнє арифметичне: {mean}")
        print(f"Медіана: {median}")
        print(f"Середньоквадратичне відхилення: {std_deviation}")
        print(f"Коефіцієнт асиметрії: {skewness}")
        print(f"Коефіцієнт ексцесу: {kurtosis}")
        print(f"Мінімум: {minimum}")
        print(f"Максимум: {maximum}")
        print(f"95% довірчий інтервал для середнього значення: {confidence_interval}")
        print(f"Standard Error of the Mean (SEM): {sem}")


    def calculate_confidence_interval(self):
        confidence_interval = tuple()

    def calculate_confidence_interval(data):
        # Sample statistics
        sample_mean = sum(data) / len(data)
        sample_std = math.sqrt(sum((x - sample_mean) ** 2 for x in data) / (len(data) - 1))

        # Desired confidence level (95%)
        confidence_level = 0.95

        # Calculate the critical value (Z) for the confidence level
        from scipy.stats import norm
        Z = norm.ppf((1 + confidence_level) / 2)

        # Calculate the margin of error
        margin_of_error = Z * (sample_std / math.sqrt(len(data)))

        # Calculate the confidence interval
        lower_bound = sample_mean - margin_of_error
        upper_bound = sample_mean + margin_of_error

        return lower_bound, upper_bound

    def calculate_estimation(self):
        estimation_map = dict()
        mean = round(np.mean(self.get_data()), 4)
        median = round(np.median(self.get_data()), 4)
        std_deviation = round(np.std(self.get_data(), ddof=1), 4)
        skewness = round(stats.skew(self.get_data()), 4)
        kurtosis = round(stats.kurtosis(self.get_data()), 4)
        minimum = round(min(self.get_data()), 4)
        maximum = round(max(self.get_data()), 4)

        n_len = len(self.get_data())
        mean_std = round(std_deviation / np.sqrt(n_len), 4)
        std_std_deviation = round(std_deviation / np.sqrt(2*n_len), 4)
        std_skewness = round(np.sqrt(6*n_len*(n_len-1)/((n_len-2)*(n_len+1)*(n_len+3))), 4)
        std_kurtosis = round(np.sqrt(24*n_len*(n_len-1)**2/((n_len-3)*(n_len-2)*(n_len+3)*(n_len+5))), 4)

        estimation_map[mean] = mean_std
        estimation_map[median] = "───"
        estimation_map[std_deviation] = std_std_deviation
        estimation_map[skewness] = std_skewness
        estimation_map[kurtosis] = std_kurtosis
        estimation_map[minimum] = "───"
        estimation_map[maximum] = "───"
        return estimation_map

    def create_quantitative_table(self):
        self.set_table(ttk.Treeview(self.get_root(),
                                    columns=list(self.characteristic_table_dictionary.keys()),
                                    show='headings'))

        for column in self.characteristic_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=80)
            except Exception as e:
                self.set_table(None)
                print(e)

        for row_values in zip(*self.characteristic_table_dictionary.values()):
            self.get_table().insert("", "end", values=row_values)

        self.get_table().grid(row=1, column=0, columnspan=4)

        scrollbar = ttk.Scrollbar(self.get_root(), orient=tk.VERTICAL, command=self.get_table().yview)
        self.get_table().configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=5, sticky='ns')

    def get_root(self):
        return self.quantitative_characteristics_table
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_table(self):
        return self.__table

    def set_table(self, treeview):
        self.__table = treeview

    def hide_window(self):
        self.controller_window.withdraw()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()
