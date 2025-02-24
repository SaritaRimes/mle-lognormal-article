from matplotlib import pyplot as plt

from amplitude_range_analysis.mean_error.data_plots import return_data_plots
from amplitude_range_analysis.error_amplitude_range import mean_std_error_amplitude_range
from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_crossvalidation


# Defining some constants
iteration = 1
occupancy = 80

# Defining plot aspects
ap = {'color_gauss': 'black', 'color_of': 'grey', 'color_cof': 'black', 'color_logn': 'grey',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '^--', 'fmt_logn': '^--'}  # plots aspects
color_grid = 'lightgrey'

# Importing the data
[amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
    = import_amplitude_crossvalidation(occupancy, iteration + 1)

# Calculating the error_mean and standard deviation for de amplitudes range
initial_amplitude = 20
[mean_error_gaussian, _] = mean_std_error_amplitude_range(amplitude_true, amplitude_gaussian, initial_amplitude)
[mean_error_of, _] = mean_std_error_amplitude_range(amplitude_true, amplitude_of, initial_amplitude)
[mean_error_cof, _] = mean_std_error_amplitude_range(amplitude_true, amplitude_cof, initial_amplitude)
[mean_error_lognormal, _] = mean_std_error_amplitude_range(amplitude_true, amplitude_lognormal, initial_amplitude)

# Defining the intervals
intervals = []
max_interval = initial_amplitude
while True:
    if max_interval < 1023:
        intervals.append(max_interval)
    else:
        intervals.append(max(amplitude_true))
        break

    max_interval = 2 * max_interval

# Plotting the graphs
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(intervals, mean_error_gaussian, yerr=0, fmt=ap['fmt_gauss'],
             color=ap['color_gauss'], markersize=15, label='MLE Gaussian')
plt.errorbar(intervals, mean_error_of, yerr=0, fmt=ap['fmt_of'],
             color=ap['color_of'], markersize=15, label='OF')
plt.errorbar(intervals, mean_error_cof, yerr=0, fmt=ap['fmt_cof'],
             color=ap['color_cof'], markersize=8, label='COF')
plt.errorbar(intervals, mean_error_lognormal, yerr=0, fmt=ap['fmt_logn'],
             color=ap['color_logn'], markersize=8, label='MLE Lognormal')
plt.legend(loc='upper left', fontsize=17)
plt.title(f'Occupancy: {occupancy}%', fontsize=17)
plt.xlabel('Amplitude interval', fontsize=17)
plt.ylabel('Mean of error_absolute (ADC counts)', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots(occupancy)
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(intervals, mean_error_gaussian, 0, ax, ax1, ap['color_gauss'], ' ',
                 'MLE Gaussian', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(intervals, mean_error_gaussian, 0, ax, ax1, ap['color_gauss'], ' ',
                 'MLE Gaussian', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

plt.show()
