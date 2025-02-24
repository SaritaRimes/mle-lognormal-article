import numpy as np
from fitter import Fitter
from matplotlib import pyplot as plt

from configure_axis_plot import configure_x_axis, configure_y_axis
from import_data import import_noise
from ks_statistic.fittings_noise.data_plots import return_data_plots

# Defining noise occupancy and pile-up error_mean
occupancy = 30
mean_pileup = 50

# Defining plot aspects
color_gauss = 'black'
color_logn = 'gray'
color_grid = 'lightgrey'

# Estimating and storing the data of methods
sumsquares = np.zeros([2, 4])
ks_statistic = np.zeros([2, 4])
occupancies = np.array([10, 30, 50, 80])
i = 0
for occupancy in occupancies:
    # Importing the noise data
    noise = import_noise(occupancy, mean_pileup)

    # Creating the fitting of the two distributions
    f = Fitter(noise, distributions=['lognorm', 'norm'])
    f.fit()
    summary = f.summary()

    # Storing the values of Sums Of Square method for each distribution
    sumsquares[0][i] = summary.sumsquare_error.norm
    sumsquares[1][i] = summary.sumsquare_error.lognorm

    # Storing the values of KS Statistic method for each distribution
    ks_statistic[0][i] = summary.ks_statistic.norm
    ks_statistic[1][i] = summary.ks_statistic.lognorm

    i += 1

# Ploting Sum of Squares figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(occupancies, sumsquares[0], '.-', color=color_gauss, markersize=15, label='Gaussian')
plt.plot(occupancies, sumsquares[1], '.-', color=color_logn, markersize=15, label='Lognormal')
plt.legend(loc='upper right', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Sum of Squares Error', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('sumsquares')
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
                 x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
                 y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)


# Ploting KS Statistic figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(occupancies, ks_statistic[0], '.-', color=color_gauss, markersize=15, label='Gaussian')
plt.plot(occupancies, ks_statistic[1], '.-', color=color_logn, markersize=15, label='Lognormal')
plt.legend(loc='upper right', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Kolmogorov–Smirnov Statistic', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('ks_statistic')
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
                 x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, sumsquares[0], ax, ax1, color_gauss, ' ', 'Gaussian', x_limit, y_limit,
                 y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)


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
