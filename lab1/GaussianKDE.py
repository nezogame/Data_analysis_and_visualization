import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

class GaussianKDE:

    def __init__(self, data, bandwidth):
        self.data = data
        self.bandwidth = bandwidth

    def _gaussian_kernel(self, x):
        return np.exp(-0.5 * (x ** 2)) / np.sqrt(2 * np.pi)

    def estimate_density(self, x_values):
        density_values = []
        for x in x_values:
            kernel_values = [self._gaussian_kernel((x - xi) / self.bandwidth) for xi in self.data]
            density = np.sum(kernel_values) / (self.bandwidth * len(self.data))
            density_values.append(density)
        return density_values
