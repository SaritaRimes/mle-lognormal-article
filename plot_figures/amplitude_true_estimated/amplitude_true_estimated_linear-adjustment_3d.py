import matplotlib
import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.colors import Normalize
from scipy.interpolate import interpn

from import_data import import_amplitude_separately_crossvalidation
from amplitude_true_estimated.data_plots import return_data_plots

# Declaring some constants
occupancy = 50
index_method = 2
iteration = 1
number_iterations = 10
method = ['gaussiano', 'of', 'cof', 'lognormal']
label = ['MLE Gaussian', 'OF', 'COF', 'MLE Lognormal']

# Defining plot aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8

# Importing the data
amplitude_true = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                      'verdadeira'))
amplitude_estimated = np.array(import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                           method[index_method]))

# Making the linear adjustment
# y = a + b*x
mean_amplitude_true = np.mean(amplitude_true)
mean_amplitude_estimated = np.mean(amplitude_estimated)
b = (np.sum((amplitude_true - mean_amplitude_true) * (amplitude_estimated - mean_amplitude_estimated))
     / np.sum((amplitude_true - mean_amplitude_true) ** 2))
a = mean_amplitude_estimated - b * mean_amplitude_true
amplitude_estimated_leastsquares = a + b * amplitude_true

# Ploting the graph
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots(occupancy, method[index_method])
plt.rcParams['figure.autolayout'] = True
fig, ax = plt.subplots(figsize=(10, 6))
data, x_e, y_e = np.histogram2d(amplitude_true, amplitude_estimated, bins=30, density=True)
z = interpn((x_e[:-1], y_e[:-1]), data, np.vstack([amplitude_true, amplitude_estimated]).T,
            method='splinef2d', bounds_error=False)
z[np.where(np.isnan(z))] = 0.0
idx = z.argsort()
amplitude_true_sort, amplitude_estimated_sort, z_sort = amplitude_true[idx], amplitude_estimated[idx], z[idx]
plt.scatter(amplitude_true_sort, amplitude_estimated_sort, c=z_sort, alpha=alpha_graphs, s=1, label=label[index_method])
norm = Normalize(vmin=np.min(z), vmax=np.max(z))
cbar = fig.colorbar(cm.ScalarMappable(norm=norm), ax=ax)
cbar.ax.set_ylabel('Density', fontsize=13)
cbar.ax.tick_params(labelsize=12)
plt.plot(amplitude_true, amplitude_estimated_leastsquares, color='C3')
plt.legend(loc='best', fontsize=18)
plt.title(f'Occupancy: {occupancy}%', fontsize=16)
plt.xlabel('Reference amplitude (ADC counts)', fontsize=16)
plt.ylabel('Estimated amplitude (ADC counts)', fontsize=16)
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
