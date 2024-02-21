# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:46:54 2023

@author: wilks
"""

import numpy as np
from scipy.signal import convolve
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")

# Generate some example data with 2400 points
original_data = np.random.rand(2400)

# Define the size of the moving average window
window_size = 80  # Adjust this value to control the level of smoothing

# Create the moving average kernel
kernel = np.ones(window_size) / window_size

# Apply convolution to smooth the data
smoothed_data = convolve(original_data, kernel, mode='same')

# Take every 80th point to reduce the data to 30 points
reduced_data = smoothed_data[::80]

# Now, 'reduced_data' contains the smoothed data with 30 points
plt.plot(range(2400), reduced_data)    
plt.show()