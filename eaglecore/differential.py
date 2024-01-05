

import numpy

def difference_finite_circular(array: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Compute directional gradient with circular boundary condition.
    
    Args:
        array (numpy.ndarray): element for derivation
        axis (int): direction of gradient

    Returns:
        derivative of array
        
    Notes: 
        - You can use the `dfc` alias
    """
    prepend = numpy.expand_dims(
        array.take(indices=-1, axis=axis),
        axis=axis
    )
    

    d_axis = numpy.diff(
        array,
        axis = axis,
        prepend=prepend
    )

    return d_axis


def transposed_difference_finite_circular(array: numpy.ndarray, axis: int) -> numpy.ndarray:
    """Compute transposed directional gradient with circular boundary condition.
    
    Args:
        array (numpy.ndarray): element for derivation
        axis (int): direction of gradient

    Returns:
        derivative of array
        
    Notes: 
        - You can use the `tdfc` alias
    """
    deriv = difference_finite_circular(numpy.flip(array, axis), axis)
    return numpy.flip(deriv, axis)
    
    
"""
"""
def laplacian2D_difference_finite_circular(array: numpy.ndarray) -> numpy.ndarray:
    """Get laplacian of array with exact definition.

    Args:
        array (numpy.ndarray): array for laplacian

    Returns:
        laplacian of array
        
    Notes: 
        - You can use the `lap2Dc` alias
    """
    d0 = difference_finite_circular(array, axis = 0)
    d1 = difference_finite_circular(array, axis = 1)
    dd0 = transposed_difference_finite_circular(d0, axis = 0)
    dd1 = transposed_difference_finite_circular(d1, axis = 1)
    
    return dd0 + dd1

dfc = difference_finite_circular
tdfc = transposed_difference_finite_circular
lap2Dc = laplacian2D_difference_finite_circular

# def dx(image: numpy.ndarray) -> numpy.ndarray:
#     """ Derivation by column

#     Params:
#         - image
    
#     Return:
#         - first element of gradient
#     """

#     nb_rows, nb_cols = numpy.shape(image)
#     image_derivated = numpy.zeros(shape=(nb_rows, nb_cols))

#     image_derivated[:, 1:nb_cols] = \
#         image[:, 1:nb_cols] - image[:, 0:nb_cols-1]

#     image_derivated[:, 0] = image[:, 0] - image[:, nb_cols-1]

#     return image_derivated
    

# def dy(image: numpy.ndarray) -> numpy.ndarray:
#     """ Derivation by line

#     Params:
#         - image
    
#     Return:
#         - second element of gradient
#     """
    
#     nb_rows, nb_cols = numpy.shape(image)
#     image_derivated = numpy.zeros(shape=(nb_rows, nb_cols))
    
#     image_derivated[1:nb_rows, :] = \
#         image[1:nb_rows, :] - image[0:nb_rows-1, :]

#     image_derivated[0, :] = image[0, :] - image[nb_rows-1, :]

#     return image_derivated


# def dxT(image: numpy.ndarray) -> numpy.ndarray:
#     """ Derivation Transposed by column

#     Params:
#         - image
    
#     Return:
#         - first element of gradient transposed
#     """

#     nb_rows, nb_cols = numpy.shape(image)
#     image_derivated = numpy.zeros(shape=(nb_rows, nb_cols))
    
#     image_derivated[:, 0:nb_cols-1] = \
#         image[:, 0:nb_cols-1] - image[:, 1:nb_cols]

#     image_derivated[:, nb_cols-1] = image[:, nb_cols-1] - image[:, 0]

#     return image_derivated


# def dyT(image: numpy.ndarray) -> numpy.ndarray:
#     """ Derivation Transposed by line

#     Params:
#         - image
    
#     Return:
#         - second element of gradient transposed
#     """
#     nb_rows, nb_cols = numpy.shape(image)
#     image_derivated = numpy.zeros(shape=(nb_rows, nb_cols))
    
#     image_derivated[0:nb_rows-1, :] = \
#         image[0:nb_rows-1, :] - image[1:nb_rows, :]

#     image_derivated[nb_rows-1, :] = image[nb_rows-1, :] - image[0, :]

#     return image_derivated


# def kernel_identity(dim: int) -> numpy.array:
#     shape = numpy.full(shape=dim, fill_value=1)
#     one_nd = numpy.full(shape=tuple(shape), fill_value=1)
#     return numpy.pad(array=one_nd, pad_width=1)





# def laplacian2D(arr: numpy.ndarray, mode: str) -> numpy.ndarray:

#     d_d_ax0 = gradient(arr, axis=0, mode=mode)
#     d_d_ax1 = gradient(arr, axis=1, mode=mode)

#     d2_d2_ax0 = transposed_gradient(d_d_ax0, axis=0, mode=mode)
#     d2_d2_ax1 = transposed_gradient(d_d_ax1, axis=1, mode=mode)

#     return d2_d2_ax0 + d2_d2_ax1
    