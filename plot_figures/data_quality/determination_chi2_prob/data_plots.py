def return_data_plots(dq_method, reconstruction_method):
    x_limit = [5, 85]
    x_axis_arguments = {'plot_step': 10, 'x_plus': 5}

    if dq_method == 'chi2':
        if reconstruction_method == 'all':
            y_limit = [-0.002, 0.001]
            y_axis_arguments = {'plot_step': 0.00025, 'y_plus': 0}
        else:
            raise Exception('With the entered DQ method, the only possibility to reconstruction method is \'all\'.')
    elif dq_method == 'probability':
        if reconstruction_method == 'all':
            y_limit = [-0.003, 0.001]  # without absolute value
            y_axis_arguments = {'plot_step': 0.00025, 'y_plus': 0}  # without absolute value
            # y_limit = [-0.45, 0.45]
            # y_axis_arguments = {'plot_step': 0.2, 'y_plus': 0.05}
        else:
            raise Exception('With the entered DQ method, the only possibility to reconstruction method is \'all\'.')
    elif dq_method == 'chi2+probability':
        if reconstruction_method == 'mle_gaussiano':
            y_limit = [-0.2, 0.225]  # without absolute value
            y_axis_arguments = {'plot_step': 0.1, 'y_plus': 0}  # without absolute value
            # y_limit = [-0.025, 0.2625]
            # y_axis_arguments = {'plot_step': 0.05, 'y_plus': 0.025}
        elif reconstruction_method == 'of':
            y_limit = [-0.375, 0.375]  # without absolute value
            y_axis_arguments = {'plot_step': 0.15, 'y_plus': 0.075}  # without absolute value
            # y_limit = [0, 0.525]
            # y_axis_arguments = {'plot_step': 0.1, 'y_plus': 0}
        elif reconstruction_method == 'cof':
            y_limit = [-0.45, 0.2625]  # without absolute value
            y_axis_arguments = {'plot_step': 0.15, 'y_plus': 0}  # without absolute value
            # y_limit = [-0.05, 0.625]
            # y_axis_arguments = {'plot_step': 0.1, 'y_plus': 0.05}
        elif reconstruction_method == 'mle_lognormal':
            y_limit = [-0.09, 0.045]  # without absolute value
            y_axis_arguments = {'plot_step': 0.03, 'y_plus': 0}  # without absolute value
            # y_limit = [0, 0.1275]
            # y_axis_arguments = {'plot_step': 0.03, 'y_plus': 0}
        else:
            raise Exception('Enter a valid reconstruction method. The options are \'mle_gaussiano\', \'of\', \'cof\''
                            'or \'mle_lognormal\'.')
    else:
        raise Exception('Enter a valid method. The options are \'chi2\', \'probability\' or \'chi2+probability\'.')

    return x_limit, y_limit, x_axis_arguments, y_axis_arguments
