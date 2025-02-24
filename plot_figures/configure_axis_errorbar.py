import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def configure_x_axis(data_x, data_y, error_bar, original_axis, copy_axis, dist_color, alpha_color, dist_style,
                     label_dist, x_limit, y_limit, x_axis_arguments):
    copy_axis.errorbar(data_x, data_y, yerr=error_bar, color=dist_color, alpha=alpha_color, ls=dist_style,
                       label=label_dist, lw=2, zorder=3)
    plt.xticks(fontsize=17)
    plt.xlim(x_limit)
    plt.ylim(y_limit)
    copy_axis.xaxis.set_ticks_position('bottom')
    mains_quantity = x_axis_arguments['mains_quantity']
    x_plus = x_axis_arguments['x_plus']
    x_minus = x_axis_arguments['x_minus']
    mains = np.linspace(x_limit[0] + x_plus, x_limit[1] - x_minus, mains_quantity)
    if x_plus == x_minus == 0:
        seconds = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity - 1)
        thirds = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity - 9)
    elif x_plus == x_minus:
        seconds = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity + 1)
        thirds = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity + 1)
    elif x_plus == ((x_limit[1] - x_limit[0]) / mains_quantity) \
            or x_minus == ((x_limit[1] - x_limit[0]) / mains_quantity):
        seconds = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity + 1)
        thirds = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity + 1)
    else:
        seconds = np.linspace(x_limit[0], x_limit[1], 2 * mains_quantity)
        thirds = np.linspace(x_limit[0], x_limit[1], 10 * mains_quantity - 4)

    original_axis.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(mains))
    original_axis.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator(seconds))
    copy_axis.xaxis.set_major_locator(matplotlib.ticker.FixedLocator([]))
    copy_axis.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator(thirds))
    copy_axis.tick_params(which="minor", axis='both', length=7)


def configure_y_axis(data_x, data_y, error_bar, original_axis, copy_axis, dist_color, alpha_color, dist_style,
                     label_dist, x_limit, y_limit, y_axis_arguments):
    copy_axis.errorbar(data_x, data_y, yerr=error_bar, color=dist_color, alpha=alpha_color, ls=dist_style,
                       label=label_dist, lw=2, zorder=3)
    plt.yticks(fontsize=17)
    plt.xlim(x_limit)
    plt.ylim(y_limit)
    copy_axis.yaxis.set_ticks_position('left')
    mains_quantity = y_axis_arguments['mains_quantity']
    y_plus = y_axis_arguments['y_plus']
    y_minus = y_axis_arguments['y_minus']
    mains = np.linspace(y_limit[0] + y_plus, y_limit[1] - y_minus, mains_quantity)
    if y_plus == y_minus == 0:
        seconds = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity - 1)
        thirds = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity - 9)
    elif y_plus == y_minus:
        seconds = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity + 1)
        thirds = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity + 1)
    elif y_plus == ((y_limit[1] - y_limit[0]) / mains_quantity) \
            or y_minus == ((y_limit[1] - y_limit[0]) / mains_quantity):
        seconds = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity + 1)
        thirds = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity + 1)
    else:
        seconds = np.linspace(y_limit[0], y_limit[1], 2 * mains_quantity)
        thirds = np.linspace(y_limit[0], y_limit[1], 10 * mains_quantity - 4)

    original_axis.yaxis.set_major_locator(matplotlib.ticker.FixedLocator(mains))
    original_axis.yaxis.set_minor_locator(matplotlib.ticker.FixedLocator(seconds))
    copy_axis.yaxis.set_major_locator(matplotlib.ticker.FixedLocator([]))
    copy_axis.yaxis.set_minor_locator(matplotlib.ticker.FixedLocator(thirds))
    copy_axis.tick_params(which="minor", axis='both', length=7)
