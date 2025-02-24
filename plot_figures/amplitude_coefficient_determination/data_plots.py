def return_data_plots(method):
    if method == 'all':
        x_limit = [5, 85]
        x_axis_arguments = {'plot_step': 10, 'x_plus': 5}
        y_limit = [0.325, 1.0375]
        y_axis_arguments = {'plot_step': 0.15, 'y_plus': 0.075}
    else:
        raise Exception('Enter a valid method. The only option is \'all\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
