"""
# Description
Linear filters are filters that can used in dicrete convolution
with some function like 
[scipy.signal.convolve2d](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html) 
"""

import numpy
import eaglecore.psf


def gaussian_filter2D(
    mu_0: float, sigma_0: float, size_0: int,
    mu_1: float, sigma_1: float, size_1: int
) -> numpy.ndarray:
    """Get a gaussian filter 2D

    Args:
        mu_0 (float): Mean of axe 0
        sigma_0 (float): Variance of axe 0
        size_0 (int): Size of axe 0
        mu_1 (float): Mean of axe 1
        sigma_1 (float): Variance of axe 1
        size_1 (int): Size of axe 1

    Returns:
        Gaussian filter 2D with size/shape of (size_0, size_1) 
    """
    axe0_values = numpy.arange(
        start = -size_0//2 + 1, 
        stop = size_0//2 + 1, 
        step = 1
    )
    
    axe1_values = numpy.arange(
        start = -size_1//2 + 1, 
        stop = size_1//2 + 1, 
        step = 1
    )
    
    x_0, x_1 = numpy.meshgrid(*[ axe0_values, axe1_values ])
    
    filter = eaglecore.psf.gaussian2d(
        mu_0 = mu_0, sigma_0 = sigma_0, x_0 = x_0,
        mu_1 = mu_1, sigma_1 = sigma_1, x_1 = x_1 
    )

    return filter

def north() -> numpy.ndarray:
    """Get North filter

    Returns:
        North filter
    """
    return numpy.array(
        [
            [0, 1, 0], 
            [0, -1, 0], 
            [0, 0, 0]
        ]
    )

def south() -> numpy.ndarray:
    """Get South filter

    Returns:
        South filter
    """
    return numpy.array(
        [
            [0, 0, 0], 
            [0, -1, 0], 
            [0, 1, 0]
        ]
    )

def west() -> numpy.ndarray:
    """Get West filter

    Returns:
        West filter
    """
    return numpy.array(
        [
            [0, 0, 0], 
            [1, -1, 0], 
            [0, 0, 0]
        ]
    )

def est() -> numpy.ndarray:
    """Get Est filter

    Returns:
        Est filter
    """
    return numpy.array(
        [
            [0, 0, 0], 
            [0, -1, 1], 
            [0, 0, 0]
        ]
    )

def laplacian() -> numpy.ndarray:
    """Get Laplacian filter
    
    Returns:
        numpy.ndarray: Laplacian filter
    """
    return numpy.array(
        [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ]
    )

def mean_filter(size: numpy.ndarray | tuple) -> numpy.ndarray:
    """Get Mean filter

    Args:
        size (numpy.ndarray | tuple): Size of filter

    Returns:
        numpy.ndarray: Mean filter
    """
    filter = numpy.ones(size=size)
    filter /= size*size
    return filter


# def roberts_masks() -> numpy.ndarray:
#     #TODO : TEST
 
#     return numpy.array(
#         [
#             numpy.array([[-1, 0], [0, 1]]),
#             numpy.array([[0, -1], [1, 0]])
#         ]
#     )


# def sobel_masks() -> numpy.ndarray:
#     #TODO : TEST
 
#     return numpy.array(
#         [
#             numpy.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
#             numpy.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
#         ]
#     )


# def kirsh_masks() -> numpy.ndarray:
#     #TODO
#     # return numpy.ndarray(
#     #     [
#     #         numpy.ndarray([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
#     #         numpy.ndarray([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
#     #     ]
#     # )
#     pass


# def robinson_masks() -> numpy.ndarray:
#     #TODO
#     # return numpy.ndarray(
#     #     [
#     #         numpy.ndarray([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
#     #         numpy.ndarray([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
#     #     ]
#     # )
#     pass
