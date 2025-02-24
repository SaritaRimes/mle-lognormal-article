import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from amplitude_range_analysis.std_error.data_plots import return_data_plots
from amplitude_range_analysis.error_amplitude_range_quantile import mean_std_error_amplitude_range, \
    define_intervals, define_midpoints_intervals, define_size_intervals
from import_data import import_amplitude_crossvalidation

# Defining some constants
occupancy = 80
number_iterations = 10
initial_amplitude_min = 10
initial_amplitude_max = 20
number_intervals = 10
error_type = 'absolute'

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.', 'fmt_of': '.', 'fmt_cof': '.', 'fmt_logn': '.'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Declaring some structures
std_error_gauss = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
std_error_of = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
std_error_cof = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
std_error_logn = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
amplitude_range = np.zeros([number_iterations, number_intervals + 1])

for it in range(number_iterations):
    print(f'Occupancy: {occupancy}%, iteration: {it + 1}')

    # Importing the data
    [amplitude_gauss, amplitude_of, amplitude_cof, amplitude_logn, amplitude_true] \
        = import_amplitude_crossvalidation(occupancy, it + 1)

    # Calculating the error_mean and standard deviation for de amplitudes range
    [_, std_error_gauss[it]] = mean_std_error_amplitude_range(amplitude_true, amplitude_gauss, number_intervals,
                                                              error_type)
    [_, std_error_of[it]] = mean_std_error_amplitude_range(amplitude_true, amplitude_of, number_intervals,
                                                           error_type)
    [_, std_error_cof[it]] = mean_std_error_amplitude_range(amplitude_true, amplitude_cof, number_intervals,
                                                            error_type)
    [_, std_error_logn[it]] = mean_std_error_amplitude_range(amplitude_true, amplitude_logn, number_intervals,
                                                             error_type)

    amplitude_range[it] = define_intervals(amplitude_true, number_intervals)

# Estimating the error_mean and standard deviation of the error_absolute
mean_std_error_gauss = np.mean(std_error_gauss, axis=0)
mean_std_error_of = np.mean(std_error_of, axis=0)
mean_std_error_cof = np.mean(std_error_cof, axis=0)
mean_std_error_logn = np.mean(std_error_logn, axis=0)
std_std_error_gauss = np.std(std_error_gauss, axis=0)
std_std_error_of = np.std(std_error_of, axis=0)
std_std_error_cof = np.std(std_error_cof, axis=0)
std_std_error_logn = np.std(std_error_logn, axis=0)

# Defining the intervals
intervals = np.mean(amplitude_range, axis=0)
size_intervals = define_size_intervals(intervals) / 2
midpoint_intervals = define_midpoints_intervals(intervals).astype(int)
indexes_plots = np.arange(1, len(intervals))
size_intervals_indexes = 0.5 * np.ones(len(indexes_plots))

# Organizing the data to plot
mean_std_error_gauss_plot = [mean_std_error_gauss[0]] + list(mean_std_error_gauss)
mean_std_error_of_plot = [mean_std_error_of[0]] + list(mean_std_error_of)
mean_std_error_cof_plot = [mean_std_error_cof[0]] + list(mean_std_error_cof)
mean_std_error_logn_plot = [mean_std_error_logn[0]] + list(mean_std_error_logn)
std_std_error_gauss_plot = [std_std_error_gauss[0]] + list(std_std_error_gauss)
std_std_error_of_plot = [std_std_error_of[0]] + list(std_std_error_of)
std_std_error_cof_plot = [std_std_error_cof[0]] + list(std_std_error_cof)
std_std_error_logn_plot = [std_std_error_logn[0]] + list(std_std_error_logn)

# Plotting the graphs
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams['figure.autolayout'] = True
# First way
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, loc_legend] \
    = return_data_plots(occupancy, 1, 0, 'standard deviation', error_type)
_, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
# MLE Gaussian
plt.errorbar(midpoint_intervals[1:], mean_std_error_gauss[1:], xerr=size_intervals[1:], yerr=std_std_error_gauss[1:],
             fmt=ap['fmt_gauss'], capsize=0, color=ap['color_gauss'], alpha=alpha_graphs, markersize=6,
             label='MLE Gaussian')
# OF
plt.errorbar(midpoint_intervals[1:], mean_std_error_of[1:], xerr=size_intervals[1:], yerr=std_std_error_of[1:],
             fmt=ap['fmt_of'], capsize=0, color=ap['color_of'], alpha=alpha_graphs, markersize=6, label='OF')
# COF
plt.errorbar(midpoint_intervals[1:], mean_std_error_cof[1:], xerr=size_intervals[1:], yerr=std_std_error_cof[1:],
             fmt=ap['fmt_cof'], capsize=0, color=ap['color_cof'], alpha=alpha_graphs, markersize=6, label='MAE')
# MLE Lognormal
plt.errorbar(midpoint_intervals[1:], mean_std_error_logn[1:], xerr=size_intervals[1:], yerr=std_std_error_logn[1:],
             fmt=ap['fmt_logn'], capsize=0, color=ap['color_logn'], alpha=alpha_graphs, markersize=6,
             label='MLE Log-normal')
plt.legend(loc=loc_legend, fontsize=legends_factor * 10)
plt.title(f'Occupancy: {occupancy}%', fontsize=legends_factor * 10)
plt.xlabel('Reference amplitude (ADC counts)', fontsize=legends_factor * 10)
plt.ylabel('Error Std (ADC counts)', fontsize=legends_factor * 10)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/amplitude_range_ocup{occupancy}.png',
            dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')

# Second way
# [x_limit, y_limit, x_axis_arguments, y_axis_arguments, loc_legend, loc_legend_bbox] \
#     = return_data_plots(occupancy, 2, len(intervals))
# _, ax = plt.subplots(figsize=(10, 6))
# plt.errorbar(indexes_plots[1:], mean_std_error_gauss[1:], xerr=size_intervals_indexes[1:], yerr=std_std_error_gauss[1:],
#              fmt=ap['fmt_gauss'], capsize=0, color=ap['color_gauss'], markersize=10, label='MLE Gaussian')
# plt.errorbar(indexes_plots[1:], mean_std_error_of[1:], xerr=size_intervals_indexes[1:], yerr=std_std_error_of[1:], fmt=ap['fmt_of'],
#              capsize=0, color=ap['color_of'], markersize=10, label='OF')
# plt.errorbar(indexes_plots[1:], mean_std_error_cof[1:], xerr=size_intervals_indexes[1:], yerr=std_std_error_cof[1:], fmt=ap['fmt_cof'],
#              capsize=0, color=ap['color_cof'], markersize=10, label='COF')
# plt.errorbar(indexes_plots[1:], mean_std_error_logn[1:], xerr=size_intervals_indexes[1:], yerr=std_std_error_logn[1:],
#              fmt=ap['fmt_logn'], capsize=0, color=ap['color_logn'], markersize=10, label='MLE Lognormal')
# plt.legend(loc=loc_legend, bbox_to_anchor=loc_legend_bbox, fontsize=17)
# plt.title(f'Occupancy: {occupancy}%', fontsize=17)
# plt.xlabel('Reference amplitude (ADC counts)', fontsize=17)
# plt.ylabel('Standard Deviation of error_absolute (ADC counts)', fontsize=17)
# plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
# plt.xlim(x_limit)
# plt.ylim(y_limit)
# # x axis
# plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
# ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# ax.set_xticklabels(intervals.astype(int))
# # y axis
# plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
# ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# # x and y axis
# ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=8,
#                labelsize=17)
# ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
