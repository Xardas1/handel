import numpy as np
import matplotlib.pyplot as plt


def calculate_difference():
    x = np.linspace(-10, 10, 400)
    y = 10*x + 10
    above_x = y > 0 
    below_x = y < 0
    distance_from_x_axis = np.abs(y)
    return y[below_x]
