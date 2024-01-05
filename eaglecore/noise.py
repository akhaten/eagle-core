
import numpy
import typing


import eaglecore.signal.measure
import eaglecore.types
import eaglecore.signal.processing

def get_awgn(
    signal_power: float, 
    snr: typing.Union[eaglecore.types.snr, eaglecore.types.snr_db],
    noise_shape: typing.Union[numpy.ndarray, tuple]
) -> tuple[float, numpy.ndarray]:
    """Get additive white gaussian noise (AWGN).

    Args:
        signal_power (float): power of signal
        snr (typing.Union[eaglecore.types.snr, eaglecore.types.snr_db]): Signal Noise Ratio
        noise_shape (typing.Union[numpy.ndarray, tuple]): shape of noise

    Raises:
        TypeError: if snr has bad type

    Returns:
        power of noise and noise
    """

    if isinstance(snr, eaglecore.types.snr_db):
        noise_power = signal_power / snr.to_linear()
    elif isinstance(snr, eaglecore.types.snr):
        noise_power = signal_power / snr
    else:
        raise TypeError('snr must be (eaglecore.types.snr) or (eaglecore.types.snr_db)')

    sigma, mu = numpy.sqrt(noise_power), 0.0
    noise = numpy.random.normal(loc=mu, scale=sigma, size=noise_shape)
    
    return noise_power, noise


def additive_white_gaussian_noise(
    signal: numpy.ndarray, 
    snr: typing.Union[eaglecore.types.snr, eaglecore.types.snr_db]
) -> numpy.ndarray:
    """Add additive white gaussian noise (AWGN).

    Args:
        signal (numpy.ndarray): a signal
        snr (typing.Union[eaglecore.types.snr, eaglecore.types.snr_db]): signal to noise ratio

    Returns:
        Noised signal
        
    Notes:
        - You can use `awgn` alias
        - You could need to normalize your noised image
    """

    # signal_noised = numpy.array(signal, numpy.double)
    signal_double = signal.astype(numpy.double)

    signal_power = eaglecore.signal.measure.power(signal_double)
    
    _, noise = get_awgn(
        signal_power = signal_power,
        snr = snr,
        noise_shape = signal_double.shape
    )
    
    noised_signal = signal_double + noise

    return noised_signal

# if signal.dtype == numpy.complex64:
#     nb_points = len(signal)
#     power_signal = sum(numpy.abs(signal)**2) / len(signal) # puissance de l’image 
#     power_noise = power_signal/(10**(snr/10)) # % puissance du bruit
#     reals = numpy.random.randn(1, nb_points)
#     imags = numpy.random.randn(1, nb_points)
#     noise = [(numpy.sqrt(power_noise) * numpy.sqrt(1/2) * (reals[0][i] + 1j * imags[0][i])) for i in range(0, N)]# bruit Gaussien 
#     return signal + noise

# def multiplicative_noise(signal: numpy.ndarray, snr: float) -> numpy.ndarray:

#     """Multiplicative Noise
    
#     Params:
#         - signal: signal
#         - snr : signal to noise ratio (not in db)

#     Returns:
#         Signal noised
#     """
#     # TODO: TEST

#     signal_power = eaglecore.signal.measure.power(signal)
#     noise_power = signal_power / snr
#     sigma, mu = numpy.sqrt(noise_power), 0.0
#     noise = numpy.random.normal(loc=mu, scale=sigma, size=signal.shape)
#     signal_noised = signal * (1+noise)
#     # grey level image must not have negative value
#     # signal_noised[signal_noised < 0.0] = 0.0
#     return signal_noised


# def pepper_and_selt(signal: numpy.ndarray) -> numpy.ndarray:
#     pass

awgn = additive_white_gaussian_noise



