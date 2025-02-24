import locale

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.ticker import AutoMinorLocator, ScalarFormatter
from scipy.interpolate import interpn

from data_quality.error_prob.data_plots import return_data_plots_prob
from import_data import (import_error_data_quality_separately_crossvalidation,
                         import_prob_data_quality_separately_crossvalidation)

# locale.setlocale(locale.LC_NUMERIC, locale.getlocale()[0])

# Defining some plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4'}
color_grid = 'gray'
alpha_ec = 1
alpha_fc = 0.15
alpha_grid = 0.25
legends_factor = 0.85

# Defining some constants
occupancy = 50
mean_pileup = 50
iteration = 1
number_iterations = 10
method = 'mle_lognormal'

# Importing the data
error_logn = np.array(import_error_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                           method))
prob_logn = np.array(import_prob_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations,
                                                                         method + 'gauss'))

# Making the interpolation for 3D graph
data, x_e, y_e = np.histogram2d(error_logn, prob_logn, bins=160, density=False)
z = interpn((x_e[:-1], y_e[:-1]), data, np.vstack([error_logn, prob_logn]).T, method='splinef2d',
            bounds_error=False)
z[np.where(np.isnan(z))] = 0.0
idx = z.argsort()
error_logn_sort, prob_logn_sort, z_sort = error_logn[idx], prob_logn[idx], z[idx]

# Plotting the graph
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, _] = return_data_plots_prob(occupancy, method + 'gauss',
                                                                                   False)
fig, ax = plt.subplots(figsize=(0.6 * 6.3228, 0.4 * 6.3228))
norm = LogNorm(vmin=0.1, vmax=np.max(z))
plt.scatter(error_logn_sort, prob_logn_sort, c=z_sort, s=2, zorder=3, norm=norm)
plt.xlabel('Error (ADC counts)', fontsize=legends_factor * 10)
plt.ylabel('Probability', fontsize=legends_factor * 10)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + y_limit[1] * 0.001,
                     y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# colorbar axis
cbar = fig.colorbar(cm.ScalarMappable(norm=norm), ax=ax, format=ScalarFormatter(useMathText=True))
cbar.ax.set_ylabel('Density', fontsize=legends_factor * 10)
cbar.ax.tick_params(labelsize=legends_factor * 10)
cbar.formatter.set_scientific(True)
cbar.formatter.set_powerlimits((0, 0))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)


plt.savefig('D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/erro_prob_logngauss' +
            f'_mpu{mean_pileup}_ocup{occupancy}.png', dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
