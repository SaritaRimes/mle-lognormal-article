import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import ks_2samp

from import_data import import_amplitude

occupancy = [10, 30, 50, 80]

ks_distributions = {}

for oc in occupancy:
    # Importing the data
    [amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] = import_amplitude(oc)

    # Creating error_histograms of data
    count_gaussian, bin_gaussian = np.histogram(amplitude_gaussian, bins=100)
    count_of, bin_of = np.histogram(amplitude_of, bins=100)
    count_cof, bin_cof = np.histogram(amplitude_cof, bins=100)
    count_lognormal, bin_lognormal = np.histogram(amplitude_lognormal, bins=100)
    count_true, bin_true = np.histogram(amplitude_true, bins=100)

    # Calculating CDFs
    cdf_gaussian = np.cumsum(count_gaussian / sum(count_gaussian))
    cdf_of = np.cumsum(count_of / sum(count_of))
    cdf_cof = np.cumsum(count_cof / sum(count_cof))
    cdf_lognormal = np.cumsum(count_lognormal / sum(count_lognormal))
    cdf_true = np.cumsum(count_true / sum(count_true))

    # Estimating ks statistic
    ks_distributions[('gaussian', oc)] = ks_2samp(cdf_true, cdf_gaussian).statistic
    ks_distributions[('of', oc)] = ks_2samp(cdf_true, cdf_of).statistic
    ks_distributions[('cof', oc)] = ks_2samp(cdf_true, cdf_cof).statistic
    ks_distributions[('lognormal', oc)] = ks_2samp(cdf_true, cdf_lognormal).statistic

# Plotting the graphs
plt.figure(figsize=(10, 6))
plt.plot(occupancy, [ks_distributions['gaussian', 10], ks_distributions['gaussian', 30],
                     ks_distributions['gaussian', 50], ks_distributions['gaussian', 80]],
         '.--', markersize=15, label='MLE Gaussian')
plt.plot(occupancy, [ks_distributions['of', 10], ks_distributions['of', 30],
                     ks_distributions['of', 50], ks_distributions['of', 80]],
         '.--', markersize=15, label='OF')
plt.plot(occupancy, [ks_distributions['cof', 10], ks_distributions['cof', 30],
                     ks_distributions['cof', 50], ks_distributions['cof', 80]],
         '.--', markersize=15, label='COF')
plt.plot(occupancy, [ks_distributions['lognormal', 10], ks_distributions['lognormal', 30],
                     ks_distributions['lognormal', 50], ks_distributions['lognormal', 80]],
         '.--', markersize=15, label='MLE Lognormal')
plt.legend()

plt.show()

print('Fim')
