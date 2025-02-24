def return_data_plots(method):
    x_limit = [5, 85]
    x_axis_arguments = {'plot_step': 10, 'x_plus': 5}

    if method == 'sumsquares':
        y_limit = [-0.001, 0.013]
        y_axis_arguments = {'mains_quantity': 7, 'y_plus': 0.001, 'y_minus': 0.001}
    elif method == 'ks_statistic':
        y_limit = [0, 0.325]
        y_axis_arguments = {'plot_step': 0.05, 'y_plus': 0}
    elif method == 'sumsquares+ks_statistic':
        y_limit = [-0.03, 0.33]
        y_axis_arguments = {'mains_quantity': 6, 'y_plus': 0.03, 'y_minus': 0.03}
    else:
        raise Exception('Enter a valid method.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
