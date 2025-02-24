def return_data_plots(occupancy, method):
    if occupancy == 10:
        if method == 'gaussiano':
            x_limit = [-112.5, 1200]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_limit = [-112.5, 1200]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 112.5}
        elif method == 'of':
            x_limit = [-187.5, 1200]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_limit = [-187.5, 1200]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 37.5}
        elif method == 'cof':
            x_limit = [-150, 1200]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_limit = [-150, 1200]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 0}
        elif method == 'lognormal':
            x_limit = [-37.5, 1200]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_limit = [-37.5, 1200]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 37.5}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 30:
        if method == 'gaussiano':
            x_limit = [-150, 1237.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_limit = [-150, 1237.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 0}
        elif method == 'of':
            x_limit = [-262.5, 1237.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_limit = [-262.5, 1237.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 112.5}
        elif method == 'cof':
            x_limit = [-187.5, 1237.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_limit = [-187.5, 1237.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 37.5}
        elif method == 'lognormal':
            x_limit = [-37.5, 1237.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_limit = [-37.5, 1237.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 37.5}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 50:
        if method == 'gaussiano':
            x_limit = [-112.5, 1275]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_limit = [-112.5, 1275]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 112.5}
        elif method == 'of':
            x_limit = [-225, 1275]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 75}
            y_limit = [-225, 1275]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 75}
        elif method == 'cof':
            x_limit = [-131.25, 1275]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 131.25}
            y_limit = [-131.25, 1275]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 131.25}
        elif method == 'lognormal':
            x_limit = [-37.5, 1275]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_limit = [-37.5, 1275]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 37.5}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    elif occupancy == 80:
        if method == 'gaussiano':
            x_limit = [-112.5, 1387.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_limit = [-112.5, 1387.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 112.5}
        elif method == 'of':
            x_limit = [-243.75, 1350]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 93.75}
            y_limit = [-243.75, 1350]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 93.75}
        elif method == 'cof':
            x_limit = [-131.25, 1387.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 131.25}
            y_limit = [-131.25, 1387.5]
            y_axis_arguments = {'plot_step': 150, 'y_plus': 131.25}
        elif method == 'lognormal':
            x_limit = [-62.5, 1375]
            x_axis_arguments = {'plot_step': 250, 'x_plus': 62.5}
            y_limit = [-62.5, 1375]
            y_axis_arguments = {'plot_step': 250, 'y_plus': 62.5}
        else:
            raise Exception('Enter a valid method. The options are \'gaussiano\', \'of\', \'cof\' or \'lognormal\'.')
    else:
        raise Exception('Enter a valid occupancy. The options are: 10, 30, 50 or 80.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
