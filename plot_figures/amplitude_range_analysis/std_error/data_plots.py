def return_data_plots(occupancy, plot_type, number_intervals, evaluation_parameter, error_type):
    if evaluation_parameter == 'standard deviation':
        if error_type == 'absolute':
            loc_legend = 'upper right'

            if plot_type == 1:
                x_limit = [-37.5, 1087.5]
                x_axis_arguments = {'plot_step': 150, 'x_plus': 37.5}
            elif plot_type == 2:
                x_limit = [0, number_intervals]
                x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
            else:
                raise Exception('Enter a valid plot type. The options are: 1 or 2.')

            if occupancy == 10:
                y_limit = [15, 38.75]
                y_axis_arguments = {'plot_step': 5, 'y_plus': 0}
            elif occupancy == 30:
                y_limit = [28, 56.5]
                y_axis_arguments = {'plot_step': 6, 'y_plus': 0}
            elif occupancy == 50:
                y_limit = [36, 67.5]
                y_axis_arguments = {'plot_step': 6, 'y_plus': 0}
            elif occupancy == 80:
                y_limit = [42, 76.5]
                y_axis_arguments = {'plot_step': 6, 'y_plus': 0}
            else:
                raise Exception('Enter a valid occupancy. The options are: 10, 30, 50 or 80.')
        elif error_type == 'relative':
            loc_legend = 'upper right'

            if occupancy == 10:
                if plot_type == 1:
                    x_limit = [-50, 1050]
                    x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
                elif plot_type == 2:
                    x_limit = [0, number_intervals]
                    x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
                else:
                    raise Exception('Enter a valid plot type.')

                y_limit = [0, 170]
                y_axis_arguments = {'plot_step': 20, 'y_plus': 0}
            elif occupancy == 30:
                if plot_type == 1:
                    x_limit = [-50, 1050]
                    x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
                elif plot_type == 2:
                    x_limit = [0, number_intervals]
                    x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
                else:
                    raise Exception('Enter a valid plot type.')

                y_limit = [0, 285]
                y_axis_arguments = {'plot_step': 30, 'y_plus': 0}
            elif occupancy == 50:
                if plot_type == 1:
                    x_limit = [-50, 1050]
                    x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
                elif plot_type == 2:
                    x_limit = [0, number_intervals]
                    x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
                else:
                    raise Exception('Enter a valid plot type.')

                y_limit = [0, 345]
                y_axis_arguments = {'plot_step': 30, 'y_plus': 0}
            elif occupancy == 80:
                if plot_type == 1:
                    x_limit = [-50, 1050]
                    x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
                elif plot_type == 2:
                    x_limit = [0, number_intervals]
                    x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
                else:
                    raise Exception('Enter a valid plot type.')

                y_limit = [0, 400]
                y_axis_arguments = {'plot_step': 50, 'y_plus': 0}
            else:
                raise Exception('Enter a valid occupancy. The options are: 10, 30, 50 or 80.')
        else:
            raise Exception('Enter a valid error type. The options are: \'absolute\' or \'relative\'.')
    elif evaluation_parameter == 'error_mean':
        if occupancy == 10:
            if plot_type == 1:
                x_limit = [-50, 1050]
                x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            elif plot_type == 2:
                x_limit = [0, number_intervals]
                x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
            else:
                raise Exception('Enter a valid plot type.')

            loc_legend = 'upper right'
            loc_legend_bbox = (1, 1)
            y_limit = [-5, 40]
            y_axis_arguments = {'plot_step': 5, 'y_plus': 0}
        elif occupancy == 30:
            if plot_type == 1:
                x_limit = [-50, 1050]
                x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            elif plot_type == 2:
                x_limit = [0, number_intervals]
                x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
            else:
                raise Exception('Enter a valid plot type.')

            loc_legend = 'upper right'
            loc_legend_bbox = (1, 1)
            y_limit = [-10, 105]
            y_axis_arguments = {'plot_step': 20, 'y_plus': 10}
        elif occupancy == 50:
            if plot_type == 1:
                x_limit = [-50, 1050]
                x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            elif plot_type == 2:
                x_limit = [0, number_intervals]
                x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
            else:
                raise Exception('Enter a valid plot type.')

            loc_legend = 'upper right'
            loc_legend_bbox = (1, 1)
            y_limit = [-12.5, 175]
            y_axis_arguments = {'plot_step': 25, 'y_plus': 12.5}
        elif occupancy == 80:
            if plot_type == 1:
                x_limit = [-50, 1050]
                x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            elif plot_type == 2:
                x_limit = [0, number_intervals]
                x_axis_arguments = {'plot_step': 1, 'x_plus': 0.5}
            else:
                raise Exception('Enter a valid plot type.')

            loc_legend = 'upper right'
            loc_legend_bbox = (1, 1)
            y_limit = [-25, 275]
            y_axis_arguments = {'plot_step': 50, 'y_plus': 25}
        else:
            raise Exception('Enter a valid occupancy.')
    else:
        raise Exception('Enter a valid evaluation parameter. The options are \'standard deviation\' or \'error_mean\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments, loc_legend
