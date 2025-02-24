import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from sklearn.metrics import r2_score

from amplitude_coefficient_determination.data_plots import return_data_plots
from import_data import import_amplitude_separately_crossvalidation

# Defining some constants
occupancies = [10, 30, 50, 80]
number_iterations = 10

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_chi2': '.--', 'fmt_prob': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Defining some structures
determination_gauss = np.zeros([number_iterations, len(occupancies)])
determination_of = np.zeros([number_iterations, len(occupancies)])
determination_cof = np.zeros([number_iterations, len(occupancies)])
determination_logn = np.zeros([number_iterations, len(occupancies)])

# Estimating the coefficient of determination
count_oc = 0
for oc in occupancies:
    for it in range(1, number_iterations + 1):
        print(f'Occupancy {oc}, iteration {it}')

        # Importing the amplitudes
        amplitude_estimated_gauss = import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                                'gaussiano')
        amplitude_estimated_of = import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                             'of')
        amplitude_estimated_cof = import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                              'cof')
        amplitude_estimated_logn = import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                               'lognormal')
        amplitude_estimated_true = import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                               'verdadeira')

        # Estimating and storing the data coefficient of determination
        determination_gauss[it - 1, count_oc] = r2_score(amplitude_estimated_true, amplitude_estimated_gauss)
        determination_of[it - 1, count_oc] = r2_score(amplitude_estimated_true, amplitude_estimated_of)
        determination_cof[it - 1, count_oc] = r2_score(amplitude_estimated_true, amplitude_estimated_cof)
        determination_logn[it - 1, count_oc] = r2_score(amplitude_estimated_true, amplitude_estimated_logn)

    count_oc += 1

# Calculating mean and standard deviation of the data
mean_determination = np.array([np.mean(determination_gauss, axis=0), np.mean(determination_of, axis=0),
                               np.mean(determination_cof, axis=0), np.mean(determination_logn, axis=0)])
std_determination = np.array([np.std(determination_gauss, axis=0), np.std(determination_of, axis=0),
                              np.std(determination_cof, axis=0), np.std(determination_logn, axis=0)])

# Plotting determination figure
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('all')
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_determination[0, :], yerr=std_determination[0, :], fmt=ap['fmt_chi2'],
             color=ap['color_gauss'], alpha=alpha_graphs, markersize=10, capsize=5, label='Gaussian MLE')
plt.errorbar(occupancies, mean_determination[1, :], yerr=std_determination[1, :], fmt=ap['fmt_chi2'],
             color=ap['color_of'], alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_determination[2, :], yerr=std_determination[2, :], fmt=ap['fmt_chi2'],
             color=ap['color_cof'], alpha=alpha_graphs, markersize=10, capsize=5, label='COF')
plt.errorbar(occupancies, mean_determination[3, :], yerr=std_determination[3, :], fmt=ap['fmt_chi2'],
             color=ap['color_logn'], alpha=alpha_graphs, markersize=10, capsize=5, label='Lognormal MLE')
plt.legend(loc='lower left', ncol=1, fontsize=legends_factor * 11)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 12)
plt.ylabel('Coeff of determination', fontsize=legends_factor * 12)
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
