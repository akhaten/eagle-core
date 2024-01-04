import numpy

def power(signal: numpy.ndarray) -> float:
    """Compute power of signal.

    Args:
        signal (numpy.ndarray): a signal

    Returns:
        Power of signal
    """
    return numpy.mean(signal ** 2)
