import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

from data_quality.error_chi2.data_plots import return_data_plots_chi2
from import_data import import_error_data_quality_separately, import_chi2_data_quality_separately

# Defining some plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4'}
color_grid = 'gray'
alpha_graphs = 0.1
alpha_ec = 1
alpha_fc = 0.15
alpha_grid = 0.25

# Defining some constants
occupancy = 80
methods = ['mle_gaussiano', 'mle_lognormal', 'cof', 'of']

# Defining some structures
error = []
chi2 = []

for met in methods:
    # Importing the data
    error_met = import_error_data_quality_separately(occupancy, met)
    chi2_met = import_chi2_data_quality_separately(occupancy, met)

    error.append(error_met)
    chi2.append(chi2_met)

error = np.array(error).transpose()
chi2 = np.array(chi2).transpose()

# Plotting the graph
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots_chi2(occupancy, 'all')
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6.3228, 0.4 * 6.3228))
plt.scatter(error[:, 3], chi2[:, 3], ec=(to_rgba(ap['color_of'], alpha=alpha_ec)),
            fc=(to_rgba(ap['color_of'], alpha=alpha_fc)), label='OF', s=15, zorder=3)
plt.scatter(error[:, 0], chi2[:, 0], ec=(to_rgba(ap['color_gauss'], alpha=alpha_ec)),
            fc=(to_rgba(ap['color_gauss'], alpha=alpha_fc)), label='MLE Gaussiano', s=15, zorder=3)
plt.scatter(error[:, 2], chi2[:, 2], ec=(to_rgba(ap['color_cof'], alpha=alpha_ec)),
            fc=(to_rgba(ap['color_cof'], alpha=alpha_fc)), label='COF', s=15, zorder=3)
plt.scatter(error[:, 1], chi2[:, 1], ec=(to_rgba(ap['color_logn'], alpha=alpha_ec)),
            fc=(to_rgba(ap['color_logn'], alpha=alpha_fc)), label='MLE Lognormal', s=15, zorder=3)
plt.xlabel('Erro (contagens de ADC)', fontsize=0.85 * 12)
plt.ylabel('$\u03C7^2$', fontsize=0.85 * 12)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
# plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=0.85 * 11)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
