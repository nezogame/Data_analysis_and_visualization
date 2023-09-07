import tkinter as tk
import numpy as np
from FrequencyTable import FrequencyTable

def f_table(data):
        __table = FrequencyTable(data)
        if not (__table is None or np.array_equiv(__table.get_data(), data)):
                __table.set_data(data)
        __table.display()