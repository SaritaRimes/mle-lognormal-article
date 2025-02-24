import matplotlib.pyplot as plt
import numpy as np
from scipy.special import kl_div, rel_entr

from import_data import import_amplitude


# Defining some constants
occupancy = 10

# Importing the data
[amplitude_gaussian, amplitude_of, amplitude_cof, amplitude_lognormal, amplitude_true] = import_amplitude(occupancy)

# Making the error_histograms
count_gaussian, bins_gaussian = np.histogram(amplitude_gaussian, bins=100)
count_of, bins_of = np.histogram(amplitude_of, bins=100)
count_cof, bins_cof = np.histogram(amplitude_cof, bins=100)
count_lognormal, bins_lognormal = np.histogram(amplitude_lognormal, bins=100)
count_true, bins_true = np.histogram(amplitude_true, bins=100)

# Calculating de CDFs
cdf_gaussian = np.cumsum(count_gaussian / sum(count_gaussian))
cdf_of = np.cumsum(count_of / sum(count_of))
cdf_cof = np.cumsum(count_cof / sum(count_cof))
cdf_lognormal = np.cumsum(count_lognormal / sum(count_lognormal))
cdf_true = np.cumsum(count_true / sum(count_true))

# Estimating KL Divergence
kl_divergence_gaussian = sum(rel_entr(cdf_true, cdf_gaussian))
kl_divergence_of = sum(rel_entr(cdf_true, cdf_of))
kl_divergence_cof = sum(rel_entr(cdf_true, cdf_cof))
kl_divergence_lognormal = sum(rel_entr(cdf_true, cdf_lognormal))

plt.show()
