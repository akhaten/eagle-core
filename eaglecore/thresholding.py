import numpy
import numpy.linalg


def soft(x: numpy.ndarray, threshold: float) -> numpy.ndarray:
    """Compute soft-thresolding.

    Args:
        x (numpy.ndarray): a data
        threshold (float): threshold

    Returns:
        thresholded data
    """
    # sign(x) * max(|x| - threshold, 0)
    expr = numpy.abs(x) - threshold
    return numpy.sign(x) * numpy.where(0 < expr, expr, 0)


def multidimensional_soft(x: numpy.ndarray, threshold: float) -> numpy.ndarray:
    """Compute generalization of soft-thresholding  for 
        multidimensional array by using generalization of sign function.

    Args:
        x (numpy.ndarray): a data
        threshold (float): threshold

    Returns:
        thresholded data
    """
    
    s = numpy.sqrt(numpy.sum(x**2, axis=0))
    ss = numpy.where(s > threshold, (s-threshold)/s, 0)
    output = numpy.array([ss*x[i] for i in range(0, x.shape[0])])
    
    return output


def singular_value(x: numpy.ndarray, threshold: float) -> numpy.ndarray:
    """Compute singular value thresholding (SVT).

    Args:
        x (numpy.ndarray): a data
        threshold (float): threshold

    Returns:
        thresholded data
    """
    
    # Decomposition
    u, s, vh = numpy.linalg.svd(x)
    # Thresholding
    singular_value_max = numpy.max(s)
    s[s < threshold*singular_value_max] = 0.0
    # Reconstruction
    res = numpy.dot(u * s, vh)
    return res


def singular_value_soft(x: numpy.ndarray, threshold: float) -> numpy.ndarray:
    """Compute singular value soft thresholding.
    
    Args:
        x (numpy.ndarray): a data
        threshold (float): threshold

    Returns:
        thresholded data
    """
   
    # Decomposition
    u, s, vh = numpy.linalg.svd(x)
    # Thresholding with 
    # singular_value_max = numpy.max(s)
    s_diag = numpy.diag(s)
    s_diag = soft(s_diag, threshold)
    s = numpy.diag(s_diag)
    # Reconstruction
    res = numpy.dot(u * s, vh)
    return res