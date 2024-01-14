import numpy

import numbers


class snr_db(float):
    """
    Class to represent Signal to Noise ratio in dB.
    """

    def __str__(self) -> str:
        return '{} [dB]'.format(super().__str__())
    
    def to_linear(self) -> 'snr':
        """Convert to SNR in linear.

        Returns:
            linear SNR
        """
        return snr(10 ** (self / 10))
    
    
class snr(float):
    """
    Class to represent Signal to Noise ratio in linear.
    """
        
    def __str__(self) -> str:
        return '{} [linear]'.format(super().__str__())
    
    def to_dB(self) -> 'snr_db':
        """Convert to SNR in dB.

        Returns:
            SNR in dB
        """
        return snr_db(10 * numpy.log10(self))
    
    
        
    