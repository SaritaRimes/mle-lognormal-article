import matplotlib
import numpy as np
from fitter import Fitter
from matplotlib import pyplot as plt

from import_data import import_noise
from ks_statistic.fittings_noise.data_plots import return_data_plots

# Defining some constants
occupancy = 30
mean_pileup = 50
quantity_signals = 2000000
number_iterations = 10

# Defining plot aspects
color_gauss = 'black'
color_logn = 'black'
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 1
legends_factor = 0.85

# Creating some structures
ks_statistic_normal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
ks_statistic_lognormal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns

# Estimating and storing the data of methods
occupancies = np.array([10, 30, 50, 80])
i = 0  # column, which is equivalent to the occupancy
for occupancy in occupancies:
    print('------------------------------')

    # Importing the noise data
    noise = import_noise(occupancy, mean_pileup, quantity_signals)

    # Calculating the number of signals in each of the 10 sets
    number_signals = int(quantity_signals / number_iterations)

    for it in range(number_iterations):
        print("Occupancy: " + str(occupancy) + ",\titeration: " + str(it + 1))

        # Defining the range of signals in each iteration
        start = it * number_signals
        end = (it + 1) * number_signals

        # Defining the number of bins
        bins = np.histogram_bin_edges(noise[start:end], bins='fd')
        number_bins = len(bins) - 1

        # Creating the fitting of the two distributions
        f = Fitter(noise[start:end], bins=number_bins, distributions=['lognorm', 'norm'])
        f.fit()
        summary = f.summary()

        # Storing the values of KS Statistic method for each distribution
        ks_statistic_normal[it, i] = summary.ks_statistic.norm
        ks_statistic_lognormal[it, i] = summary.ks_statistic.lognorm

    i += 1

# Estimating the error_mean and standard deviation of the methods for the two distributions
mean_ks_statistic_normal = np.mean(ks_statistic_normal, axis=0)
mean_ks_statistic_lognormal = np.mean(ks_statistic_lognormal, axis=0)
std_ks_statistic_normal = np.std(ks_statistic_normal, axis=0)
std_ks_statistic_lognormal = np.std(ks_statistic_lognormal, axis=0)

# Ploting KS Statistic figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('ks_statistic')
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_ks_statistic_normal, yerr=20*std_ks_statistic_normal, fmt='.-', color=color_gauss,
             markersize=10, label='Gaussian', capsize=5)
plt.errorbar(occupancies, mean_ks_statistic_lognormal, yerr=20*std_ks_statistic_lognormal, fmt='.--', color=color_logn,
             markersize=10, label='Log-normal', capsize=5)
plt.legend(loc='upper right', fontsize=legends_factor * 10)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 10)
plt.ylabel('KS Statistic', fontsize=legends_factor * 10)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
ax.yaxis.get_offset_text().set_fontsize(legends_factor * 10)
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

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

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/ks_statistic_gauss_logn_mPu{mean_pileup}.png',
            dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
