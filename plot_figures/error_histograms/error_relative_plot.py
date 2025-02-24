import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from matplotlib.colors import to_rgba

from amplitude_range_analysis.error_amplitude_range import relative_error
from auxiliary_functions import number_bins
from error_histograms.data_plots import return_parameters
from import_data import import_amplitude_crossvalidation


# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4'}  # plots aspects
color_grid = 'gray'
alpha_ec = 1
alpha_fc = 0.15
alpha_grid = 0.25

# Defining some constants
oc = 80
it = 1

# Importing the data
[amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
    = import_amplitude_crossvalidation(oc, it + 1)

# Calculating the errors
indexes_amplitude_true_10 = np.where(np.array(amplitude_true) > 10)
error_gaussian = relative_error(amplitude_gaussian, amplitude_true)[indexes_amplitude_true_10]
error_of = relative_error(amplitude_of, amplitude_true)[indexes_amplitude_true_10]
error_cof = relative_error(amplitude_cof, amplitude_true)[indexes_amplitude_true_10]
error_lognormal = relative_error(amplitude_lognormal, amplitude_true)[indexes_amplitude_true_10]

# Defining the number of bins for each method
bins = np.histogram_bin_edges(error_lognormal, bins='fd')
width_bins = np.ceil(bins[1] - bins[0])
n_bins_gaussian = number_bins(error_gaussian, width_bins)
n_bins_of = number_bins(error_of, width_bins)
n_bins_cof = number_bins(error_cof, width_bins)
n_bins_lognormal = number_bins(error_lognormal, width_bins)

# Creating the histogram of the errors
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, hist_arguments] = return_parameters(oc, 'relative')
plt.rcParams['figure.autolayout'] = True
# plt.figure(figsize=(10, 6))
fig, ax = plt.subplots(figsize=(10, 6))
plt.hist(error_gaussian, bins=n_bins_gaussian, ec=(to_rgba(ap['color_gauss'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_gauss'], alpha=alpha_fc)), label='MLE Gaussian', **hist_arguments)
plt.hist(error_of, bins=n_bins_of, ec=(to_rgba(ap['color_of'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_of'], alpha=alpha_fc)), label='OF', **hist_arguments)
plt.hist(error_cof, bins=n_bins_cof, ec=(to_rgba(ap['color_cof'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_cof'], alpha=alpha_fc)), label='COF', **hist_arguments)
plt.hist(error_lognormal, bins=n_bins_lognormal, ec=(to_rgba(ap['color_logn'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_logn'], alpha=alpha_fc)), label='MLE Lognormal', **hist_arguments)
plt.legend(loc="upper right", fontsize=17)
plt.title(f'Occupancy: {oc}%', fontsize=17)
plt.xlabel('Error (ADC counts)', fontsize=17)
plt.ylabel('Number of events', fontsize=17)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which="major", direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=8,
               labelsize=17)
ax.tick_params(which="minor", direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
