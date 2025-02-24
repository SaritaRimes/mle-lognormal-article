import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from amplitude_range_analysis.error_amplitude_range import relative_error
from amplitude_range_analysis.std_error.data_plots import return_data_plots
from amplitude_range_analysis.error_amplitude_range_quantile import mean_std_error_amplitude_range, \
    define_intervals, define_midpoints_intervals, define_size_intervals
from import_data import import_amplitude_crossvalidation

# Defining some constants
number_iterations = 10
occupancy = 10
initial_amplitude_min = 10
initial_amplitude_max = 20
number_intervals = 10

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.', 'fmt_of': '.', 'fmt_cof': '.', 'fmt_logn': '.'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Declaring some structures
mean_error_gauss = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
mean_error_of = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
mean_error_cof = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
mean_error_logn = np.zeros([number_iterations, number_intervals])  # iterations -> rows, intervals -> columns
amplitude_range = np.zeros([number_iterations, number_intervals + 1])

for it in range(number_iterations):
    print(f'Occupancy: {occupancy}%, iteration: {it + 1}')

    # Importing the data
    [amplitude_gauss, amplitude_of, amplitude_cof, amplitude_logn, amplitude_true] \
        = import_amplitude_crossvalidation(occupancy, it + 1)

    # Apagar depois
    indices = np.where((np.array(amplitude_true) > 0) & (np.array(amplitude_true) <= 10.5))
    amp_true = np.array(amplitude_true)[indices]
    amp_gauss = np.array(amplitude_gauss)[indices]
    amp_of = np.array(amplitude_of)[indices]
    amp_cof = np.array(amplitude_cof)[indices]
    amp_logn = np.array(amplitude_logn)[indices]
    plt.hist(relative_error(amp_gauss, amp_true), bins=100, histtype='step', label='MLE Gaussian')
    plt.hist(relative_error(amp_of, amp_true), bins=100, histtype='step', label='OF')
    plt.hist(relative_error(amp_cof, amp_true), bins=100, histtype='step', label='COF')
    plt.hist(relative_error(amp_logn, amp_true), bins=100, histtype='step', label='MLE Lognormal')
    plt.legend()
    #

    # Calculating the error_mean and standard deviation for de amplitudes range
    [mean_error_gauss[it], _] = mean_std_error_amplitude_range(amplitude_true, amplitude_gauss, number_intervals)
    [mean_error_of[it], _] = mean_std_error_amplitude_range(amplitude_true, amplitude_of, number_intervals)
    [mean_error_cof[it], _] = mean_std_error_amplitude_range(amplitude_true, amplitude_cof, number_intervals)
    [mean_error_logn[it], _] = mean_std_error_amplitude_range(amplitude_true, amplitude_logn, number_intervals)

    amplitude_range[it] = define_intervals(amplitude_true, number_intervals)

# Estimating the error_mean and standard deviation of the error_absolute
mean_mean_error_gauss = np.mean(mean_error_gauss, axis=0)
mean_mean_error_of = np.mean(mean_error_of, axis=0)
mean_mean_error_cof = np.mean(mean_error_cof, axis=0)
mean_mean_error_logn = np.mean(mean_error_logn, axis=0)
std_mean_error_gauss = np.std(mean_error_gauss, axis=0)
std_mean_error_of = np.std(mean_error_of, axis=0)
std_mean_error_cof = np.std(mean_error_cof, axis=0)
std_mean_error_logn = np.std(mean_error_logn, axis=0)

# Defining the intervals
intervals = np.mean(amplitude_range, axis=0)
size_intervals = define_size_intervals(intervals) / 2
midpoint_intervals = define_midpoints_intervals(intervals).astype(int)
indexes_plots = np.arange(1, len(intervals))
size_intervals_indexes = 0.5 * np.ones(len(indexes_plots))

# Organizing the data to plot
mean_mean_error_gauss_plot = [mean_mean_error_gauss[0]] + list(mean_mean_error_gauss)
mean_mean_error_of_plot = [mean_mean_error_of[0]] + list(mean_mean_error_of)
mean_mean_error_cof_plot = [mean_mean_error_cof[0]] + list(mean_mean_error_cof)
mean_mean_error_logn_plot = [mean_mean_error_logn[0]] + list(mean_mean_error_logn)
std_mean_error_gauss_plot = [std_mean_error_gauss[0]] + list(std_mean_error_gauss)
std_mean_error_of_plot = [std_mean_error_of[0]] + list(std_mean_error_of)
std_mean_error_cof_plot = [std_mean_error_cof[0]] + list(std_mean_error_cof)
std_mean_error_logn_plot = [std_mean_error_logn[0]] + list(std_mean_error_logn)

# Plotting the graphs
plt.rcParams['figure.autolayout'] = True
# First way
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, loc_legend, loc_legend_bbox] \
    = return_data_plots(occupancy, 1, 0, 'error_mean')
_, ax = plt.subplots(figsize=(10, 6))
# MLE Gaussian
plt.errorbar(midpoint_intervals[1:], mean_mean_error_gauss[1:], xerr=size_intervals[1:], yerr=std_mean_error_gauss[1:],
             fmt=ap['fmt_gauss'], capsize=0, color=ap['color_gauss'], alpha=alpha_graphs, markersize=10,
             label='MLE Gaussian')
# OF
plt.errorbar(midpoint_intervals[1:], mean_mean_error_of[1:], xerr=size_intervals[1:], yerr=std_mean_error_of[1:],
             fmt=ap['fmt_of'], capsize=0, color=ap['color_of'], alpha=alpha_graphs, markersize=10, label='OF')
# COF
plt.errorbar(midpoint_intervals[1:], mean_mean_error_cof[1:], xerr=size_intervals[1:], yerr=std_mean_error_cof[1:], fmt=ap['fmt_cof'],
             capsize=0, color=ap['color_cof'], alpha=alpha_graphs, markersize=10, label='COF')
# MLE Lognormal
plt.errorbar(midpoint_intervals[1:], mean_mean_error_logn[1:], xerr=size_intervals[1:], yerr=std_mean_error_logn[1:], fmt=ap['fmt_logn'],
             capsize=0, color=ap['color_logn'], alpha=alpha_graphs, markersize=10, label='MLE Lognormal')
plt.legend(loc=loc_legend, bbox_to_anchor=loc_legend_bbox, fontsize=17)
plt.title(f'Occupancy: {occupancy}%', fontsize=17)
plt.xlabel('Reference amplitude (ADC counts)', fontsize=17)
plt.ylabel('Mean of relative error_absolute (ADC counts)', fontsize=17)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=8,
               labelsize=17)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

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
