import numpy


def least_square(A: numpy.ndarray, b: numpy) -> numpy.ndarray:
    """Least square estimation

    Args:
        A (numpy.ndarray): a matrix
        b (numpy): a vector

    Returns:
        Estimation of least square
    """
    pseudo_inverse = (A.T @ A) @ A.T
    solution = pseudo_inverse @ b
    return solution


def total_least_square(A: numpy.ndarray) -> numpy.ndarray:
    """Total least square estimation

    Args:
        A (numpy.ndarray): a matrix

    Returns:
        Estiamtion of total least square
    """

    eigen_values, eigen_vectors = numpy.linalg.eig(A.T @ A)
    indmin = numpy.argmin(eigen_values)
    solution = eigen_vectors[:, indmin]

    return solution