def return_parameters(occupancy, error_type):
    if error_type == 'absolute':
        if occupancy == 10:
            x_limit = [-70, 80]
            y_limit = [0, 17000]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 20, 'x_plus': 10}
            y_axis_arguments = {'plot_step': 2000}
        elif occupancy == 30:
            x_limit = [-175, 200]
            y_limit = [0, 6400]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 50, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 800}
        elif occupancy == 50:
            x_limit = [-225, 275]
            y_limit = [0, 5600]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 50, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 800}
        elif occupancy == 80:
            x_limit = [-262.5, 337.5]
            y_limit = [0, 4800]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 75, 'x_plus': 37.5}
            y_axis_arguments = {'plot_step': 800}
        else:
            raise Exception('Insira uma ocupação válida.')
    elif error_type == 'relative':
        if occupancy == 10:
            x_limit = [-60, 67.5]
            y_limit = [0, 15000]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 15, 'x_plus': 0}
            y_axis_arguments = {'plot_step': 2000}
        elif occupancy == 30:
            x_limit = [-175, 200]
            y_limit = [0, 11500]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 50, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 1000}
        elif occupancy == 50:
            x_limit = [-275, 375]
            y_limit = [0, 7600]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 50, 'x_plus': 25}
            y_axis_arguments = {'plot_step': 800}
        elif occupancy == 80:
            x_limit = [-450, 700]
            y_limit = [0, 5500]
            hist_arguments = {'histtype': 'stepfilled', 'lw': 1.5, 'ls': '-', 'zorder': 3}
            x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
            y_axis_arguments = {'plot_step': 500}
        else:
            raise Exception('Enter a valid occupancy.')
    else:
        raise Exception('Enter a valid type of error_absolute. The options are \'absolute\' or \'relative\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments, hist_arguments
