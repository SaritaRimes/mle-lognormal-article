import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, ScalarFormatter

from data_quality.error_prob.data_plots import return_data_plots_prob
from import_data import (import_prob_data_quality_separately_crossvalidation,
                         import_error_data_quality_separately_crossvalidation)

# Defining some plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4'}
color_grid = 'gray'
alpha_ec = 1
alpha_fc = 0.15
alpha_grid = 0.25
legends_factor = 0.85

# Defining some constants
occupancy = 50
iteration = 1
number_iterations = 10
method = 'mle_gaussiano'

# Importing the data
error_gauss = import_error_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations, method)
prob_gauss = import_prob_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations, method)

# Plotting the graph
[x_limit, y_limit, x_axis_arguments, y_axis_arguments, _] = return_data_plots_prob(occupancy, method, False)
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6.3228, 0.4 * 6.3228))
plt.scatter(error_gauss, prob_gauss, color=ap['color_gauss'], s=2, zorder=3)
plt.xlabel('Erro (contagens de ADC)', fontsize=legends_factor * 12)
plt.ylabel('Probabilidade', fontsize=legends_factor * 12)
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
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 11)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
