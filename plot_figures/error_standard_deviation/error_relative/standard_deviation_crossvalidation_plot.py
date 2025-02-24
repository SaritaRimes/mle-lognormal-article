import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from amplitude_range_analysis.error_amplitude_range import relative_error
from import_data import import_amplitude_crossvalidation
from error_standard_deviation.error_relative.data_plots import return_data_plots

# Declaring some constants
number_iterations = 10

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '.-', 'fmt_logn': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Declaring some structures
std_gaussian = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
std_of = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
std_cof = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
std_lognormal = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns

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
        std_gaussian[it, i] = np.std(error_gaussian)
        std_of[it, i] = np.std(error_of)
        std_cof[it, i] = np.std(error_cof)
        std_lognormal[it, i] = np.std(error_lognormal)

    i += 1

# Estimating the error_mean and standard deviation of the standard deviation
mean_std_gaussian = np.mean(std_gaussian, axis=0)
mean_std_of = np.mean(std_of, axis=0)
mean_std_cof = np.mean(std_cof, axis=0)
mean_std_lognormal = np.mean(std_lognormal, axis=0)
std_std_gaussian = np.std(std_gaussian, axis=0)
std_std_of = np.std(std_of, axis=0)
std_std_cof = np.std(std_cof, axis=0)
std_std_lognormal = np.std(std_lognormal, axis=0)

# Estimating the improvements
improvement_gaussian = (1 - np.divide(mean_std_lognormal, mean_std_gaussian)) * 100
improvement_of = (1 - np.divide(mean_std_lognormal, mean_std_of)) * 100
improvement_cof = (1 - np.divide(mean_std_lognormal, mean_std_cof)) * 100

# Ploting standard deviation figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.rcParams['figure.autolayout'] = True
_, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_std_gaussian, yerr=std_std_gaussian, fmt=ap['fmt_gauss'], color=ap['color_gauss'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='MLE Gaussian')
plt.errorbar(occupancies, mean_std_of, yerr=std_std_of, fmt=ap['fmt_of'], color=ap['color_of'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_std_cof, yerr=std_std_cof, fmt=ap['fmt_cof'], color=ap['color_cof'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='COF')
plt.errorbar(occupancies, mean_std_lognormal, yerr=std_std_lognormal, fmt=ap['fmt_logn'], color=ap['color_logn'],
             alpha=alpha_graphs, markersize=10, capsize=5, label='MLE Lognormal')
plt.legend(loc='upper left', fontsize=18)
plt.xlabel('Occupancy (%)', fontsize=16)
plt.ylabel('Std of relative error_absolute (ADC counts)', fontsize=16)
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

# Ploting the figure of improvement of MLE Lognormal when compared to each method
y_limit = [5, 25]
y_axis_arguments = {'plot_step': 5, 'y_plus': 0}
_, ax = plt.subplots(figsize=(10, 6))
plt.plot(occupancies, improvement_gaussian, marker='.', color=ap['color_gauss'], alpha=alpha_graphs, markersize=10,
         label='MLE Gaussian')
plt.plot(occupancies, improvement_of, marker='.', color=ap['color_of'], alpha=alpha_graphs, markersize=10,
         label='OF')
plt.plot(occupancies, improvement_cof, marker='.', color=ap['color_cof'],
         alpha=alpha_graphs, markersize=10, label='COF')
plt.legend(loc='upper right', fontsize=18)
plt.xlabel('Occupancy (%)', fontsize=16)
plt.ylabel('Improvement (%)', fontsize=16)
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
