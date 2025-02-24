import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from amplitude_range_analysis.error_amplitude_range import relative_error
from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_crossvalidation
from error_mean.error_relative.data_plots import return_data_plots

# Declaring some constants
number_iterations = 10

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '.-', 'fmt_logn': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Declaring some structures
mean_gaussian = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_of = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_cof = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_lognormal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns

occupancies = [10, 30, 50, 80]
i = 0  # column, which is equivalent to the occupancy
for oc in occupancies:
    print('------------------------------')

    for it in range(10):
        print(f'Occupancy: {oc}%, iteration: {it + 1}')
        # Importing the data
        [amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
            = import_amplitude_crossvalidation(oc, it + 1)

        # Calculating the errors
        indexes_amplitude_true_10 = np.where(np.array(amplitude_true) > 10)
        error_gaussian = relative_error(amplitude_gaussian, amplitude_true)[indexes_amplitude_true_10]
        error_of = relative_error(amplitude_of, amplitude_true)[indexes_amplitude_true_10]
        error_cof = relative_error(amplitude_cof, amplitude_true)[indexes_amplitude_true_10]
        error_lognormal = relative_error(amplitude_lognormal, amplitude_true)[indexes_amplitude_true_10]

        # Estimating the standard deviation of the errors
        mean_gaussian[it, i] = np.mean(error_gaussian)
        mean_of[it, i] = np.mean(error_of)
        mean_cof[it, i] = np.mean(error_cof)
        mean_lognormal[it, i] = np.mean(error_lognormal)

    i += 1

# Estimating the error_mean and standard deviation of the standard deviation
mean_mean_gaussian = np.mean(mean_gaussian, axis=0)
mean_mean_of = np.mean(mean_of, axis=0)
mean_mean_cof = np.mean(mean_cof, axis=0)
mean_mean_lognormal = np.mean(mean_lognormal, axis=0)
std_mean_gaussian = np.std(mean_gaussian, axis=0)
std_mean_of = np.std(mean_of, axis=0)
std_mean_cof = np.std(mean_cof, axis=0)
std_mean_lognormal = np.std(mean_lognormal, axis=0)

# Ploting error_mean squared error_absolute figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_mean_gaussian, yerr=std_mean_gaussian, fmt=ap['fmt_gauss'], color=ap['color_gauss'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='MLE Gaussian')
plt.errorbar(occupancies, mean_mean_of, yerr=std_mean_of, fmt=ap['fmt_of'], color=ap['color_of'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_mean_cof, yerr=std_mean_cof, fmt=ap['fmt_cof'], color=ap['color_cof'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='COF')
plt.errorbar(occupancies, mean_mean_lognormal, yerr=std_mean_lognormal, fmt=ap['fmt_logn'], color=ap['color_logn'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='MLE Lognormal')
plt.legend(loc='upper left', fontsize=18)
plt.xlabel('Occupancy (%)', fontsize=16)
plt.ylabel('Mean of relative error (ADC counts)', fontsize=16)
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
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=8,
               labelsize=17)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
