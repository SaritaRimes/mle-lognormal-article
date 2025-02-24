import numpy as np
from fitter import Fitter
from matplotlib import pyplot as plt

from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_noise
from ks_statistic.fittings_noise.data_plots import return_data_plots

# Defining some constants
occupancy = 30
mean_pileup = 50
quantity_signals = 2000000
number_iterations = 10

# Defining plot aspects
color_gauss = 'black'
color_logn = 'gray'
color_grid = 'lightgrey'

# Creating some structures
sumsquares_normal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
sumsquares_lognormal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns

# Estimating and storing the data of methods
occupancies = np.array([10, 30, 50, 80])
i = 0  # column, which is equivalent to the occupancy
for occupancy in occupancies:
    # Importing the noise data
    noise = import_noise(occupancy, mean_pileup, quantity_signals)

    # Calculating the number of signals in each of the 10 sets
    number_signals = int(quantity_signals / number_iterations)

    for it in range(number_iterations):
        print("Occupancy: " + str(occupancy) + ",\titeration: " + str(it + 1))

        # Defining the range of signals in each iteration
        start = it * number_signals
        end = (it + 1) * number_signals

        # Creating the fitting of the two distributions
        f = Fitter(noise[start:end], distributions=['lognorm', 'norm'])
        f.fit()
        summary = f.summary()

        # Storing the values of Sums Of Square method for each distribution
        sumsquares_normal[it, i] = summary.sumsquare_error.norm
        sumsquares_lognormal[it, i] = summary.sumsquare_error.lognorm

    i += 1

# Estimating the error_mean and standard deviation of the methods for the two distributions
mean_sumsquares_normal = np.mean(sumsquares_normal, axis=0)
mean_sumsquares_lognormal = np.mean(sumsquares_lognormal, axis=0)
std_sumsquares_normal = np.std(sumsquares_normal, axis=0)
std_sumsquares_lognormal = np.std(sumsquares_lognormal, axis=0)

# Ploting KS Statistic figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_sumsquares_normal, yerr=std_sumsquares_normal, fmt='.-', color=color_gauss,
             markersize=15, label='Gaussian', capsize=5)
plt.errorbar(occupancies, mean_sumsquares_lognormal, yerr=std_sumsquares_lognormal, fmt='.-', color=color_logn,
             markersize=15, label='Lognormal', capsize=5)
plt.legend(loc='upper right', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Sum of Squares', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('sumsquares')
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, mean_sumsquares_normal, std_sumsquares_normal, ax, ax1, color_gauss, ' ',
                 'Gaussian', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, mean_sumsquares_normal, std_sumsquares_normal, ax, ax1, color_gauss, ' ',
                 'Gaussian', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

# Ploting Sum of Squares figure
# plt.rcParams['figure.autolayout'] = True
# plt.figure(figsize=(10, 6))
# fig, ax = plt.subplots(figsize=(10, 6))
# plt.plot(occupancies, sumsquares[0], '.-', color=color_gauss, markersize=15, label='Gaussian')
# plt.plot(occupancies, sumsquares[1], '.-', color=color_logn, markersize=15, label='Lognormal')
# plt.legend(loc='upper right', fontsize=19)
# plt.xlabel('Occupancy (%)', fontsize=17)
# plt.ylabel('Sum of Squares Error', fontsize=17)
# plt.grid(color=color_grid, zorder=0)
# [x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('sumsquares')
# plt.xlim(x_limit)
# plt.ylim(y_limit)
# # x axis
# ax1 = ax.twiny()
# configure_x_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
#                  x_axis_arguments)
# # y axis
# ax1 = ax.twinx()
# configure_y_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
#                  y_axis_arguments)
# # x and y axis
# ax.tick_params(which="major", axis='both', length=14, labelsize=15)
# ax.tick_params(which="minor", axis='both', length=11)

# Ploting both Sum of Squares and KS Statistic figures
# plt.rcParams['figure.autolayout'] = True
# plt.figure(figsize=(10, 6))
# fig, ax = plt.subplots(figsize=(10, 6))
# plt.plot(occupancies, sumsquares[0], '.-', color=color_gauss, markersize=15, label='Sum of Squares Gaussian')
# plt.plot(occupancies, sumsquares[1], '.-', color=color_logn, markersize=15, label='Sum of Squares Lognormal')
# plt.plot(occupancies, ks_statistic[0], '^--', color=color_gauss, markersize=9, label='KS Statistic Gaussian')
# plt.plot(occupancies, ks_statistic[1], '^--', color=color_logn, markersize=9, label='KS Statistic Lognormal')
# plt.legend(loc='upper right', fontsize=19)
# plt.xlabel('Occupancy (%)', fontsize=17)
# plt.ylabel('Magnitude', fontsize=17)
# plt.grid(color=color_grid, zorder=0)
# [x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('sumsquares+ks_statistic')
# plt.xlim(x_limit)
# plt.ylim(y_limit)
# # x axis
# ax1 = ax.twiny()
# configure_x_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Sum of Squares Gaussian', x_limit, y_limit,
#                  x_axis_arguments)
# # y axis
# ax1 = ax.twinx()
# configure_y_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Sum of Squares Gaussian', x_limit, y_limit,
#                  y_axis_arguments)
# # x and y axis
# ax.tick_params(which="major", axis='both', length=14, labelsize=15)
# ax.tick_params(which="minor", axis='both', length=11)

plt.show()
