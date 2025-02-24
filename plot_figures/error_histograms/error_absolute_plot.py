# Defining plot aspects
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from matplotlib.colors import to_rgba

from auxiliary_functions import number_bins
from error_histograms.data_plots import return_parameters
from import_data import import_amplitude_crossvalidation

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4'}  # plots aspects
color_grid = 'gray'
alpha_ec = 1
alpha_fc = 0.15
alpha_grid = 0.25
legends_factor = 0.85

# Defining some constants
occupancy = 80
mean_pileup = 50
it = 1

# Importing the data
[amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] \
    = import_amplitude_crossvalidation(occupancy, it + 1)

# Calculating the errors
error_gaussian = np.array(amplitude_gaussian) - np.array(amplitude_true)
error_of = np.array(amplitude_of) - np.array(amplitude_true)
error_cof = np.array(amplitude_cof) - np.array(amplitude_true)
error_lognormal = np.array(amplitude_lognormal) - np.array(amplitude_true)

# Defining the number of bins for each method
bins = np.histogram_bin_edges(error_lognormal, bins='fd')
width_bins = np.ceil(bins[1] - bins[0])
n_bins_gaussian = number_bins(error_gaussian, width_bins)
n_bins_of = number_bins(error_of, width_bins)
n_bins_cof = number_bins(error_cof, width_bins)
n_bins_lognormal = number_bins(error_lognormal, width_bins)

# Creating the histogram of the errors
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, hist_arguments] = return_parameters(occupancy, 'absolute')
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.hist(error_gaussian, bins=n_bins_gaussian, ec=(to_rgba(ap['color_gauss'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_gauss'], alpha=alpha_fc)), label='MLE Gaussian', **hist_arguments)
plt.hist(error_of, bins=n_bins_of, ec=(to_rgba(ap['color_of'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_of'], alpha=alpha_fc)), label='OF', **hist_arguments)
plt.hist(error_cof, bins=n_bins_cof, ec=(to_rgba(ap['color_cof'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_cof'], alpha=alpha_fc)), label='MAE', **hist_arguments)
plt.hist(error_lognormal, bins=n_bins_lognormal, ec=(to_rgba(ap['color_logn'], alpha=alpha_ec)),
         fc=(to_rgba(ap['color_logn'], alpha=alpha_fc)), label='MLE Log-normal', **hist_arguments)
plt.legend(loc="upper right", fontsize=legends_factor * 9.7)
# plt.title(f'Occupancy: {oc}%', fontsize=16)
plt.xlabel('Error (ADC counts)', fontsize=legends_factor * 10)
plt.ylabel('Number of events', fontsize=legends_factor * 10)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']),
           fontsize=legends_factor * 10)
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0], y_limit[1] + 0.001, y_axis_arguments['plot_step']), fontsize=legends_factor * 10)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
ax.yaxis.get_offset_text().set_fontsize(legends_factor * 10)
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which="major", direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which="minor", direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/histogram_error_mPu{mean_pileup}_ocup{occupancy}.png',
            dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
