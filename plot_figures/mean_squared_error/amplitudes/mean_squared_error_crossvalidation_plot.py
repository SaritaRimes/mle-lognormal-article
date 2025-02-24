import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error

from configure_axis_errorbar import configure_x_axis, configure_y_axis
from import_data import import_amplitude_crossvalidation
from mean_squared_error.amplitudes.data_plots import return_data_plots

# Declaring some constants
number_iterations = 10
occupancies = [10, 30, 50, 80]

# Defining plot aspects
ap = {'color_gauss': 'black', 'color_of': 'grey', 'color_cof': 'black', 'color_logn': 'grey',
      'fmt_gauss': '.-', 'fmt_of': '.-', 'fmt_cof': '^--', 'fmt_logn': '^--'}  # plots aspects
color_grid = 'lightgrey'

# Declaring some structures
mse_gaussian = np.zeros([number_iterations, len(occupancies)])  # iterations on the rows, occupancies on the columns
mse_of = np.zeros([number_iterations, len(occupancies)])  # iterations on the rows, occupancies on the columns
mse_cof = np.zeros([number_iterations, len(occupancies)])  # iterations on the rows, occupancies on the columns
mse_lognormal = np.zeros([number_iterations, len(occupancies)])  # iterations on the rows, occupancies on the columns

i = 0  # column, which is equivalent to the occupancy
for oc in occupancies:
    print('------------------------------')

    for it in range(number_iterations):
        print(f'Occupancy: {oc}%, iteration: {it + 1}')
        # Importing the data
        [amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
            = import_amplitude_crossvalidation(oc, it + 1)

        # Estimating the error_mean squared error_absolute
        mse_gaussian[it, i] = mean_squared_error(amplitude_true, amplitude_gaussian)
        mse_of[it, i] = mean_squared_error(amplitude_true, amplitude_of)
        mse_cof[it, i] = mean_squared_error(amplitude_true, amplitude_cof)
        mse_lognormal[it, i] = mean_squared_error(amplitude_true, amplitude_lognormal)

    i += 1

# Estimating the error_mean and standard deviation of the methods
mean_mse_gaussian = np.mean(mse_gaussian, axis=0)
mean_mse_of = np.mean(mse_of, axis=0)
mean_mse_cof = np.mean(mse_cof, axis=0)
mean_mse_lognormal = np.mean(mse_lognormal, axis=0)
std_mse_gaussian = np.std(mse_gaussian, axis=0)
std_mse_of = np.std(mse_of, axis=0)
std_mse_cof = np.std(mse_cof, axis=0)
std_mse_lognormal = np.std(mse_lognormal, axis=0)

# Ploting error_mean squared error_absolute figure
plt.rcParams['figure.autolayout'] = True
plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.errorbar(occupancies, mean_mse_gaussian, yerr=10 * std_mse_gaussian, fmt=ap['fmt_gauss'], color=ap['color_gauss'],
             markersize=15, label='Gaussian')
plt.errorbar(occupancies, mean_mse_of, yerr=10 * std_mse_of, fmt=ap['fmt_of'], color=ap['color_of'],
             markersize=15, label='OF')
plt.errorbar(occupancies, mean_mse_cof, yerr=10 * std_mse_cof, fmt=ap['fmt_cof'], color=ap['color_cof'],
             markersize=8, label='COF')
plt.errorbar(occupancies, mean_mse_lognormal, yerr=10 * std_mse_lognormal, fmt=ap['fmt_logn'], color=ap['color_logn'],
             markersize=8, label='Lognormal')
plt.legend(loc='lower right', fontsize=19)
plt.xlabel('Occupancy (%)', fontsize=17)
plt.ylabel('Mean Squared Error (ADC counts)', fontsize=17)
plt.grid(color=color_grid, zorder=0)
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots()
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
ax1 = ax.twiny()
configure_x_axis(occupancies, mean_mse_gaussian, 10 * std_mse_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, x_axis_arguments)
# y axis
ax1 = ax.twinx()
configure_y_axis(occupancies, mean_mse_gaussian, 10 * std_mse_gaussian, ax, ax1, ap['color_gauss'], ' ',
                 'Gaussian', x_limit, y_limit, y_axis_arguments)
# x and y axis
ax.tick_params(which="major", axis='both', length=14, labelsize=15)
ax.tick_params(which="minor", axis='both', length=11)

plt.show()
