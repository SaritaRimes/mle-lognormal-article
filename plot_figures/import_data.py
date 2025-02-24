import os


def import_data(path, column_number):
    with open(path) as f:
        lines = f.readlines()
        data = [line.split()[column_number] for line in lines]

    return data


def import_noise(occupancy, mean_pileup, quantity_signals):
    path = (f'{os.path.dirname(__file__)}/../dados_txt/ruido_media{mean_pileup}'
            f'/ruido_ocup{occupancy}_{quantity_signals}sinais.txt')

    noise_txt = import_data(path, 0)

    return [float(noise) for noise in noise_txt]


def import_amplitude(occupancy):
    path = f'{os.path.dirname(__file__)}/../dados_txt/amplitude_gaussiano_ocup{occupancy}.txt'
    amplitude_gaussian_txt = import_data(path, 0)

    path = f'{os.path.dirname(__file__)}/../dados_txt/amplitude_of_ocup{occupancy}.txt'
    amplitude_of_txt = import_data(path, 0)

    path = f'{os.path.dirname(__file__)}/../dados_txt/amplitude_cof_ocup{occupancy}.txt'
    amplitude_cof_txt = import_data(path, 0)

    path = f'{os.path.dirname(__file__)}/../dados_txt/amplitude_lognormal_ocup{occupancy}.txt'
    amplitude_lognormal_txt = import_data(path, 0)

    path = f'{os.path.dirname(__file__)}/../dados_txt/amplitude_verdadeira_ocup{occupancy}.txt'
    amplitude_true_txt = import_data(path, 1)

    return [float(amp) for amp in amplitude_gaussian_txt], [float(amp) for amp in amplitude_of_txt], \
           [float(amp) for amp in amplitude_cof_txt], [float(amp) for amp in amplitude_lognormal_txt], \
           [float(amp) for amp in amplitude_true_txt]


def import_amplitude_crossvalidation(occupancy, iteration):
    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/gaussiano/ocup{occupancy}'
            f'/amplitude_gaussiano_ocup{occupancy}_it{iteration}.txt')
    amplitude_gaussian_txt = import_data(path, 0)

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/of/ocup{occupancy}'
            f'/amplitude_of_ocup{occupancy}_it{iteration}.txt')
    amplitude_of_txt = import_data(path, 0)

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/cof/ocup{occupancy}'
            f'/amplitude_cof_ocup{occupancy}_it{iteration}.txt')
    amplitude_cof_txt = import_data(path, 0)

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/lognormal/ocup{occupancy}'
            f'/amplitude_lognormal_ocup{occupancy}_it{iteration}.txt')
    amplitude_lognormal_txt = import_data(path, 0)

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/verdadeira/ocup{occupancy})'
            f'/amplitude_verdadeira_ocup{occupancy}_it{iteration}.txt')
    amplitude_true_txt = import_data(path, 1)

    return [float(amp) for amp in amplitude_gaussian_txt], [float(amp) for amp in amplitude_of_txt], \
           [float(amp) for amp in amplitude_cof_txt], [float(amp) for amp in amplitude_lognormal_txt], \
           [float(amp) for amp in amplitude_true_txt]


def import_amplitude_separately_crossvalidation(occupancy, iteration, number_iterations, amplitude):
    possible_amplitudes = ['gaussiano', 'lognormal', 'cof', 'of', 'verdadeira']

    if amplitude not in possible_amplitudes:
        raise Exception('Enter a valid amplitude. The options are: \'gaussiano\', \'of\', \'cof\', \'lognormal\' or '
                        '\'verdadeira\'.')

    if iteration not in range(1, number_iterations + 1):
        raise Exception(f'Enter a valid iteration. The options go from 1 to {number_iterations}.')

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/efficiency/{amplitude}/ocup{occupancy}'
            f'/amplitude_{amplitude}_ocup{occupancy}_it{iteration}.txt')

    if amplitude != 'verdadeira':
        amplitude_txt = import_data(path, 0)
    else:
        amplitude_txt = import_data(path, 1)

    return [float(amp) for amp in amplitude_txt]


def import_error_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations, method):
    possible_methods = ['mle_gaussiano', 'mle_lognormal', 'cof', 'of']

    if method not in possible_methods:
        raise Exception('Enter a valid method. The options are: \'mle_gaussiano\', \'mle_lognormal\', \'cof\' '
                        'or \'of\'.')

    if iteration not in range(1, number_iterations + 1):
        raise Exception(f'Enter a valid iteration. The options go from 1 to {number_iterations}.')

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/data_quality/ocup{str(occupancy)}'
            f'/erro_data_quality/erro_{method}_ocup{occupancy}_it{iteration}.txt')
    error_txt = import_data(path, 0)

    return [float(error) for error in error_txt]


def import_chi2_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations, method):
    possible_methods = ['mle_gaussiano', 'mle_lognormal', 'cof', 'of']

    if method not in possible_methods:
        raise Exception('Enter a valid method. The options are: \'mle_gaussiano\', \'mle_lognormal\', \'cof\' '
                        'or \'of\'.')

    if iteration not in range(1, number_iterations + 1):
        raise Exception(f'Enter a valid iteration. The options go from 1 to {number_iterations}.')

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/data_quality/ocup{occupancy}'
            f'/chi2/chi2_{method}_ocup{occupancy}_it{iteration}.txt')
    chi2_txt = import_data(path, 0)

    return [float(chi2) for chi2 in chi2_txt]


def import_prob_data_quality_separately_crossvalidation(occupancy, iteration, number_iterations, method):
    possible_methods = ['mle_gaussiano', 'mle_lognormal', 'mle_lognormalgauss', 'cof', 'of']

    if method not in possible_methods:
        raise Exception('Enter a valid method. The options are: \'mle_gaussiano\', \'mle_lognormal\','
                        '\'mle_lognormalgauss\', \'cof\' or \'of\'')

    if iteration not in range(1, number_iterations + 1):
        raise Exception(f'Enter a valid iteration. The options go from 1 to {number_iterations}.')

    path = (f'{os.path.dirname(__file__)}/../dados_txt/cross_validation/data_quality/ocup{occupancy}'
            f'/probabilidade/prob_{method}_ocup{occupancy}_it{iteration}.txt')
    prob_txt = import_data(path, 0)

    return [float(prob) for prob in prob_txt]
