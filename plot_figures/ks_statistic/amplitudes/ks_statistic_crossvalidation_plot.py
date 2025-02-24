import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import ks_2samp

from auxiliary_functions import find_index_positive, number_bins
from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_crossvalidation
from data_plots import return_data_plots

# Defining some constants
number_iterations = 10
occupancies = [10, 30, 50, 80]
width_bins = 10

# Defining plot aspects
ap = {'color_gauss': 'black', 'color_of': 'grey', 'color_cof': 'black', 'color_logn': 'grey',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '^--', 'fmt_logn': '^--'}  # plots aspects
color_grid = 'lightgrey'

# Declaring some structures
ks_statistic_gaussian = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
ks_statistic_of = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
ks_statistic_cof = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
ks_statistic_lognormal = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns

i = 0  # column, which is equivalent to the occupancy
for oc in occupancies:
    print('------------------------------')

    for it in range(number_iterations):
        print(f'Occupancy: {oc}%, iteration: {it + 1}')

        # Importing the data
        [amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
            = import_amplitude_crossvalidation(oc, it + 1)

        # Creating error_histograms of data
        n_bins = number_bins(amplitude_gaussian, width_bins)
        amplitude_gaussian_hist, bins_gaussian = np.histogram(amplitude_gaussian, bins=n_bins, density=True)
        n_bins = number_bins(amplitude_of, width_bins)
        amplitude_of_hist, bins_of = np.histogram(amplitude_of, bins=n_bins, density=True)
        n_bins = number_bins(amplitude_cof, width_bins)
        amplitude_cof_hist, bins_cof = np.histogram(amplitude_cof, bins=n_bins, density=True)
        n_bins = number_bins(amplitude_lognormal, width_bins)
        amplitude_lognormal_hist, bins_lognormal = np.histogram(amplitude_lognormal, bins=n_bins, density=True)
        n_bins = number_bins(amplitude_true, width_bins)
        amplitude_true_hist, bins_true = np.histogram(amplitude_true, bins=n_bins, density=True)

        # Estimating ks statistic
        # plt.figure()
        idx1 = find_index_positive(bins_gaussian, amplitude_gaussian_hist, 1)
        ks_statistic_gaussian[it, i] = ks_2samp(amplitude_true_hist, amplitude_gaussian_hist[idx1:]).statistic
        # plt.plot(amplitude_gaussian_hist[idx1:], label='Gaussian')
        idx1 = find_index_positive(bins_of, amplitude_of_hist, 1)
        ks_statistic_of[it, i] = ks_2samp(amplitude_true_hist, amplitude_of_hist[idx1:]).statistic
        # plt.plot(amplitude_of_hist[idx1:], label='OF')
        idx1 = find_index_positive(bins_cof, amplitude_cof_hist, 1)
        ks_statistic_cof[it, i] = ks_2samp(amplitude_true_hist, amplitude_cof_hist[idx1:]).statistic
        # plt.plot(amplitude_cof_hist[idx1:], label='COF')
        idx1 = find_index_positive(bins_lognormal, amplitude_lognormal_hist, 1)
        ks_statistic_lognormal[it, i] = ks_2samp(amplitude_true_hist, amplitude_lognormal_hist[idx1:]).statistic
        # plt.plot(amplitude_lognormal_hist[idx1:], label='Lognormal')
        # plt.plot(amplitude_true_hist, label='True')
        # plt.title(f'Occupancy: {oc}%, Iterarion: {it}')
        # plt.legend()
        # plt.show()

        # Calculating CDFs
        # idx1 = find_index_positive(bins_gaussian, amplitude_gaussian_hist, 1)
        # cdf_gaussian = np.cumsum(amplitude_gaussian_hist[idx1:] / sum(amplitude_gaussian_hist[idx1:]))
        # idx1 = find_index_positive(bins_of, amplitude_of_hist, 1)
        # cdf_of = np.cumsum(amplitude_of_hist[idx1:] / sum(amplitude_of_hist[idx1:]))
        # idx1 = find_index_positive(bins_cof, amplitude_cof_hist, 1)
        # cdf_cof = np.cumsum(amplitude_cof_hist[idx1:] / sum(amplitude_cof_hist[idx1:]))
        # idx1 = find_index_positive(bins_lognormal, amplitude_lognormal_hist, 1)
        # cdf_lognormal = np.cumsum(amplitude_lognormal_hist[idx1:] / sum(amplitude_lognormal_hist[idx1:]))
        # cdf_true = np.cumsum(amplitude_true_hist / sum(amplitude_true_hist))
        #
        # # Estimating ks statistic
        # idx2 = min(len(cdf_true), len(cdf_gaussian))
        # ks_statistic_gaussian[it, i] = ks_2samp(cdf_true[:idx2], cdf_gaussian[:idx2]).statistic
        # idx2 = min(len(cdf_true), len(cdf_of))
        # ks_statistic_of[it, i] = ks_2samp(cdf_true[:idx2], cdf_of[:idx2]).statistic
        # idx2 = min(len(cdf_true), len(cdf_cof))
        # ks_statistic_cof[it, i] = ks_2samp(cdf_true[:idx2], cdf_cof[:idx2]).statistic
        # idx2 = min(len(cdf_true), len(cdf_lognormal))
        # ks_statistic_lognormal[it, i] = ks_2samp(cdf_true[:idx2], cdf_lognormal[:idx2]).statistic

    i += 1

# Estimating the error_mean and standard deviation of the ks statistics
mean_ks_statistic_gaussian = np.mean(ks_statistic_gaussian, axis=0)
mean_ks_statistic_of = np.mean(ks_statistic_of, axis=0)
mean_ks_statistic_cof = np.mean(ks_statistic_cof, axis=0)
mean_ks_statistic_lognormal = np.mean(ks_statistic_lognormal, axis=0)
std_ks_statistic_gaussian = np.std(ks_statistic_gaussian, axis=0)
std_ks_statistic_of = np.std(ks_statistic_of, axis=0)
std_ks_statistic_cof = np.std(ks_statistic_cof, axis=0)
std_ks_statistic_lognormal = np.std(ks_statistic_lognormal, axis=0)

# Ploting ks statistic figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_ks_statistic_gaussian, yerr=std_ks_statistic_gaussian, fmt=ap['fmt_gauss'],
             color=ap['color_gauss'], markersize=15, label='Gaussian')
plt.errorbar(occupancies, mean_ks_statistic_of, yerr=std_ks_statistic_of, fmt=ap['fmt_of'],
             color=ap['color_of'], markersize=15, label='OF')
plt.errorbar(occupancies, mean_ks_statistic_cof, yerr=std_ks_statistic_cof, fmt=ap['fmt_cof'],
             color=ap['color_cof'], markersize=8, label='COF')
plt.errorbar(occupancies, mean_ks_statistic_lognormal, yerr=std_ks_statistic_lognormal, fmt=ap['fmt_logn'],
             color=ap['color_logn'], markersize=8, label='Lognormal')
plt.legend(loc='upper right', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Kolmogorov–Smirnov Statistic', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, mean_ks_statistic_gaussian, std_ks_statistic_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, mean_ks_statistic_gaussian, std_ks_statistic_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

plt.show()
