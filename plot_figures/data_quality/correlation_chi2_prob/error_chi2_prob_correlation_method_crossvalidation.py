import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from data_quality.correlation_chi2_prob.data_plots import return_data_plots
from import_data import (import_error_data_quality_separately_crossvalidation,
                         import_chi2_data_quality_separately_crossvalidation,
                         import_prob_data_quality_separately_crossvalidation)

# Defining some constants
occupancies = [10, 30, 50, 80]
method = 'mle_lognormal'
number_iterations = 10

# Defining plot aspects
ap = {'mle_gaussiano': 'C9', 'of': 'C2', 'cof': 'C1', 'mle_lognormal': 'C4',
      'fmt_chi2': '.--', 'fmt_prob': '.-'}  # plots aspects
labels = {'mle_gaussiano': 'Gaussian MLE', 'of': 'OF', 'cof': 'COF', 'mle_lognormal': 'Lognormal MLE'}
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Defining some structures
correlation_chi2 = np.zeros([number_iterations, len(occupancies)])
correlation_prob = np.zeros([number_iterations, len(occupancies)])

# Estimating the correlation coefficient
count_oc = 0
for oc in occupancies:
    for it in range(1, number_iterations + 1):
        print(f'Occupancy {oc}, iteration {it}')

        # Importing the data
        error = np.array(import_error_data_quality_separately_crossvalidation(oc, it, number_iterations, method))
        chi2 = np.array(import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations, method))
        prob = np.array(import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations, method))

        # Estimating and storing the data correlation coefficient
        correlation_chi2[it - 1, count_oc] = np.corrcoef(np.abs(error), chi2)[0, 1]
        correlation_prob[it - 1, count_oc] = np.corrcoef(np.abs(error), prob)[0, 1]

    count_oc += 1

# Calculating mean and standard deviation of the data
# mean_correlation_chi2 = np.abs(np.mean(correlation_chi2, axis=0))
mean_correlation_chi2 = np.mean(correlation_chi2, axis=0)
# std_correlation_chi2 = np.abs(np.std(correlation_chi2, axis=0))
std_correlation_chi2 = np.std(correlation_chi2, axis=0)
# mean_correlation_prob = np.abs(np.mean(correlation_prob, axis=0))
mean_correlation_prob = np.mean(correlation_prob, axis=0)
# std_correlation_prob = np.abs(np.std(correlation_prob, axis=0))
std_correlation_prob = np.std(correlation_prob, axis=0)

# Plotting correlation figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('chi2+probability', method)
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_correlation_chi2, yerr=std_correlation_chi2, fmt=ap['fmt_chi2'],
             color=ap[method], alpha=alpha_graphs, markersize=10, capsize=5, label=f'{labels[method]} $\u03C7^2$')
plt.errorbar(occupancies, mean_correlation_prob, yerr=std_correlation_prob, fmt=ap['fmt_prob'],
             color=ap[method], alpha=alpha_graphs, markersize=10, capsize=5, label=f'{labels[method]} probability')
plt.legend(loc='best', ncol=1, fontsize=legends_factor * 11)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 12)
plt.ylabel('Correlation', fontsize=legends_factor * 12)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 11)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.show()
