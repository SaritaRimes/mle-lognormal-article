def return_data_plots(occupancy):
    if occupancy == 10:
        x_limit = [0, 250]
        y_limit = [0, 0.18]
        x_axis_arguments = {'plot_step': 25, 'x_plus': 25}
        y_axis_arguments = {'plot_step': 0.03, 'y_plus': 0}
    elif occupancy == 30:
        x_limit = [0, 325]
        y_limit = [0, 0.065]
        x_axis_arguments = {'plot_step': 50, 'x_plus': 50}
        y_axis_arguments = {'plot_step': 0.01, 'y_plus': 0}
    elif occupancy == 50:
        x_limit = [0, 475]
        y_limit = [0, 0.0195]
        x_axis_arguments = {'plot_step': 50, 'x_plus': 50}
        y_axis_arguments = {'plot_step': 0.003, 'y_plus': 0}
    elif occupancy == 80:
        x_limit = [0, 600]
        y_limit = [0, 0.009]
        x_axis_arguments = {'plot_step': 100, 'x_plus': 50}
        y_axis_arguments = {'plot_step': 0.0015, 'y_plus': 0}
    else:
        raise Exception('Enter a valid occupancy.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
