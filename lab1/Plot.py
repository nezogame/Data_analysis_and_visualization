import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BasePlot:
    def __init__(self, frame, title, data):
        self.frame = frame
        self.title = title
        self.data = data
        self.figure, self.ax = plt.subplots()
        self.plot()

    def plot(self):
        pass  # Implement this method in derived classes


