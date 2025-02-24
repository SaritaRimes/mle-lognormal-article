import numpy as np
from pycps import TextFilePulseShape, PulseGenerator, DatasetGenerator, Random

# set the random engine seed
Random.seed(0)

# read pulse shape
pulse_shape = TextFilePulseShape("../../unipolar-pulse-shape.dat")

# configura o gerador do pulso
phase = 10
pedestal = 50
media_ruido = 50
pulse_generator = PulseGenerator(pulse_shape)
pulse_generator.set_amplitude_distribution(PulseGenerator.EXPONENTIAL_DISTRIBUTION, [1/media_ruido])
pulse_generator.set_phase_distribution(PulseGenerator.UNIFORM_INT_DISTRIBUTION, [-phase, phase])
pulse_generator.set_deformation_level(0.01)
pulse_generator.set_noise_params(0, 0)
pulse_generator.set_pedestal(pedestal)

# configura o gerador do conjunto de dados
occupancy = 0.8
dataset_generator = DatasetGenerator()
dataset_generator.set_pulse_generator(pulse_generator)
dataset_generator.set_occupancy(occupancy)
dataset_generator.set_sampling_rate(25.0)
dataset_generator.set_noise_params(0, 1.5)

# gera um conjunto de dados continuo
n_events = 100000
dataset = dataset_generator.generate_continuous_dataset(n_events)

# gera um conjunto de dados discreto
n_slices = 100000
slice_size = 7
dataset = dataset_generator.generate_sliced_dataset(n_slices, slice_size)

# acessa o tempo, as amostras e as amplitudes gerados
time = np.array(dataset.time)
samples = np.array(dataset.samples)
amplitudes = np.array(dataset.amplitudes)

print('amplitudes: \n' + str(amplitudes))
print('samples: \n' + str(samples))
print('time: \n' + str(time))

# salva os dados em um arquivo txt
with open('ruido_ocup' + str(round(occupancy * 100)) + '.txt', 'wb') as f:
    for line in np.matrix(samples):
        np.savetxt(f, line, fmt='%.7f')
