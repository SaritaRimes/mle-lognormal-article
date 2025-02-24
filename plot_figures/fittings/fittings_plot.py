import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from fitter import Fitter
from matplotlib.colors import to_rgba

from fittings.data_plots import return_data_plots
from import_data import import_noise
from scipy.stats import norm, lognorm

from ks_statistic.fittings_noise.scalar_formatter_custom import ScalarFormatterCustom

# Defining noise occupancy and pile-up error_mean
occupancy = 80
mean_pileup = 50
quantity_signals = 2000000

# Defining plot aspects
color_gauss = 'black'
color_logn = 'black'
color_histogram = 'darkgray'
color_grid = 'gray'
alpha_grid = 0.25
alpha_graphs = 1
legends_factor = 0.85

# Importing noise data
noise = import_noise(occupancy, mean_pileup, quantity_signals)

# Defining the number of bins
bins = np.histogram_bin_edges(noise, bins='fd')
number_bins = len(bins) - 1

# Making de fit with the data
fitting = Fitter(noise, bins=number_bins, distributions=['norm', 'lognorm'])
fitting.fit()
summary = fitting.summary()

# Getting the distributions parameters
parameters_gauss = fitting.fitted_param['norm']
parameters_logn = fitting.fitted_param['lognorm']

# Getting the distributions to plot
pdf_gauss_fitted = norm.pdf(fitting.x, *parameters_gauss)
pdf_logn_fitted = lognorm.pdf(fitting.x, *parameters_logn)

# Plotting the PDFs fitted to data
[x_limit, y_limit, x_axis_arguments, y_axis_arguments] = return_data_plots(occupancy)
plt.rcParams['axes.formatter.use_locale'] = True
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots(figsize=(0.6 * 6, 0.4 * 6))  # inches
plt.hist(noise, bins=fitting.bins, density=True, ec=(to_rgba(color_histogram)), fc=to_rgba(color_histogram, alpha=0.5),
         lw=1.5, histtype='stepfilled', label='Noise', zorder=2)
plt.plot(fitting.x, pdf_gauss_fitted, '-', color=color_gauss, alpha=alpha_graphs, label='Gaussian', lw=2, zorder=3)
plt.plot(fitting.x, pdf_logn_fitted, '--', color=color_logn, alpha=alpha_graphs, label='Log-normal', lw=2, zorder=3)
plt.legend(loc='upper right', fontsize=legends_factor * 10)
plt.xlabel('Sample value (ADC counts)', fontsize=legends_factor * 10)
plt.ylabel('Number of events (%)', fontsize=legends_factor * 10)
plt.grid(color=color_grid, alpha=alpha_grid, zorder=0)
# x axis
plt.xlim(x_limit)
plt.xticks(np.arange(x_limit[0] + x_axis_arguments['x_plus'], x_limit[1] + 0.001, x_axis_arguments['plot_step']))
ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
# y axis
plt.ylim(y_limit)
plt.yticks(np.arange(y_limit[0] + y_axis_arguments['y_plus'], y_limit[1] + 0.001, y_axis_arguments['plot_step']))
ax.yaxis.get_offset_text().set_fontsize(legends_factor * 10)
ax.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator(4))
yfmt = ScalarFormatterCustom()
yfmt.set_powerlimits((0, 0))
ax.yaxis.set_major_formatter(yfmt)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0), useMathText=True)
# x and y axis
ax.tick_params(which='major', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=6.5,
               labelsize=legends_factor * 10)
ax.tick_params(which='minor', direction='in', left=True, right=True, bottom=True, top=True, axis='both', length=4)

plt.savefig(f'D:/Documentos/UERJ/Doutorado/ArtigoIEEE/Figuras/fitting_gauss_logn_mPu{mean_pileup}_ocup{occupancy}.png',
            dpi=600, format='png', pad_inches=0.025, bbox_inches='tight')
plt.show()
