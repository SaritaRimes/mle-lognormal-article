import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from sklearn.metrics import r2_score

from data_quality.determination_chi2_prob.data_plots import return_data_plots
from import_data import (import_chi2_data_quality_separately_crossvalidation,
                         import_error_data_quality_separately_crossvalidation,
                         import_prob_data_quality_separately_crossvalidation,
                         import_amplitude_separately_crossvalidation)

# Defining some constants
occupancies = [10, 30, 50, 80]
number_iterations = 10
minimum_amplitude = 0

# Defining plot aspects
ap = {'color_gauss': 'C9', 'color_of': 'C2', 'color_cof': 'C1', 'color_logn': 'C4',
      'fmt_chi2': '.--', 'fmt_prob': '.-'}  # plots aspects
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 0.8
legends_factor = 0.85

# Defining some structures
determination_chi2_gauss = np.zeros([number_iterations, len(occupancies)])
determination_chi2_of = np.zeros([number_iterations, len(occupancies)])
determination_chi2_cof = np.zeros([number_iterations, len(occupancies)])
determination_chi2_logn = np.zeros([number_iterations, len(occupancies)])
determination_prob_gauss = np.zeros([number_iterations, len(occupancies)])
determination_prob_of = np.zeros([number_iterations, len(occupancies)])
determination_prob_cof = np.zeros([number_iterations, len(occupancies)])
determination_prob_logn = np.zeros([number_iterations, len(occupancies)])

# Estimating the coefficient of determination
count_oc = 0
for oc in occupancies:
    for it in range(1, number_iterations + 1):
        print(f'Occupancy {oc}, iteration {it}')

        # Importing the true amplitude
        amplitude_true = np.array(import_amplitude_separately_crossvalidation(oc, it, number_iterations,
                                                                              'verdadeira'))

        # Importing the data of chi2, error and probability
        # Gaussian MLE
        error_gauss = np.array(
            import_error_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                 'mle_gaussiano'))
        chi2_gauss = np.array(
            import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'mle_gaussiano'))
        prob_gauss = np.array(
            import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'mle_gaussiano'))
        # OF
        error_of = np.array(
            import_error_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                 'of'))
        chi2_of = np.array(
            import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'of'))
        prob_of = np.array(
            import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'of'))
        # COF
        error_cof = np.array(
            import_error_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                 'cof'))
        chi2_cof = np.array(
            import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'cof'))
        prob_cof = np.array(
            import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'cof'))
        # Lognormal MLE
        error_logn = np.array(
            import_error_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                 'mle_lognormal'))
        chi2_logn = np.array(
            import_chi2_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'mle_lognormal'))
        prob_logn = np.array(
            import_prob_data_quality_separately_crossvalidation(oc, it, number_iterations,
                                                                'mle_lognormal'))

        # Calculating the relative error
        error_gauss_relative = (np.abs(error_gauss)/amplitude_true) * 100
        error_of_relative = (np.abs(error_of)/amplitude_true) * 100
        error_cof_relative = (np.abs(error_cof)/amplitude_true) * 100
        error_logn_relative = (np.abs(error_logn)/amplitude_true) * 100

        # Estimating and storing the data coefficient of determination
        # chi2
        determination_chi2_gauss[it - 1, count_oc] = r2_score(error_gauss_relative, chi2_gauss)
        determination_chi2_of[it - 1, count_oc] = r2_score(error_of_relative, chi2_of)
        determination_chi2_cof[it - 1, count_oc] = r2_score(error_cof_relative, chi2_cof)
        determination_chi2_logn[it - 1, count_oc] = r2_score(error_logn_relative, chi2_logn)
        # Probability
        determination_prob_gauss[it - 1, count_oc] = r2_score(error_gauss_relative, prob_gauss)
        determination_prob_of[it - 1, count_oc] = r2_score(error_of_relative, prob_of)
        determination_prob_cof[it - 1, count_oc] = r2_score(error_cof_relative, prob_cof)
        determination_prob_logn[it - 1, count_oc] = r2_score(error_logn_relative, prob_logn)

    count_oc += 1

# Calculating mean and standard deviation of the data
mean_determination_chi2 = np.array([np.mean(determination_chi2_gauss, axis=0), np.mean(determination_chi2_of, axis=0),
                                    np.mean(determination_chi2_cof, axis=0), np.mean(determination_chi2_logn, axis=0)])
std_determination_chi2 = np.array([np.std(determination_chi2_gauss, axis=0), np.std(determination_chi2_of, axis=0),
                                   np.std(determination_chi2_cof, axis=0), np.std(determination_chi2_logn, axis=0)])
mean_determination_prob = np.array([np.mean(determination_prob_gauss, axis=0), np.mean(determination_prob_of, axis=0),
                                    np.mean(determination_prob_cof, axis=0), np.mean(determination_prob_logn, axis=0)])
std_determination_prob = np.array([np.std(determination_prob_gauss, axis=0), np.std(determination_prob_of, axis=0),
                                   np.std(determination_prob_cof, axis=0), np.std(determination_prob_logn, axis=0)])

# Plotting chi2 and probability determination figure
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
# chi2
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('chi2', 'all')
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_determination_chi2[0, :], yerr=std_determination_chi2[0, :], fmt=ap['fmt_chi2'],
             color=ap['color_gauss'], alpha=alpha_graphs, markersize=10, capsize=5, label='Gaussian MLE')
plt.errorbar(occupancies, mean_determination_chi2[1, :], yerr=std_determination_chi2[1, :], fmt=ap['fmt_chi2'],
             color=ap['color_of'], alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_determination_chi2[2, :], yerr=std_determination_chi2[2, :], fmt=ap['fmt_chi2'],
             color=ap['color_cof'], alpha=alpha_graphs, markersize=10, capsize=5, label='COF')
plt.errorbar(occupancies, mean_determination_chi2[3, :], yerr=std_determination_chi2[3, :], fmt=ap['fmt_chi2'],
             color=ap['color_logn'], alpha=alpha_graphs, markersize=10, capsize=5, label='Lognormal MLE')
# Aspects
plt.legend(loc='upper right', ncol=1, fontsize=legends_factor * 11)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 12)
plt.ylabel('$\u03C7^2$ determination', fontsize=legends_factor * 12)
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
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

# Probability
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots('probability', 'all')
_, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.errorbar(occupancies, mean_determination_prob[0, :], yerr=std_determination_prob[0, :], fmt=ap['fmt_prob'],
             color=ap['color_gauss'], alpha=alpha_graphs, markersize=10, capsize=5, label='Gaussian MLE')
plt.errorbar(occupancies, mean_determination_prob[1, :], yerr=std_determination_prob[1, :], fmt=ap['fmt_prob'],
             color=ap['color_of'], alpha=alpha_graphs, markersize=10, capsize=5, label='OF')
plt.errorbar(occupancies, mean_determination_prob[2, :], yerr=std_determination_prob[2, :], fmt=ap['fmt_prob'],
             color=ap['color_cof'], alpha=alpha_graphs, markersize=10, capsize=5, label='COF')
plt.errorbar(occupancies, mean_determination_prob[3, :], yerr=std_determination_prob[3, :], fmt=ap['fmt_prob'],
             color=ap['color_logn'], alpha=alpha_graphs, markersize=10, capsize=5, label='Lognormal MLE')
# Aspects
plt.legend(loc='upper right', ncol=1, fontsize=legends_factor * 11)
plt.xlabel('Occupancy (%)', fontsize=legends_factor * 12)
plt.ylabel('Probability determination', fontsize=legends_factor * 12)
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
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 11)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.show()
