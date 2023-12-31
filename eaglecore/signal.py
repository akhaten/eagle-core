import numpy

def power(signal: numpy.ndarray) -> float:
    """Power of signal
    """
    # nb_value = numpy.prod(numpy.array(signal.shape))
    # sum = numpy.sum(numpy.power(signal, 2))
    # return sum / nb_value
    return numpy.mean(numpy.power(signal, 2))

# def power_noise(power_signal: float, snr: float) -> float:
#     return power_signal / ( 10 ** (snr/10) )
