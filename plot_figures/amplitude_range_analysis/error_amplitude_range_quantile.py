import numpy as np

from amplitude_range_analysis.error_amplitude_range import relative_error


def mean_std_error_amplitude_range(amplitude_true, amplitude_estimated, number_intervals_amp, error_type):
    # Checking if we have arrays of amplitudes and if the arrays have the same length
    check_arrays_and_length(amplitude_estimated, amplitude_true)

    # Converting the amplitude lists in amplitude arrays
    amplitude_true = np.array(amplitude_true)
    amplitude_estimated = np.array(amplitude_estimated)

    # Creating the error_mean and standard deviation structures
    mean_error = np.zeros(number_intervals_amp)
    std_error = np.zeros(number_intervals_amp)

    # Defining the percentage to divide intervals
    percentage_interval = 1 / number_intervals_amp
    # Estimating the error_mean and standard deviation in the intervals
    i = 0
    amplitude_analysis_min = 0
    for it in range(number_intervals_amp):
        amplitude_analysis_max = np.quantile(amplitude_true, (it + 1) * percentage_interval)

        # Getting the indexes of the amplitudes within the interval
        if amplitude_analysis_min == 0:
            indexes_amplitudes = np.where((amplitude_true >= amplitude_analysis_min)
                                          & (amplitude_true <= amplitude_analysis_max))[0]
        else:
            indexes_amplitudes = np.where((amplitude_true > amplitude_analysis_min)
                                          & (amplitude_true <= amplitude_analysis_max))[0]

        # Calculating the error
        if error_type == 'absolute':
            error = absolute_error(amplitude_estimated[indexes_amplitudes], amplitude_true[indexes_amplitudes])
        elif error_type == 'relative':
            error = relative_error(amplitude_estimated[indexes_amplitudes], amplitude_true[indexes_amplitudes])
        else:
            raise Exception('Enter a valid error type. The options are: \'absolute\' or \'relative\'.')

        # Estimating error_mean and standard deviation of error_absolute within the range
        if np.any(error):
            mean_error[i] = np.mean(error)
            std_error[i] = np.std(error)
        else:
            mean_error[i] = 0
            std_error[i] = 0

        amplitude_analysis_min = amplitude_analysis_max
        i += 1

    return mean_error, std_error


def quantity_signals_amplitude_range(amplitude_true, initial_amplitude_min, initial_amplitude_max):
    # Converting the amplitude lists in amplitude arrays
    amplitude_true = np.array(amplitude_true)

    # Checking how many intervals there will be
    n_intervals = number_intervals(initial_amplitude_min, initial_amplitude_max, 1023)

    # Creating the quantity signals structures
    quantity_signals = np.zeros(n_intervals).astype(int)

    # Defining the initial interval
    amplitude_analysis_min = initial_amplitude_min
    amplitude_analysis_max = initial_amplitude_max
    # Estimating the error_mean and standard deviation in the intervals
    i = 0
    while True:
        # Checking if it is the last interval for adjust the maximum amplitude
        if amplitude_analysis_min < 1023 < amplitude_analysis_max:
            amplitude_analysis_max = max(amplitude_true)

        # Getting the indexes of the amplitudes within the interval
        if amplitude_analysis_min == 0:
            indexes_amplitudes = np.where((amplitude_true >= amplitude_analysis_min)
                                          & (amplitude_true <= amplitude_analysis_max))[0]
        else:
            indexes_amplitudes = np.where((amplitude_true > amplitude_analysis_min)
                                          & (amplitude_true <= amplitude_analysis_max))[0]

        # Calculating the quantity of signals
        quantity_signals[i] = len(amplitude_true[indexes_amplitudes])

        # Checking if it is the last interval for break the looping
        if amplitude_analysis_max == max(amplitude_true):
            break

        # aux = amplitude_analysis_min
        amplitude_analysis_min = amplitude_analysis_max
        # amplitude_analysis_max += 2 * (amplitude_analysis_max - aux)
        amplitude_analysis_max = 2 * amplitude_analysis_max
        i += 1

    return quantity_signals


def absolute_error(estimated_distribution, true_distribution):
    estimated_distribution = np.array(estimated_distribution)
    true_distribution = np.array(true_distribution)

    return estimated_distribution - true_distribution


def number_intervals(initial_amplitude_min, initial_amplitude_max, max_amplitude):
    n_intervals = 0
    min_interval = initial_amplitude_min
    max_interval = initial_amplitude_max
    while True:
        if max_interval < max_amplitude:
            n_intervals += 1
        else:
            n_intervals += 1
            break

        # aux = min_interval
        min_interval = max_interval
        # max_interval += 2 * (max_interval - aux)
        max_interval = 2 * max_interval

    return n_intervals


def define_intervals(amplitude_true, n_intervals):
    intervals = [0]

    percentage_interval = 1 / n_intervals
    for it in range(n_intervals):
        amplitude_analysis_max = np.quantile(amplitude_true, (it + 1) * percentage_interval)

        if amplitude_analysis_max < 1023:
            intervals.append(amplitude_analysis_max)
        else:
            intervals.append(1023)

    return np.array(intervals)


def define_midpoints_intervals(intervals):
    midpoint_intervals = np.zeros(len(intervals) - 1)
    for i in range(len(intervals) - 1):
        midpoint_intervals[i] = (intervals[i] + intervals[i + 1]) / 2

    return midpoint_intervals


def define_size_intervals(intervals):
    size_intervals = np.zeros(len(intervals) - 1)

    for i in range(len(size_intervals)):
        size_intervals[i] = intervals[i + 1] - intervals[i]

    return size_intervals


def check_arrays_and_length(amplitude_estimated, amplitude_true):
    if isinstance(amplitude_true, list) and isinstance(amplitude_estimated, list):
        if (isinstance(amplitude_true[0], list) or isinstance(amplitude_estimated[0], list)) \
             or (len(amplitude_true) <= 1 or len(amplitude_estimated) <= 1):
            raise Exception('The amplitudes variables must be one-dimension lists or arrays.')
    elif isinstance(amplitude_true, np.ndarray) and isinstance(amplitude_estimated, np.ndarray):
        if (amplitude_true.ndim > 1 or amplitude_estimated.ndim > 1) \
             or (len(amplitude_true) <= 1 or len(amplitude_estimated) <= 1):
            raise Exception('The amplitudes variables must be one-dimension lists or arrays.')
    elif isinstance(amplitude_true, list) and isinstance(amplitude_estimated, np.ndarray):
        if (isinstance(amplitude_true[0], list) or amplitude_estimated.ndim > 1) \
             or (len(amplitude_true) <= 1 or len(amplitude_estimated) <= 1):
            raise Exception('The amplitudes variables must be one-dimension lists or arrays.')
    elif isinstance(amplitude_true, np.ndarray) and isinstance(amplitude_estimated, list):
        if (amplitude_true.ndim > 1 or isinstance(amplitude_estimated[0], list)) \
             or (len(amplitude_true) <= 1 or len(amplitude_estimated) <= 1):
            raise Exception('The amplitudes variables must be one-dimension lists or arrays.')
    else:
        raise Exception('The amplitudes variables must be one-dimension lists or arrays.')
