import tkinter as tk
from tkinter import ttk
import math as math
import numpy as np
from scipy import stats
from ProbabilityCoin import ProbabilityPaper
from Graph import Graph

# Коефіцієнти для формули
C0 = 2.515_517
C1 = 0.802_853
C2 = 0.010_328
D1 = 1.432_788
D2 = 0.189_265_9
D3 = 0.001_308


class QuantitativeCharacteristics:
    def __init__(self, root, graph):
        self.__data = None
        self.characteristic_fields_map = ["Mean", "Median", "Std", "Skewness", "Kurtosis", "Min", "Max"]
        self.quantitative_characteristics_table = tk.Toplevel(root)
        self.quantitative_characteristics_table.withdraw()
        self.quantitative_characteristics_table.title("Quantitative Characteristics")
        self.quantitative_characteristics_table.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.normal_split = tk.Toplevel(root)
        self.normal_split.withdraw()
        self.normal_split.title("Identify the normal distribution")
        self.normal_split.protocol("WM_DELETE_WINDOW", self.hide_normal_split)
        self.__graph_table: Graph = graph
        self.characteristic_table_dictionary = dict()
        self.label_ta: tk.Label = None
        self.label_te: tk.Label = None
        self.label_quantile: tk.Label = None
        self.label_identification: tk.Label = None
        self.__table: ttk.Treeview = None
        self.mean = None
        self.std_deviation = None
        self.a = None
        self.e = None
        self.sa = None
        self.se = None

    def add_to_dictionary(self, column_name, column_data):
        self.characteristic_table_dictionary.update({column_name: column_data})

    def display(self):
        self.add_characteristics()
        self.create_quantitative_table()
        self.quantitative_characteristics_table.deiconify()
        if self.label_identification is not None:
            self.clean_normal_split()
        self.calculate_normal_split()
        self.normal_split.deiconify()

    def create_probability_plot(self):
        __data_for_abnormal = [self.get_dictionary().get("№ option"),
                               self.get_dictionary().get("Values"),
                               normal_interval[0],
                               normal_interval[1]]
        if not (self.get_graph_table() is None or np.array_equiv(self.get_graph_table().get_abnormal_data(),
                                                                 __data_for_abnormal)):
            self.__graph_table.hide_window()
            self.__graph_table.set_abnormal_data(__data_for_abnormal)
        self.__graph_table.display_abnormal_values("Abnormal Values")

    def add_characteristics(self):
        estimation = self.calculate_estimation()
        self.add_to_dictionary("Characteristic", self.characteristic_fields_map)
        self.add_to_dictionary("Estimation", estimation.keys())
        self.add_to_dictionary("SEM", estimation.values())
        confidence_intervals = self.calculate_confidence_interval(estimation)
        self.add_to_dictionary("95% Confidence Interval", confidence_intervals)

    def calculate_confidence_interval(self, estimation: dict):
        confidence_interval = list(range(0, 7))
        median_conf_interval = self.calculate_median_confidence_interval(list(estimation.keys())[1])
        confidence_interval[1] = f"[{median_conf_interval[0]}; {median_conf_interval[1]}]"
        confidence_interval[5] = "───"
        confidence_interval[6] = "───"

        v = len(self.get_data()) - 1
        student_quantile = self.student_quantile(0.95, v)
        print("student_quantile: " + str(student_quantile))
        i = 0
        for key in estimation.keys():
            if (estimation.get(key) == "───"):
                i = i + 1
                continue
            upper_bound = round(key - student_quantile * estimation.get(key), 4)
            lower_bound = round(key + student_quantile * estimation.get(key), 4)
            confidence_interval[i] = f"[{upper_bound}; {lower_bound}]"

            i = i + 1

        return confidence_interval

    def calculate_median_confidence_interval(self, median):
        num_samples = 1000

        bootstrap_samples = [np.random.choice(self.get_data(), size=len(self.get_data()), replace=True) for _ in
                             range(num_samples)]

        bootstrap_medians = np.median(bootstrap_samples, axis=1)

        std_error_median = np.std(bootstrap_medians, ddof=1)
        v = len(self.get_data()) - 1
        student_quantile = self.student_quantile(1 - 0.05 / 2, v)
        lower_bound = round(median - student_quantile * std_error_median, 4)
        upper_bound = round(median + student_quantile * std_error_median, 4)

        return lower_bound, upper_bound

    def calculate_normal_interval(self):
        v = len(self.get_data()) - 1
        student_quantile = self.student_quantile(1 - 0.05 / 2, v)
        lower_bound = round(self.mean - student_quantile * self.std_deviation, 4)
        upper_bound = round(self.mean + student_quantile * self.std_deviation, 4)
        return lower_bound, upper_bound

    def calculate_estimation(self):
        estimation_map = dict()
        self.mean = round(np.mean(self.get_data()), 4)
        median = round(np.median(self.get_data()), 4)
        self.std_deviation = round(np.std(self.get_data(), ddof=1), 4)
        self.a = round(stats.skew(self.get_data()), 4)
        self.e = round(stats.kurtosis(self.get_data()), 4)
        minimum = round(min(self.get_data()), 4)
        maximum = round(max(self.get_data()), 4)

        n_len = len(self.get_data())
        mean_std = round(self.std_deviation / np.sqrt(n_len), 4)
        std_std_deviation = round(self.std_deviation / np.sqrt(2 * n_len), 4)
        self.sa = round(np.sqrt(6 * n_len * (n_len - 1) / ((n_len - 2) * (n_len + 1) * (n_len + 3))), 4)
        self.se = round(
            np.sqrt(24 * n_len * (n_len - 1) ** 2 / ((n_len - 3) * (n_len - 2) * (n_len + 3) * (n_len + 5))), 4)

        estimation_map[self.mean] = mean_std
        estimation_map[median] = "───"
        estimation_map[self.std_deviation] = std_std_deviation
        estimation_map[self.a] = self.sa
        estimation_map[self.e] = self.se
        estimation_map[minimum] = "───"
        estimation_map[maximum] = "───"
        return estimation_map

    def calculate_normal_split(self):
        ta = self.a / self.sa
        te = self.e / self.se
        student_quantile = self.student_quantile(1 - 0.05 / 2, len(self.get_data()) - 1)
        self.label_ta = tk.Label(self.normal_split, text=f"tA = {ta}")
        self.label_te = tk.Label(self.normal_split, text=f"tE = {te}")
        self.label_quantile = tk.Label(self.normal_split, text=f"Quantile = {student_quantile}")

        if ta <= student_quantile and te <= student_quantile:
            identification_result = "identified"
        else:
            identification_result = "not identified"

        self.label_identification = tk.Label(self.normal_split, text=f"Identification: {identification_result}")

        self.label_ta.pack()
        self.label_te.pack()
        self.label_quantile.pack()
        self.label_identification.pack()

    def clean_normal_split(self):
        self.label_ta.pack_forget()
        self.label_te.pack_forget()
        self.label_quantile.pack_forget()
        self.label_identification.pack_forget()
    def create_quantitative_table(self):
        self.set_table(ttk.Treeview(self.get_root(),
                                    columns=list(self.characteristic_table_dictionary.keys()),
                                    show='headings'))

        for column in self.characteristic_table_dictionary.keys():
            try:
                self.get_table().heading(column, text=column)
                self.get_table().column(column, width=100)
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
        self.quantitative_characteristics_table.withdraw()

    def hide_normal_split(self):
        self.normal_split.withdraw()

    def calculate_quantile(self, p):
        if p > 0.5:
            t = math.sqrt(-2 * math.log(1 - p))
            quantile = (t - ((C0 + C1 * t + C2 * t ** 2) / (1 + D1 * t + D2 * t ** 2 + D3 * t ** 3)))
        else:
            t = math.sqrt(-2 * math.log(1 - p))
            quantile = -(t - ((C0 + C1 * t + C2 * t ** 2) / (1 + D1 * t + D2 * t ** 2 + D3 * t ** 3)))

        return quantile

    def student_quantile(self, p, v):
        up = self.calculate_quantile(p)

        tpv = up + (1 / v) * (1 / 4) * (up ** 3 + up) + (1 / v ** 2) * (1 / 96) * (
                5 * up ** 5 + 16 * up ** 3 + 3 * up) + (1 / v ** 3) * (1 / 384) * (
                      3 * up ** 7 + 19 * up ** 5 + 17 * up ** 3 - 15 * up) + (1 / v ** 4) * (1 / 92_160) * (
                      79 * up ** 9 + 779 * up ** 7 + 1_482 * up ** 5 - 1_920 * up ** 3 - 945 * up)
        return tpv

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __hash__(self) -> int:
        return super().__hash__()
