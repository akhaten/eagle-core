import numpy
# import numpy.fft
import scipy.signal
import enum
import typing

import eaglecore.filters.linear


def bilateral(image: numpy.ndarray, sigma_spatial: float, sigma_color: float, size: int) -> numpy.ndarray:
    """Apply Bilateral filter on image.
    
    Let $I$ the image and $I_D$ the filtered image:
    
    \\begin{align}
    w(i, j, k, l) &= e^{-\\frac{(i-k)^2+(j-l)^2}{2\sigma_{spatial}^2} 
    - \\frac{\\lVert I(i,j)-I(k,l) \\rVert^{2}_{2}}{2\sigma_{color}^{2}}} \\\\
    I_{D}(i,j) &= \\frac{\\sum_{k,l} I(k,l) w(i,j,k,l)}{\\sum_{k,l} w(i,j,k,l)}
    \\end{align}

    Args:
        image (numpy.ndarray): image
        sigma_spatial (float): sigma spatial
        sigma_color (float): sigma color
        size (int): size of window/neighbourhood

    Returns:
        Filtered image
    """

    def weight(i: int, j: int, k: int, l: int) -> float:
        expr1: float = ( (i-k)**2 + (j-l) ** 2 ) / ( 2*(sigma_spatial**2) )
        expr2: float = ( (image[i, j]-image[k, l]) ** 2 ) / ( 2*(sigma_color**2) )
        return numpy.exp(-expr1-expr2)

    nb_rows, nb_cols = image.shape
    half_size = size // 2

    image_d = numpy.copy(image)
    
    for i in range(half_size, nb_rows-half_size):
        for j in range(half_size, nb_cols-half_size):
            sum_iw = 0.0
            sum_w = 0.0
            for k in range(i-half_size, i+half_size):
                for l in range(j-half_size, j+half_size):
                    w = weight(i, j, k, l)
                    sum_iw += image[k, l] * w
                    sum_w += w

            image_d[i, j] = sum_iw / sum_w
   
    return image_d


def non_local_mean(image: numpy.ndarray, sigma: float, size: int) -> numpy.ndarray:
    """Apply Non Local Mean (NLM) filter on image.

    Args:
        image (numpy.ndarray): an image
        sigma (float): standard deviation
        size (int): size of window/neighbourhood

    Returns:
        Filtered image
    """
    def weight(i: int, j: int, k: int, l: int) -> float:
        expr: float = ((image[i, j]-image[k, l]) ** 2) / (2*(sigma**2))
        return numpy.exp(-expr)

    nb_rows, nb_cols = image.shape
    half_size = size // 2

    image_d = numpy.copy(image)
    
    for i in range(half_size, nb_rows-half_size):
        for j in range(half_size, nb_cols-half_size):
            sum_iw = 0.0
            sum_w = 0.0
            for k in range(i-half_size, i+half_size):
                for l in range(j-half_size, j+half_size):
                    w = weight(i, j, k, l)
                    sum_iw += image[k, l] * w
                    sum_w += w

            image_d[i, j] = sum_iw / sum_w
   
    return image_d

def anisotropic(image: numpy.ndarray, lamda: float, k: float, nb_iterations: int) -> numpy.ndarray:
    """Apply Anisotropic filter on image.

    Args:
        image (numpy.ndarray): an image
        lamda (float): hyperparameters for gradient ~ ]0, 25]
        k (float): hyperparameters for hot function ~ [0, 20]
        nb_iterations (int): number of iterations ~ 20

    Returns:
        Filtered image
    """

    class Mask(enum.Enum):
        NORTH = list(eaglecore.filters.linear.north())
        SOUTH = list(eaglecore.filters.linear.south())
        WEST  = list(eaglecore.filters.linear.west())
        EST   = list(eaglecore.filters.linear.east())

    c = lambda u : numpy.exp(-(u/k)**2)
    image_n = numpy.copy(image)
    masks = list(Mask)

    for i in range(0, nb_iterations):

        grad = {}
        c_dir = {}
        for mask in masks:
            grad[mask] = scipy.signal.convolve2d(image_n, mask.value, mode = 'same')
            c_dir[mask] = c(grad[mask])

        image_n = image_n + lamda * (
              grad[Mask.NORTH] * c_dir[Mask.NORTH]
            + grad[Mask.EST]   * c_dir[Mask.EST]
            + grad[Mask.WEST]  * c_dir[Mask.WEST]
            + grad[Mask.SOUTH] * c_dir[Mask.SOUTH]
        )

    return image_n


# def mean_geometric(image_fft2: numpy.ndarray, kernel_fft2: numpy.ndarray, k: float, s: float) -> numpy.ndarray:
#     #TODO : TEST
#     e1 = 1 / ( numpy.absolute(kernel_fft2) ** s )
#     e2 = numpy.conj(kernel_fft2) / (numpy.absolute(kernel_fft2)**2 + k)
#     e2 = e2 ** (1-s)
#     e3 = e1 * e2
#     return e3 * image_fft2

def wiener(image: numpy.ndarray, kernel: numpy.ndarray, k: float, use_fft: typing.Optional[bool] = False) -> numpy.ndarray:
    """Apply Wiener filter on image.

    Args:
        image (numpy.ndarray): an image
        kernel (numpy.ndarray): a kernel
        k (float): hyperparameter to avoid divide by zero
        use_fft (typing.Optional[bool], optional): Apply numpy.fft.fftn
            on image and kernel. Defaults to False.

    Returns:
        Filtered image
    """
    
    img = numpy.copy(image)
    ker = numpy.copy(kernel)
    
    if use_fft :
        img = numpy.fft.fftn(img)
        ker = numpy.fft.fftn(ker)
    
    frac = numpy.conj(ker) / (numpy.absolute(ker)**2 + k)
    
    return frac * img

def inverse(image: numpy.ndarray, kernel: numpy.ndarray, use_fft: typing.Optional[bool] = False) -> numpy.ndarray:
    """Apply Inverse filter on image.

    Args:
        image (numpy.ndarray): an image
        kernel (numpy.ndarray): a kernel
        use_fft (typing.Optional[bool], optional): Apply numpy.fft.fftn
            on image and kernel. Defaults to False.

    Returns:
        Filtered image
    """
    
    img = numpy.copy(image)
    ker = numpy.copy(kernel)
    
    if use_fft :
        img = numpy.fft.fftn(img)
        ker = numpy.fft.fftn(ker)
        
    return img / ker


def pseudo_inverse(image: numpy.ndarray, kernel: numpy.ndarray, threshold: float, use_fft: typing.Optional[bool] = False) -> numpy.ndarray:
    """Apply Pseudo-Inverse filter on image.

    Args:
        image (numpy.ndarray): an image
        kernel (numpy.ndarray): a kernel
        threshold (float): threshold to avoid divivide by zero
        use_fft (typing.Optional[bool], optional): Apply numpy.fft.fftn
            on image and kernel. Defaults to False.

    Returns:
        Filtered image
    """
    
    img = numpy.copy(image)
    ker = numpy.copy(kernel)
    
    if use_fft :
        img = numpy.fft.fftn(img)
        ker = numpy.fft.fftn(ker)
        
    return numpy.where(
        threshold <= numpy.absolute(ker), 
        img / ker, 
        img
    )