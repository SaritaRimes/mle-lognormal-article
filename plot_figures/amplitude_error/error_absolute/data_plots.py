def return_data_plots(occupancy, method):
    x_limit = [0, 1200]
    x_axis_arguments = {'plot_step': 150, 'x_plus': 0}

    if occupancy == 10:
        if method == 'gaussiano':
            y_limit = [-100, 400]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'of':
            y_limit = [-200, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'cof':
            y_limit = [-150, 450]
            y_axis_arguments = {'plot_step': 75, 'y_plus': 0}
        elif method == 'lognormal':
            y_limit = [-100, 375]
            y_axis_arguments = {'plot_step': 50, 'y_plus': 0}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 30:
        if method == 'gaussiano':
            y_limit = [-150, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 50}
        elif method == 'of':
            y_limit = [-300, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'cof':
            y_limit = [-200, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'lognormal':
            y_limit = [-150, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 50}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 50:
        if method == 'gaussiano':
            y_limit = [-150, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 50}
        elif method == 'of':
            y_limit = [-300, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'cof':
            y_limit = [-200, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'lognormal':
            y_limit = [-200, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 80:
        if method == 'gaussiano':
            y_limit = [-150, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 50}
        elif method == 'of':
            y_limit = [-300, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        elif method == 'cof':
            y_limit = [-150, 550]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 50}
        elif method == 'lognormal':
            y_limit = [-200, 500]
            y_axis_arguments = {'plot_step': 100, 'y_plus': 0}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    else:
        raise Exception('Enter a valid occupancy. The options are: 10, 30, 50 or 80.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
