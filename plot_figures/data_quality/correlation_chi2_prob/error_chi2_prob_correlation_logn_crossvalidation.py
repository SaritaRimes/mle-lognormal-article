import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from data_quality.correlation_chi2_prob.data_plots import return_data_plots
from import_data import (import_error_data_quality_separately_crossvalidation,
                         import_chi2_data_quality_separately_crossvalidation,
                         import_prob_data_quality_separately_crossvalidation)

# Defining some constants
occupancies = [10, 30, 50, 80]
number_iterations = 10

# Defining plot aspects
ap = {'mle_lognormal': 'C4', 'mle_lognormalgauss': 'C3', 'fmt_chi2': '.--', 'fmt_prob': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Defining some structures
correlation_chi2 = np.zeros([number_iterations, len(occupancies)])
correlation_prob_logn = np.zeros([number_iterations, len(occupancies)])
correlation_prob_logngauss = np.zeros([number_iterations, len(occupancies)])

# Estimating the correlation coefficient
count_oc = 0
for oc in occupancies:
    for it in range(1, number_iterations + 1):
        print(f'Occupancy {oc}, iteration {it}')

        # Importing the error data
        error_logn = np.array(import_error_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                                   'mle_lognormal'))
        chi2_logn = np.array(import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                                 'mle_lognormal'))
        prob_logn = np.array(import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                                 'mle_lognormal'))
        prob_logngauss = np.array(import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                                      'mle_lognormalgauss'))

        # Estimating and storing the data correlation coefficient
        correlation_chi2[it - 1, count_oc] = np.corrcoef(error_logn, chi2_logn)[0, 1]
        correlation_prob_logn[it - 1, count_oc] = np.corrcoef(error_logn, prob_logn)[0, 1]
        correlation_prob_logngauss[it - 1, count_oc] = np.corrcoef(error_logn, prob_logngauss)[0, 1]

    count_oc += 1

# Calculating mean and standard deviation of the data
mean_correlation_chi2 = np.mean(correlation_chi2, axis=0)
std_correlation_chi2 = np.std(correlation_chi2, axis=0)
mean_correlation_prob_logn = np.mean(correlation_prob_logn, axis=0)
std_correlation_prob_logn = np.std(correlation_prob_logn, axis=0)
mean_correlation_prob_logngauss = np.mean(correlation_prob_logngauss, axis=0)
std_correlation_prob_logngauss = np.std(correlation_prob_logngauss, axis=0)

# Plotting correlation figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('chi2+probability',
                                                                           'mle_lognormal')
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_correlation_chi2, yerr=std_correlation_chi2, fmt=ap['fmt_chi2'],
             color=ap['mle_lognormal'], alpha=alpha_graphs, markersize=10, capsize=5, label='Logn MLE $\u03C7^2$')
plt.errorbar(occupancies, mean_correlation_prob_logn, yerr=std_correlation_prob_logn, fmt=ap['fmt_prob'],
             color=ap['mle_lognormal'], alpha=alpha_graphs, markersize=10, capsize=5,
             label='Logn MLE prob (Logn)')
plt.errorbar(occupancies, mean_correlation_prob_logngauss, yerr=std_correlation_prob_logngauss, fmt=ap['fmt_prob'],
             color=ap['mle_lognormalgauss'], alpha=alpha_graphs, markersize=10, capsize=5,
             label='Logn MLE prob (Gauss)')
plt.legend(loc='upper right', ncol=1, fontsize=legends_factor * 10)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 10)
plt.ylabel('Correlation', fontsize=legends_factor * 10)
plt.grid(True, color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
ax.yaxis.get_offset_text().set_fontsize(legends_factor * 10)
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

# plt.savefig('D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/correlation_logn.png', dpi=600, format='png',
#             pad_inches=0.025, bbox_inches='tight')
plt.show()
