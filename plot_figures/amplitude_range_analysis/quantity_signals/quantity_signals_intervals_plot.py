import numpy as np
from matplotlib import pyplot as plt

from amplitude_range_analysis.error_amplitude_range import number_intervals, quantity_signals_amplitude_range, \
    define_intervals, define_midpoints_intervals
from amplitude_range_analysis.quantity_signals.data_plots import return_data_plots
from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_separately_crossvalidation

# Defining some constants
number_iterations = 10
occupancies = [10, 30, 50, 80]
initial_amplitude_min = 10
initial_amplitude_max = 20

# Defining plot aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Checking how many intervals there will be
number_intervals = number_intervals(initial_amplitude_min, initial_amplitude_max, 1023)

# Declaring some structures
quantity_signals = np.zeros([number_iterations, number_intervals]).astype(int)
mean_quantity_signals = np.zeros([len(occupancies), number_intervals]).astype(int)
std_quantity_signals = np.zeros([len(occupancies), number_intervals]).astype(int)
# iterations -> rows, intervals -> columns

i = 0
for occupancy in occupancies:
    print('------------------------------')

    for it in range(number_iterations):
        print("Occupancy: " + str(occupancy) + ",\titeration: " + str(it + 1))

        # Importing the data
        amplitude_true = import_amplitude_separately_crossvalidation(occupancy, it + 1, 'verdadeira')

        # Calculating the quantity of signals in each interval
        quantity_signals[it] = quantity_signals_amplitude_range(amplitude_true, initial_amplitude_min, initial_amplitude_max)

    mean_quantity_signals[i] = np.mean(quantity_signals, axis=0)
    std_quantity_signals[i] = np.std(quantity_signals, axis=0)
    i += 1

# Defining the intervals
intervals = define_intervals(initial_amplitude_min, initial_amplitude_max)
midpoint_intervals = define_midpoints_intervals(intervals).astype(int)

# Plotting the graphs
plt.rcParams['figure.autolayout'] = True
# First way
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.figure(figsize=(10, 6))
_, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(midpoint_intervals, mean_quantity_signals[0], yerr=std_quantity_signals[0], fmt='.-',
             capsize=2, color='C1', alpha=alpha_graphs, markersize=10, label='Occupancy 10%')
plt.errorbar(midpoint_intervals, mean_quantity_signals[1], yerr=std_quantity_signals[1], fmt='.-',
             capsize=2, color='C2', alpha=alpha_graphs, markersize=10, label='Occupancy 30%')
plt.errorbar(midpoint_intervals, mean_quantity_signals[2], yerr=std_quantity_signals[2], fmt='.-',
             capsize=2, color='C3', alpha=alpha_graphs, markersize=10, label='Occupancy 50%')
plt.errorbar(midpoint_intervals, mean_quantity_signals[3], yerr=std_quantity_signals[3], fmt='.-',
             capsize=2, color='C4', alpha=alpha_graphs, markersize=10, label='Occupancy 80%')
plt.legend(loc='upper right', fontsize=17)
plt.title(f'Occupancy: {occupancy}%', fontsize=17)
plt.xlabel('Reference amplitude (ADC counts)', fontsize=17)
plt.ylabel('Number of signals', fontsize=17)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(midpoint_intervals, np.mean(quantity_signals, axis=0), 0, ax, ax1, 'C3', alpha_graphs,
                 ' ', ' ', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(midpoint_intervals, np.mean(quantity_signals, axis=0), 0, ax, ax1, 'C3', alpha_graphs,
                 ' ', ' ', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

plt.show()
