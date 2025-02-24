import matplotlib
import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.colors import Normalize
from scipy.interpolate import interpn

from import_data import import_amplitude_separately_crossvalidation
from amplitude_error.error_absolute.data_plots import return_data_plots

# Declaring some constants
occupancy = 80
iteration = 1
number_iterations = 10
method = 'gaussiano'  # 'gaussiano', 'of', 'cof', 'lognormal'
label = {'gaussiano': 'MLE Gaussian', 'of': 'OF', 'cof': 'COF', 'lognormal': 'MLE Lognormal'}

# Defining plot aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Importing the data
amplitude_estimated = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                           method))
amplitude_true = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                      'verdadeira'))

# Estimating the absolute error
error = amplitude_estimated - amplitude_true

# Ploting the graph
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots(occupancy, method)
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(10, 6))
data, x_e, y_e = np.histogram2d(amplitude_true, error, bins=30, density=True)
# z = interpn((0.3 * (x_e[1:] + x_e[:-1]), 0.3 * (y_e[1:] + y_e[:-1])), data, np.vstack([amplitude_true, error]).T,
#             method='splinef2d', bounds_error=False)
z = interpn((x_e[:-1], y_e[:-1]), data, np.vstack([amplitude_true, error]).T,
            method='splinef2d', bounds_error=False)
# z[np.where(np.isnan(z))] = 0.0
idx = z.argsort()
amplitude_true_sort, error_sort, z_sort = amplitude_true[idx], error[idx], z[idx]
plt.scatter(amplitude_true_sort, error_sort, c=z_sort, alpha=alpha_graphs, s=3, label=method)
norm = Normalize(vmin=np.min(z), vmax=np.max(z))
cbar = fig.colorbar(cm.ScalarMappable(norm=norm), ax=ax)
cbar.ax.set_ylabel('Density', fontsize=13)
cbar.ax.tick_params(labelsize=12)
plt.legend(loc='best', fontsize=18)
plt.title(f'Occupancy: {occupancy}%', fontsize=16)
plt.xlabel('Reference amplitude (ADC counts)', fontsize=16)
plt.ylabel('Absolute error (ADC counts)', fontsize=16)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
plt.xlim(x_limit)
plt.ylim(y_limit)
# x axis
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=8,
               labelsize=17)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
