import numpy

class snr_db(float):
    
    def __init__(self, value) -> None:
        pass
        
    def __str__(self) -> str:
        return '{} [dB]'.format(super().__str__())
    
    def to_linear(self) -> 'snr':
        return snr(10 ** (self / 10))
    
    
class snr(float):
    
    def __init__(self, value) -> None:
        pass
        
    def __str__(self) -> str:
        return '{} [linear]'.format(super().__str__())
    
    def to_dB(self) -> 'snr_db':
        return snr_db(10 * numpy.log10(self))
    
    
        
    