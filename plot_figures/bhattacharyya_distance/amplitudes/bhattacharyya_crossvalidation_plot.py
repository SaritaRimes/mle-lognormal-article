import numpy as np
from matplotlib import pyplot as plt

from auxiliary_functions import number_bins, find_index_positive
from bhattacharyya_distance.amplitudes.data_plots import return_data_plots
from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_crossvalidation


# Defining some constants
number_iterations = 10
occupancies = [10, 30, 50, 80]
width_bins = 1

# Defining plot aspects
ap = {'color_gauss': 'black', 'color_of': 'grey', 'color_cof': 'black', 'color_logn': 'grey',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '^--', 'fmt_logn': '^--'}  # plots aspects
color_grid = 'lightgrey'

# Declaring some structures
bhatt_gaussian = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
bhatt_of = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
bhatt_cof = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
bhatt_lognormal = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns

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

        # Creating the PDF of all distributions
        pdf_amplitude_gaussian = amplitude_gaussian_hist / sum(amplitude_gaussian_hist)
        pdf_amplitude_of = amplitude_of_hist / sum(amplitude_of_hist)
        pdf_amplitude_cof = amplitude_cof_hist / sum(amplitude_cof_hist)
        pdf_amplitude_lognormal = amplitude_lognormal_hist / sum(amplitude_lognormal_hist)
        pdf_amplitude_true = amplitude_true_hist / sum(amplitude_true_hist)

        # Estimating the Bhattacharyya Distance
        # Gaussian
        idx1 = find_index_positive(bins_gaussian, amplitude_gaussian_hist, 1)
        idx2 = min(len(amplitude_gaussian_hist) - idx1, len(amplitude_true_hist))
        bhatt_gaussian[it, i] = - np.log(np.sum(np.sqrt(pdf_amplitude_true[:idx2]
                                                        * pdf_amplitude_gaussian[idx1:(idx2 + idx1)])))
        # OF
        idx1 = find_index_positive(bins_of, amplitude_of_hist, 1)
        idx2 = min(len(amplitude_of_hist) - idx1, len(amplitude_true_hist))
        bhatt_of[it, i] = - np.log(np.sum(np.sqrt(pdf_amplitude_true[:idx2] * pdf_amplitude_of[idx1:(idx2 + idx1)])))
        # COF
        idx1 = find_index_positive(bins_cof, amplitude_cof_hist, 1)
        idx2 = min(len(amplitude_cof_hist) - idx1, len(amplitude_true_hist))
        bhatt_cof[it, i] = - np.log(np.sum(np.sqrt(pdf_amplitude_true[:idx2] * pdf_amplitude_cof[idx1:(idx2 + idx1)])))
        # Lognormal
        idx1 = find_index_positive(bins_lognormal, amplitude_lognormal_hist, 1)
        idx2 = min(len(amplitude_lognormal_hist) - idx1, len(amplitude_true_hist))
        bhatt_lognormal[it, i] = - np.log(np.sum(np.sqrt(pdf_amplitude_true[:idx2]
                                                         * pdf_amplitude_lognormal[idx1:(idx2 + idx1)])))

    i += 1

# Estimating the error_mean and standard deviation of the bhattacharyya distance
mean_bhatt_gaussian = np.mean(bhatt_gaussian, axis=0)
mean_bhatt_of = np.mean(bhatt_of, axis=0)
mean_bhatt_cof = np.mean(bhatt_cof, axis=0)
mean_bhatt_lognormal = np.mean(bhatt_lognormal, axis=0)
std_bhatt_gaussian = np.std(bhatt_gaussian, axis=0)
std_bhatt_of = np.std(bhatt_of, axis=0)
std_bhatt_cof = np.std(bhatt_cof, axis=0)
std_bhatt_lognormal = np.std(bhatt_lognormal, axis=0)

# Ploting bhattacharyya distance figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_bhatt_gaussian, yerr=std_bhatt_gaussian, fmt=ap['fmt_gauss'],
             color=ap['color_gauss'], markersize=15, label='Gaussian')
plt.errorbar(occupancies, mean_bhatt_of, yerr=std_bhatt_of, fmt=ap['fmt_of'],
             color=ap['color_of'], markersize=15, label='OF')
plt.errorbar(occupancies, mean_bhatt_cof, yerr=std_bhatt_cof, fmt=ap['fmt_cof'],
             color=ap['color_cof'], markersize=8, label='COF')
plt.errorbar(occupancies, mean_bhatt_lognormal, yerr=std_bhatt_lognormal, fmt=ap['fmt_logn'],
             color=ap['color_logn'], markersize=8, label='Lognormal')
plt.legend(loc='upper left', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Bhattacharyya Distance', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, mean_bhatt_gaussian, std_bhatt_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, mean_bhatt_gaussian, std_bhatt_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

plt.show()


