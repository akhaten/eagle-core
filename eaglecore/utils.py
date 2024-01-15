import numpy



def circshift(kernel: numpy.ndarray, shift: numpy.ndarray) -> numpy.ndarray:
    """Apply circular shift similary to circshift from GNU Octave / Matlab.

    Args:
        kernel (numpy.ndarray): matrix
        shift (numpy.ndarray): shift

    Returns:
        Circulary shifted matrix
    """
    return numpy.roll(kernel, shift, [ i for i in range(0, kernel.ndim) ])


def fourier_diagonalization(kernel: numpy.ndarray, shape_out: numpy.ndarray) -> numpy.ndarray:
    """Diagonalize kernel in Fourier space.

    Args:
        kernel (numpy.ndarray): filter/kernel for diagonalization
        shape_out (numpy.ndarray): dimesion of output

    Returns:
        diagonalized kernel in Fourier space
    """
    
    # Post Zero Padding Kernel ie add zero to bottom and right of kernel
    shape_arr_ = numpy.array(kernel.shape) 
    shape_out_ = numpy.array(shape_out)
    pad_dim = shape_out_ - shape_arr_
    padded = numpy.pad(
        array = kernel, 
        pad_width = [ (0, pad_value) for pad_value in pad_dim ]
    )
    
    # Circshift kernel
    center = numpy.array(kernel.shape) // 2
    circshifted = circshift(padded, -center)
    
    # Compute diagonalized form
    diagonalized = numpy.fft.fftn(circshifted)
    
    return diagonalized


def make_bccb(kernel: numpy.ndarray) -> numpy.ndarray:
    """Construct Block Circulant-Circulant Block (BCCB) matrix.

    Args:
        kernel (numpy.ndarray): a kernel 2D

    Returns:
        BCCB matrix for the kernel
    """
    
    # Step 1 : Build circshifted kernel
    center = numpy.array(kernel.shape) // 2
    kernel_circshifted = circshift(kernel, -center)
    
    # Step 2 : Build first column of BCCB matrix
    dim = numpy.prod(numpy.array(kernel.shape))
    first_column = numpy.reshape(kernel_circshifted, newshape=dim)
    kernel_bccb = numpy.zeros(shape=(dim, dim))
    kernel_bccb[:, 0] = first_column

    # Step 3 : Build first column-block of BCCB matrix
    
    N, M = kernel.shape
    
    for j in range(1, M):
        for i in range(0, M*N, N):
            kernel_bccb[i:i+N, j] = numpy.roll(kernel_bccb[i:i+N, j-1], 1)

    # Step 4 : Build others columns-blocks of BCCB matrix
    for j in range(1, M):
        kernel_bccb[:, N*j: N*j+N] = numpy.roll(
            kernel_bccb[:, N*(j-1): N*(j-1)+N], (N, 0), (0, 1)
        )
   
    return kernel_bccb


# def make_bccb(p: numpy.ndarray) -> numpy.ndarray :
    
#     N, M = p.shape
    
#     dim = numpy.prod(numpy.array(p.shape))
#     p_cpy = numpy.copy(p)
    
#     p1 = numpy.reshape(p_cpy.T, newshape=dim)
#     P = numpy.zeros(shape=(dim, dim))
#     P[:, 0] = p1

#     # print("First Boucle")
#     # print(P)
#     for j in range(1, M):
#         for i in range(0, M*N, N):
#             P[i:i+N, j] = numpy.roll(P[i:i+N, j-1], 1)
#             # print(P)

#     # print("Second Boucle")
#     for j in range(1, M):
#         P[:, N*j: N*j+N] = numpy.roll(P[:, N*(j-1): N*(j-1)+N], (N, 0), (0, 1))
#         # print(P)


#     return P