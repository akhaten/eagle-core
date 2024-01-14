import numpy
import typing


def gaussian1d(
    mu: float, 
    sigma: float, 
    x: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """Point Spread Function (PSF) of gaussian 1D.
    
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
    """Point Spread Function (PSF) of gaussian 2D.

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for first axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for second axe

    Returns:
        value(s) of psf for gaussian 2D
    """
    exp = numpy.exp(
        - (x_0 - mu_0)**2 / ( 2*sigma_0**2 )
        - (x_1 - mu_1)**2 / ( 2*sigma_1**2 )
    ) 
    return ( 1 / (2*numpy.pi*sigma_0*sigma_1) ) * exp


def gaussian2d_dx0(
    mu_0: float, sigma_0: float, x_0: typing.Union[float, numpy.ndarray],
    mu_1: float, sigma_1: float, x_1: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """First order derivation of point spread function (PSF) of gaussian 2D
    for first axe.

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for first axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for second axe

    Returns:
        value(s) of psf for gaussian 2D    
    """
    coef = - (x_0 - mu_0) / sigma_0
    g = gaussian2d(mu_0, sigma_0, x_0, mu_1, sigma_1, x_1)
    return coef * g


def gaussian2d_dx1(
    mu_0: float, sigma_0: float, x_0: typing.Union[float, numpy.ndarray],
    mu_1: float, sigma_1: float, x_1: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """First order derivation of point spread function (PSF) of gaussian 2D
    for second axe.

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for first axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for second axe

    Returns:
        value(s) of psf for gaussian 2D
    """
    coef = - (x_1 - mu_1) / sigma_1
    g = gaussian2d(mu_0, sigma_0, x_0, mu_1, sigma_1, x_1)
    return coef * g


def gaussian2d_d2x0(
    mu_0: float, sigma_0: float, x_0: typing.Union[float, numpy.ndarray],
    mu_1: float, sigma_1: float, x_1: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """Second order derivation of point spread function (PSF) of gaussian 2D
    for first axe.

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for first axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for second axe

    Returns:
        value(s) of psf for gaussian 2D
    """
    coef = ( (x_0 - mu_0) / sigma_0 )**2 - 1 / sigma_0
    g = gaussian2d(mu_0, sigma_0, x_0, mu_1, sigma_1, x_1)
    return coef * g


def gaussian2d_d2x1(
    mu_0: float, sigma_0: float, x_0: typing.Union[float, numpy.ndarray],
    mu_1: float, sigma_1: float, x_1: typing.Union[float, numpy.ndarray]
) -> typing.Union[float, numpy.ndarray]:
    """Second order derivation of point spread function (PSF) of gaussian 2D
    for second axe.

    Args:
        mu_0 (float): mean of first axe
        sigma_0 (float): standard deviation of first axe
        x_0 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for first axe
        mu_1 (float): mean of second axe
        sigma_1 (float): standard deviation of second axe
        x_1 (typing.Union[float, numpy.ndarray]): value to evaluate psf 
            for second axe

    Returns:
        value(s) of psf for gaussian 2D
    """
    coef =  ( (x_1 - mu_1) / sigma_1 )**2 - 1 / sigma_1
    g = gaussian2d(mu_0, sigma_0, x_0, mu_1, sigma_1, x_1)
    return coef * g