import matplotlib.pyplot
import matplotlib.cm
import numpy
import pathlib

def read(data_path: pathlib.Path) -> numpy.ndarray:
    """Read data from path by function of file's extension.

    Args:
        data_path (pathlib.Path): path of data

    Returns:
        datas from file
    """

    ext = data_path.suffix
    image: numpy.ndarray = None

    if ext == '.npy':
        image = numpy.load(data_path)
    else:
        image = matplotlib.pyplot.imread(data_path)

    return image

def save(data: numpy.ndarray, data_path: pathlib.Path) -> None:
    """Save data.

    Args:
        data (numpy.ndarray): data
        data_path (pathlib.Path): path of data
    """
    
    ext = data_path.suffix

    if ext == '.npy':
        numpy.save(data_path, data)
    else:
        matplotlib.pyplot.imsave(data_path, data)

