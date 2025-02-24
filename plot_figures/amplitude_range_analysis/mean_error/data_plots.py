def return_data_plots(occupancy, plot_type, number_intervals):
    if occupancy == 10:
        if plot_type == 1:
            x_limit = [-50, 1050]
            x_axis_arguments = {'mains_quantity': 11, 'x_plus': 50, 'x_minus': 50}
        elif plot_type == 2:
            x_limit = [0, number_intervals]
            x_axis_arguments = {'mains_quantity': number_intervals, 'x_plus': 0.5, 'x_minus': 0.5}
        else:
            raise Exception('Enter a valid plot type.')

        loc_legend = 'upper left'
        loc_legend_bbox = (0, 0.67)
        y_limit = [-2, 7]
        y_axis_arguments = {'mains_quantity': 10, 'y_plus': 0, 'y_minus': 0}
    elif occupancy == 30:
        if plot_type == 1:
            x_limit = [-50, 1050]
            x_axis_arguments = {'mains_quantity': 11, 'x_plus': 50, 'x_minus': 50}
        elif plot_type == 2:
            x_limit = [0, number_intervals]
            x_axis_arguments = {'mains_quantity': number_intervals, 'x_plus': 0.5, 'x_minus': 0.5}
        else:
            raise Exception('Enter a valid plot type.')

        loc_legend = 'upper left'
        loc_legend_bbox = (0, 0.71)
        y_limit = [-6, 18]
        y_axis_arguments = {'mains_quantity': 7, 'y_plus': 0, 'y_minus': 0}
    elif occupancy == 50:
        if plot_type == 1:
            x_limit = [-50, 1050]
            x_axis_arguments = {'mains_quantity': 11, 'x_plus': 50, 'x_minus': 50}
        elif plot_type == 2:
            x_limit = [0, number_intervals]
            x_axis_arguments = {'mains_quantity': number_intervals, 'x_plus': 0.5, 'x_minus': 0.5}
        else:
            raise Exception('Enter a valid plot type.')

        loc_legend = 'upper left'
        loc_legend_bbox = (0, 0.62)
        y_limit = [-5, 30]
        y_axis_arguments = {'mains_quantity': 8, 'y_plus': 0, 'y_minus': 0}
    elif occupancy == 80:
        if plot_type == 1:
            x_limit = [-50, 1050]
            x_axis_arguments = {'mains_quantity': 11, 'x_plus': 50, 'x_minus': 50}
        elif plot_type == 2:
            x_limit = [0, number_intervals]
            x_axis_arguments = {'mains_quantity': number_intervals, 'x_plus': 0.5, 'x_minus': 0.5}
        else:
            raise Exception('Enter a valid plot type.')

        loc_legend = 'upper left'
        loc_legend_bbox = (0, 0.59)
        y_limit = [-10, 45]
        y_axis_arguments = {'mains_quantity': 12, 'y_plus': 0, 'y_minus': 0}
    else:
        raise Exception('Insira uma ocupação válida.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments, loc_legend, loc_legend_bbox
