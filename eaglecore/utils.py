import numpy



def circshift(array: numpy.ndarray, shift: numpy.ndarray) -> numpy.ndarray:
    """Circular Shift
    Similary to matlab function.

    Params:
        - matrix : matrix
        - shift : shift 

    Returns:
        - Circulary shifted matrix
    """
    return numpy.roll(array, shift, [ i for i in range(0, array.ndim) ])


def fourier_diagonalization(kernel: numpy.ndarray, shape_out: numpy.ndarray) -> numpy.ndarray:
    """Diagonalize input in Fourier space

    Params:
        - kernel: filter/kernel for diagonalization
        - shape_out: dimesion of output

    Returns:
        Diagonalisation in Fourier space (Complex Array) of kernel with dimension shape out
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


def make_bccb(p: numpy.ndarray) -> numpy.ndarray :
    
    N, M = p.shape
    
    dim = numpy.prod(numpy.array(p.shape))
    p_cpy = numpy.copy(p)
    
    p1 = numpy.reshape(p_cpy.T, newshape=dim)
    P = numpy.zeros(shape=(dim, dim))
    P[:, 0] = p1

    # print("First Boucle")
    # print(P)
    for j in range(1, M):
        for i in range(0, M*N, N):
            P[i:i+N, j] = numpy.roll(P[i:i+N, j-1], 1)
            # print(P)

    # print("Second Boucle")
    for j in range(1, M):
        P[:, N*j: N*j+N] = numpy.roll(P[:, N*(j-1): N*(j-1)+N], (N, 0), (0, 1))
        # print(P)


    return P