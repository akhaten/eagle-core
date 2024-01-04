import numpy
import typing

def gaussian1d(
    mu: float, 
    sigma: float, 
    x: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """Point Spread Function (PSF) of gaussian 1D

    Args:
        mu (float): mean
        sigma (float): standard deviation
        x (typing.Union[float, numpy.ndarray]): value tu evaluate psf

    Returns:
        value(s) of psf for gaussian 1D
    """
    exp = numpy.exp( - (x - mu)**2 / ( 2*sigma**2 ) ) 
    return ( 1 / ( numpy.sqrt(2*numpy.pi) * sigma ) ) * exp


def gaussian2d(
    mu_0: float, sigma_0: float, x_0: typing.Union[float, numpy.ndarray],
    mu_1: float, sigma_1: float, x_1: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """Point Spread Function (PSF) of gaussian 2D

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for fist axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for fist axe

    Returns:
        value(s) of psf for gaussian 2D
    """
    exp = numpy.exp(
        - (x_0 - mu_0)**2 / ( 2*sigma_0**2 )
        - (x_1 - mu_1)**2 / ( 2*sigma_1**2 )
    ) 
    return ( 1 / (2*numpy.pi*sigma_0*sigma_1) ) * exp


