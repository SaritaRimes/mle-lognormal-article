import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from import_data import import_amplitude_crossvalidation
from error_mean_mode.error_absolute.data_plots import return_data_plots

# Declaring some constants
number_iterations = 10

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '.-', 'fmt_logn': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Declaring some structures
mean_gauss = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_of = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_cof = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mean_logn = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mode_gauss = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mode_of = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mode_cof = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns
mode_logn = np.zeros([10, 4])  # iterations on the rows, occupancies on the columns

occupancies = [10, 30, 50, 80]
i = 0  # column, which is equivalent to the occupancy
for oc in occupancies:
    print('------------------------------')

    for it in range(10):
        print(f'Occupancy: {oc}%, iteration: {it + 1}')
        # Importing the data
        [amplitude_gauss, amplitude_of, amplitude_cof, amplitude_logn, amplitude_true] \
            = import_amplitude_crossvalidation(oc, it + 1)

        # Calculating the errors
        error_gauss = np.array(amplitude_gauss) - np.array(amplitude_true)
        error_of = np.array(amplitude_of) - np.array(amplitude_true)
        error_cof = np.array(amplitude_cof) - np.array(amplitude_true)
        error_logn = np.array(amplitude_logn) - np.array(amplitude_true)

        # Estimating the error_mean of the errors
        mean_gauss[it, i] = np.mean(error_gauss)
        mean_of[it, i] = np.mean(error_of)
        mean_cof[it, i] = np.mean(error_cof)
        mean_logn[it, i] = np.mean(error_logn)

        # Estimating the error_mean_mode of the errors
        # MLE Gaussian
        hist, bins = np.histogram(error_gauss, bins=100)
        max_hist = np.argmax(hist)
        mode_gauss[it, i] = (bins[max_hist + 1] + bins[max_hist]) / 2
        # OF
        hist, bins = np.histogram(error_of, bins=100)
        max_hist = np.argmax(hist)
        mode_of[it, i] = (bins[max_hist + 1] + bins[max_hist]) / 2
        # COF
        hist, bins = np.histogram(error_cof, bins=100)
        max_hist = np.argmax(hist)
        mode_cof[it, i] = (bins[max_hist + 1] + bins[max_hist]) / 2
        # MLE Lognormal
        hist, bins = np.histogram(error_logn, bins=100)
        max_hist = np.argmax(hist)
        mode_logn[it, i] = (bins[max_hist + 1] + bins[max_hist]) / 2

    i += 1

# Estimating the error_mean and standard deviation of the error_mean
mean_mean_gauss = np.mean(mean_gauss, axis=0)
mean_mean_of = np.mean(mean_of, axis=0)
mean_mean_cof = np.mean(mean_cof, axis=0)
mean_mean_logn = np.mean(mean_logn, axis=0)
std_mean_gauss = np.std(mean_gauss, axis=0)
std_mean_of = np.std(mean_of, axis=0)
std_mean_cof = np.std(mean_cof, axis=0)
std_mean_logn = np.std(mean_logn, axis=0)

# Estimating the error_mean and standard deviation of the error_mean_mode
mean_mode_gauss = np.mean(mode_gauss, axis=0)
mean_mode_of = np.mean(mode_of, axis=0)
mean_mode_cof = np.mean(mode_cof, axis=0)
mean_mode_logn = np.mean(mode_logn, axis=0)
std_mode_gauss = np.std(mode_gauss, axis=0)
std_mode_of = np.std(mode_of, axis=0)
std_mode_cof = np.std(mode_cof, axis=0)
std_mode_logn = np.std(mode_logn, axis=0)

# Ploting error_mean squared error_absolute figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(10, 6))
# Mean
plt.errorbar(occupancies, mean_mean_gauss, yerr=5 * std_mean_gauss, fmt=ap['fmt_gauss'], color=ap['color_gauss'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='MLE Gaussian mean')
plt.errorbar(occupancies, mean_mean_of, yerr=5 * std_mean_of, fmt=ap['fmt_of'], color=ap['color_of'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='OF mean')
plt.errorbar(occupancies, mean_mean_cof, yerr=5 * std_mean_cof, fmt=ap['fmt_cof'], color=ap['color_cof'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='COF mean')
plt.errorbar(occupancies, mean_mean_logn, yerr=5 * std_mean_logn, fmt=ap['fmt_logn'], color=ap['color_logn'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='MLE Lognormal mean')
# Mode
plt.errorbar(occupancies, mean_mode_gauss, yerr=std_mode_gauss, fmt='.--', color=ap['color_gauss'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='MLE Gaussian mode')
plt.errorbar(occupancies, mean_mode_of, yerr=std_mode_of, fmt='.--', color=ap['color_of'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='OF mode')
plt.errorbar(occupancies, mean_mode_cof, yerr=std_mode_cof, fmt='.--', color=ap['color_cof'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='COF mode')
plt.errorbar(occupancies, mean_mode_logn, yerr=std_mode_logn, fmt='.--', color=ap['color_logn'],
             alpha=alpha_graphs, markersize=10, capsize=3, label='MLE Lognormal mode')
plt.legend(loc='best', fontsize=15)
plt.xlabel('Occupancy (%)', fontsize=16)
plt.ylabel('Mean/mode of absolute error (ADC counts)', fontsize=16)
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
