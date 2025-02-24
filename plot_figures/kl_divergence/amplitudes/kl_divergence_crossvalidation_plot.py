import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import rel_entr

from import_data import import_amplitude_crossvalidation
from data_plots import return_data_plots
from auxiliary_functions import find_index_positive, number_bins

# Defining some constants
number_iterations = 10
occupancies = [10, 30, 50, 80]
mean_pileup = 50

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '.-', 'fmt_logn': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Declaring some structures
kl_divergence_gaussian = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
kl_divergence_of = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
kl_divergence_cof = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns
kl_divergence_lognormal = np.zeros([number_iterations, len(occupancies)])  # iterations -> rows, occupancies -> columns

i = 0  # column, which is equivalent to the occupancy
for oc in occupancies:
    print('------------------------------')

    for it in range(number_iterations):
        print(f'Occupancy: {oc}%, iteration: {it + 1}')

        # Importing the data
        [amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
            = import_amplitude_crossvalidation(oc, it + 1)

        # Creating the histogram of the estimated data
        # Gaussian
        bins = np.histogram_bin_edges(amplitude_gaussian, bins='fd')
        width_bins_gaussian = bins[1] - bins[0]
        n_bins = number_bins(amplitude_gaussian, width_bins_gaussian)
        amplitude_gaussian_hist, bins_gaussian = np.histogram(amplitude_gaussian, n_bins, density=True)
        # OF
        bins = np.histogram_bin_edges(amplitude_of, bins='fd')
        width_bins_of = bins[1] - bins[0]
        n_bins = number_bins(amplitude_of, width_bins_of)
        amplitude_of_hist, bins_of = np.histogram(amplitude_of, n_bins, density=True)
        # COF
        bins = np.histogram_bin_edges(amplitude_cof, bins='fd')
        width_bins_cof = bins[1] - bins[0]
        n_bins = number_bins(amplitude_cof, width_bins_cof)
        amplitude_cof_hist, bins_cof = np.histogram(amplitude_cof, n_bins, density=True)
        # Lognormal
        bins = np.histogram_bin_edges(amplitude_lognormal, bins='fd')
        width_bins_lognormal = bins[1] - bins[0]
        n_bins = number_bins(amplitude_lognormal, width_bins_lognormal)
        amplitude_lognormal_hist, bins_lognormal = np.histogram(amplitude_lognormal, n_bins, density=True)

        # Creating the histogram of the true data
        # Gaussian
        n_bins = number_bins(amplitude_true, width_bins_gaussian)
        amplitude_true_gaussian_hist, _ = np.histogram(amplitude_true, n_bins, density=True)
        # OF
        n_bins = number_bins(amplitude_true, width_bins_of)
        amplitude_true_of_hist, _ = np.histogram(amplitude_true, n_bins, density=True)
        # COF
        n_bins = number_bins(amplitude_true, width_bins_cof)
        amplitude_true_cof_hist, _ = np.histogram(amplitude_true, n_bins, density=True)
        # Lognormal
        n_bins = number_bins(amplitude_true, width_bins_lognormal)
        amplitude_true_lognormal_hist, _ = np.histogram(amplitude_true, n_bins, density=True)

        # Normalizing the histogram of the estimated data
        amplitude_gaussian_hist_norm = amplitude_gaussian_hist / sum(amplitude_gaussian_hist)
        amplitude_of_hist_norm = amplitude_of_hist / sum(amplitude_of_hist)
        amplitude_cof_hist_norm = amplitude_cof_hist / sum(amplitude_cof_hist)
        amplitude_lognormal_hist_norm = amplitude_lognormal_hist / sum(amplitude_lognormal_hist)

        # Normalizing the histogram of the true data
        amplitude_true_gaussian_hist_norm = amplitude_true_gaussian_hist / sum(amplitude_true_gaussian_hist)
        amplitude_true_of_hist_norm = amplitude_true_of_hist / sum(amplitude_true_of_hist)
        amplitude_true_cof_hist_norm = amplitude_true_cof_hist / sum(amplitude_true_cof_hist)
        amplitude_true_lognormal_hist_norm = amplitude_true_lognormal_hist / sum(amplitude_true_lognormal_hist)

        # Estimating kl divergence
        # Gaussian
        idx1 = find_index_positive(bins_gaussian, amplitude_gaussian_hist_norm, 1)
        idx2 = find_index_positive(bins_gaussian, amplitude_gaussian_hist_norm, 2)
        kl_divergence_gaussian[it, i] = sum(rel_entr(amplitude_true_gaussian_hist_norm[0:idx2-idx1],
                                                     amplitude_gaussian_hist_norm[idx1:idx2]))
        # OF
        idx1 = find_index_positive(bins_of, amplitude_of_hist_norm, 1)
        idx2 = find_index_positive(bins_of, amplitude_of_hist_norm, 2)
        kl_divergence_of[it, i] = sum(rel_entr(amplitude_true_of_hist_norm[0:idx2-idx1],
                                               amplitude_of_hist_norm[idx1:idx2]))
        # COF
        idx1 = find_index_positive(bins_cof, amplitude_cof_hist_norm, 1)
        idx2 = find_index_positive(bins_cof, amplitude_cof_hist_norm, 2)
        kl_divergence_cof[it, i] = sum(rel_entr(amplitude_true_cof_hist_norm[0:idx2-idx1],
                                                amplitude_cof_hist_norm[idx1:idx2]))
        # Lognormal
        idx1 = find_index_positive(bins_lognormal, amplitude_lognormal_hist_norm, 1)
        idx2 = find_index_positive(bins_lognormal, amplitude_lognormal_hist_norm, 2)
        kl_divergence_lognormal[it, i] = sum(rel_entr(amplitude_true_lognormal_hist_norm[0:idx2-idx1],
                                                      amplitude_lognormal_hist_norm[idx1:idx2]))

    i += 1

# Estimating the error_mean and standard deviation of the kl divergence
mean_kl_divergence_gaussian = np.mean(kl_divergence_gaussian, axis=0)
mean_kl_divergence_of = np.mean(kl_divergence_of, axis=0)
mean_kl_divergence_cof = np.mean(kl_divergence_cof, axis=0)
mean_kl_divergence_lognormal = np.mean(kl_divergence_lognormal, axis=0)
std_kl_divergence_gaussian = np.std(kl_divergence_gaussian, axis=0)
std_kl_divergence_of = np.std(kl_divergence_of, axis=0)
std_kl_divergence_cof = np.std(kl_divergence_cof, axis=0)
std_kl_divergence_lognormal = np.std(kl_divergence_lognormal, axis=0)

# Ploting kl divergence figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams['figure.autolayout'] = True
_, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_kl_divergence_gaussian, yerr=std_kl_divergence_gaussian, fmt=ap['fmt_gauss'],
             color=ap['color_gauss'], alpha=alpha_graphs, markersize=10, capsize=5, label='Gaussian')
plt.errorbar(occupancies, mean_kl_divergence_of, yerr=std_kl_divergence_of, fmt=ap['fmt_of'],
             color=ap['color_of'], alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_kl_divergence_cof, yerr=std_kl_divergence_cof, fmt=ap['fmt_cof'],
             color=ap['color_cof'], alpha=alpha_graphs, markersize=10, capsize=5, label='MAE')
plt.errorbar(occupancies, mean_kl_divergence_lognormal, yerr=std_kl_divergence_lognormal, fmt=ap['fmt_logn'],
             color=ap['color_logn'], alpha=alpha_graphs, markersize=10, capsize=5, label='Log-normal')
plt.legend(loc='upper left', fontsize=legends_factor * 10)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 10)
plt.ylabel('KL Divergence', fontsize=legends_factor * 10)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
plt.xlim(x_limit)
plt.ylim(y_limit)
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

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/kl_divergence_mPu{mean_pileup}_occupancies.png',
            dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
