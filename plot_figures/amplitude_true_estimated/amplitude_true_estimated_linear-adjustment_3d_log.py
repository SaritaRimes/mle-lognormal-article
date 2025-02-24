import matplotlib
import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.colors import Normalize, LogNorm
from scipy.interpolate import interpn

from import_data import import_amplitude_separately_crossvalidation
from amplitude_true_estimated.data_plots import return_data_plots

# Declaring some constants
occupancy = 80
iteration = 1
number_iterations = 10
method = 'lognormal'
label = {'gaussiano': 'MLE Gaussian', 'of': 'OF', 'cof': 'COF', 'lognormal': 'Lognormal MLE'}

# Defining plot aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Importing the data
amplitude_estimated = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                           method))
amplitude_true = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                      'verdadeira'))

# Making the linear adjustment (y = a + b*x)
mean_amplitude_true = np.mean(amplitude_true)
mean_amplitude_estimated = np.mean(amplitude_estimated)
b = (np.sum((amplitude_true - mean_amplitude_true) * (amplitude_estimated - mean_amplitude_estimated))
     / np.sum((amplitude_true - mean_amplitude_true) ** 2))
a = mean_amplitude_estimated - b * mean_amplitude_true
amplitude_estimated_leastsquares = a + b * amplitude_true

# Plotting the graph
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots(occupancy, method)
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
# Density histogram for frequency of occurrences
data, x_e, y_e = np.histogram2d(amplitude_true, amplitude_estimated, bins=30, density=False)
z = interpn((x_e[:-1], y_e[:-1]), data, np.vstack([amplitude_true, amplitude_estimated]).T,
            method='splinef2d', bounds_error=False)
z[np.where(np.isnan(z))] = 0.0
idx = z.argsort()
amplitude_true_sort, amplitude_estimated_sort, z_sort = amplitude_true[idx], amplitude_estimated[idx], z[idx]
norm = LogNorm(vmin=0.1, vmax=np.max(z))
# Plots
plt.scatter(amplitude_true_sort, amplitude_estimated_sort, c=z_sort, alpha=alpha_graphs, s=1, label=label[method],
            norm=norm)
plt.plot(amplitude_true, amplitude_estimated_leastsquares, color='C3')
cbar = fig.colorbar(cm.ScalarMappable(norm=norm), ax=ax)
# plt.legend(loc='upper left', fontsize=legends_factor * 10)
# plt.title(f'Occupancy: {occupancy}%', fontsize=16)
plt.xlabel('Ref. amplitude (ADC counts)', fontsize=legends_factor * 10)
plt.ylabel('Est. amplitude (ADC counts)', fontsize=legends_factor * 10)
cbar.ax.set_ylabel('Events', fontsize=legends_factor * 10)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
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
# colorbar
cbar.ax.tick_params(which='major', length=6.5, labelsize=legends_factor * 10)
cbar.ax.tick_params(which='minor', length=4)

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/amplitude_verdadeira_estimada_{method}'
            f'_ocup{occupancy}.png', dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
