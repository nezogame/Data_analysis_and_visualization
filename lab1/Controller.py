import tkinter as tk
import numpy as np
from FrequencyTable import FrequencyTable
from FrequencyDistributionTable import FrequencyDistributionTable

def f_table(data):
        __table = FrequencyTable(data)
        if not (__table is None or np.array_equiv(__table.get_data(), data)):
                __table.set_data(data)
        __table.display()

def f_distribution_table(data):
        __dist_table = FrequencyDistributionTable(data)
        if not (__dist_table is None or np.array_equiv(__dist_table.get_data(), data)):
                __dist_table.set_data(data)
                __dist_table.set_number_of_classes(__dist_table.find_number_of_classes(len(data)))
        __dist_table.display()