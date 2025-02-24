def return_data_plots_chi2(occupancy, method, by_method):
    legend_position = (0.665, 0.78)

    if method == 'mle_gaussiano':
        if occupancy == 10:
            x_limit = [-125, 425]
            y_limit = [-25, 300]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 50, 'y_plus': 25}

            if by_method:
                legend_position = (0.23, 0.78)
        elif occupancy == 30:
            x_limit = [-300, 525]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            x_limit = [-156.25, 525]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 31.25}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            x_limit = [-250, 531.25]
            y_limit = [-37.5, 356.25]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are: \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'mle_lognormal':
        if occupancy == 10:
            x_limit = [-200, 375]
            y_limit = [-25, 287.5]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 50, 'y_plus': 25}

            if by_method:
                legend_position = (0.32, 0.78)
        elif occupancy == 30:
            x_limit = [-300, 562.5]
            y_limit = [-37.5, 318.75]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            x_limit = [-225, 525]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 75}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            x_limit = [-300, 562.5]
            y_limit = [-37.5, 356.25]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are: \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'cof':
        if occupancy == 10:
            x_limit = [-150, 375]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 30:
            x_limit = [-262.5, 525]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 112.5}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            x_limit = [-187.5, 531.25]
            y_limit = [-37.5, 356.25]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 62.5}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            x_limit = [-218.75, 562.5]
            y_limit = [-37.5, 393.75]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 93.75}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are: \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'of':
        if occupancy == 10:
            x_limit = [-187.5, 406.25]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 62.5}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.55}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 30:
            x_limit = [-375, 487.5]
            y_limit = [-37.5, 337.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 75}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            x_limit = [-281.25, 500]
            y_limit = [-37.5, 393.75]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 31.25}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            x_limit = [-337.5, 525]
            y_limit = [-37.5, 412.5]
            x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    elif method == 'all':
        if occupancy == 10:
            x_limit = [-275, 450]
            y_limit = [-25, 262.5]
            x_axis_arguments = {'plot_step': 100, 'x_plus': 75}
            y_axis_arguments = {'plot_step': 50, 'y_plus': 25}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 30:
            x_limit = [-375, 468.75]
            y_limit = [-25, 337.5]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 50, 'y_plus': 25}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 50:
            x_limit = [-375, 562.5]
            y_limit = [-37.5, 393.75]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        elif occupancy == 80:
            x_limit = [-343.75, 531.25]
            y_limit = [-37.5, 412.5]
            x_axis_arguments = {'plot_step': 125, 'x_plus': 93.75}
            y_axis_arguments = {'plot_step': 75, 'y_plus': 37.5}

            if by_method:
                legend_position = (0.665, 0.78)
        else:
            raise Exception('Enter a valid occupancy. The options are \'10\', \'30\', \'50\' or \'80\'.')
    else:
        raise Exception('Enter a valid method. The options are: \'mle_gaussiano\', \'mle_lognormal\', \'cof\','
                        '\'of\' or \'all\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments, legend_position
