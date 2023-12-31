import numpy

def power(signal: numpy.ndarray) -> float:
    """Compute power of signal

    Args:
        signal (numpy.ndarray): a signal

    Returns:
        float: power of signal
    """
    return numpy.mean(signal ** 2)
