def return_data_plots_prob(occupancy, method, by_method):
    legend_position = (0.665, 0.78)
    if method == 'mle_gaussiano':
        if occupancy == 10:
            e = 10e-13
            x_limit = [-125, 500]
            y_limit = [-0.29 * e, 3.45 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 0.6 * e, 'y_plus': 0.29 * e}

            if by_method:
                legend_position = (0.33, 0.78)
        elif occupancy == 30:
            e = 10e-15
            x_limit = [-300, 525]
            y_limit = [-0.75 * e, 9 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 1.5 * e, 'y_plus': 0.75 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            e = 10e-15
            x_limit = [-150, 525]
            y_limit = [-0.2 * e, 2.2 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            y_axis_arguments = {'plot_step': 0.4 * e, 'y_plus': 0.2 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            e = 10e-16
            x_limit = [-250, 531.25]
            y_limit = [-0.75 * e, 7.125 * e]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 1.5 * e, 'y_plus': 0.75 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'mle_lognormal':
        if occupancy == 10:
            e = 10e-11
            x_limit = [-200, 375]
            y_limit = [-0.45 * e, 4.95 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.9 * e, 'y_plus': 0.45 * e}

            if by_method:
                legend_position = (0.33, 0.78)
        elif occupancy == 30:
            e = 10e-12
            x_limit = [-300, 562.5]
            y_limit = [-0.15 * e, 1.5 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.3 * e, 'y_plus': 0.15 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            e = 10e-13
            x_limit = [-218.75, 531.25]
            y_limit = [-0.2 * e, 2 * e]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 93.75}
            y_axis_arguments = {'plot_step': 0.4 * e, 'y_plus': 0.2 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            e = 10e-14
            x_limit = [-300, 562.5]
            y_limit = [-0.1 * e, 2.2 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.4 * e, 'y_plus': 0.1 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'mle_lognormalgauss':
        if occupancy == 10:
            e = 10e-13
            x_limit = [-200, 375]
            y_limit = [-0.25 * e, 3 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.5 * e, 'y_plus': 0.25 * e}

            if by_method:
                legend_position = (0.33, 0.78)
        elif occupancy == 30:
            e = 10e-14
            x_limit = [-300, 562.5]
            y_limit = [-0.05 * e, 0.95 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.2 * e, 'y_plus': 0.05 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            e = 10e-15
            x_limit = [-218.75, 531.25]
            y_limit = [-0.125 * e, 2.375 * e]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 93.75}
            y_axis_arguments = {'plot_step': 0.5 * e, 'y_plus': 0.125 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            e = 10e-15
            x_limit = [-300, 562.5]
            y_limit = [-0.05 * e, 0.85 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.2 * e, 'y_plus': 0.05 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'cof':
        if occupancy == 10:
            e = 10e-13
            x_limit = [-150, 375]
            y_limit = [-0.3 * e, 3.15 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            y_axis_arguments = {'plot_step': 0.6 * e, 'y_plus': 0.3 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 30:
            e = 10e-15
            x_limit = [-262.5, 525]
            y_limit = [-0.5 * e, 6 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_axis_arguments = {'plot_step': 1 * e, 'y_plus': 0.5 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            e = 10e-16
            x_limit = [-150, 525]
            y_limit = [-0.75 * e, 8.25 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            y_axis_arguments = {'plot_step': 1.5 * e, 'y_plus': 0.75 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            e = 10e-17
            x_limit = [-218.75, 562.5]
            y_limit = [-0.75 * e, 7.125 * e]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 93.75}
            y_axis_arguments = {'plot_step': 1.5 * e, 'y_plus': 0.75 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'of':
        if occupancy == 10:
            e = 10e-13
            x_limit = [-200, 400]
            y_limit = [-0.3 * e, 3.45 * e]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 0.6 * e, 'y_plus': 0.3 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 30:
            e = 10e-15
            x_limit = [-375, 487.5]
            y_limit = [-1 * e, 9.5 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 75}
            y_axis_arguments = {'plot_step': 2 * e, 'y_plus': 1 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            e = 10e-15
            x_limit = [-262.5, 487.5]
            y_limit = [-0.25 * e, 2.5 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_axis_arguments = {'plot_step': 0.5 * e, 'y_plus': 0.25 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            e = 10e-16
            x_limit = [-337.5, 525]
            y_limit = [-1 * e, 9.5 * e]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_axis_arguments = {'plot_step': 2 * e, 'y_plus': 1 * e}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    else:
        raise Exception('Enter a valid method. The options are: \'mle_gaussiano\', \'mle_lognormal\', \'cof\''
                        'or \'of\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments, legend_position
