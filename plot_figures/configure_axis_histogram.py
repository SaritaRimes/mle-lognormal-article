import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def configure_x_axis(data, n_bins, axis_original, axis_copy, x_limit, y_limit, hist_arguments, mains_quantity, x_plus,
                     x_minus):
    axis_copy.hist(data, bins=n_bins, color='white', label="MLE Gaussian", **hist_arguments)
    plt.xlim(x_limit)
    plt.ylim(y_limit)
    axis_copy.xaxis.set_ticks_position("bottom")
    mains_quantity = mains_quantity
    principais = np.linspace(x_limit[0] + x_plus, x_limit[1] - x_minus, mains_quantity)
    if x_minus == x_plus == 0:
        segundos = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity - 1)
        terceiros = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity - 9)
    elif x_minus == x_plus:
        segundos = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity + 1)
        terceiros = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity + 1)
    elif x_plus == ((x_limit[1] - x_limit[0]) / mains_quantity) \
            or x_minus == ((x_limit[1] - x_limit[0]) / mains_quantity):
        segundos = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity + 1)
        terceiros = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity + 1)
    else:
        segundos = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity)
        terceiros = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity - 4)

    axis_original.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(principais))
    axis_original.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator(segundos))
    axis_copy.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([]))
    axis_copy.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator(terceiros))
    axis_copy.tick_params(which="minor", axis='both', length=5)


def configure_y_axis(data, n_bins, axis_original, axis_copy, x_limit, y_limit, hist_arguments, mains_quantity, y_minus):
    axis_copy.hist(data, bins=n_bins, color='white', label="MLE Gaussiano", **hist_arguments)
    plt.xlim(x_limit)
    plt.ylim(y_limit)
    axis_copy.yaxis.set_ticks_position("left")
    mains_quantity = mains_quantity
    principais = np.linspace(y_limit[0], y_limit[1] - y_minus, mains_quantity)
    if y_minus == 0:
        segundos = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity - 1)
        terceiros = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity - 9)
    else:
        segundos = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity)
        terceiros = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity - 4)

    axis_original.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(principais))
    axis_original.yaxis.set_minor_locator(matplotlib.ticker.FixedLocator(segundos))
    axis_copy.yaxis.set_major_locator(matplotlib.ticker.FixedLocator([]))
    axis_copy.yaxis.set_minor_locator(matplotlib.ticker.FixedLocator(terceiros))
    axis_copy.tick_params(which="minor", axis='both', length=5)
