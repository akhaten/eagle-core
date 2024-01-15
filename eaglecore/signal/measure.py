import numpy
import numpy.typing

def energy(signal: numpy.ndarray) -> float:
    """Compute energy of signal

    Args:
        signal (numpy.ndarray): a signal real or complex

    Returns:
        energy of signal
    """
    
    out = 0.0
    
    if signal.dtype != numpy.complex_:
       out = (signal**2).sum()
    else:
        n = numpy.prod(signal.shape)
        out = (numpy.abs(signal)**2).sum() / n
    
    return out
    
def power(signal: numpy.ndarray) -> float:
    """Compute power of signal.

    Args:
        signal (numpy.ndarray): a signal

    Returns:
        Power of signal
    """
    n = numpy.prod(signal.shape)    
    return energy(signal) / n
