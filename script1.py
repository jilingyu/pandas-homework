import numpy as np
import pandas as pd

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

int_array = np.array([1,22.4,5,35,4,6.7,3,8,40])
pretty_print('ndim', int_array.ndim)
pretty_print('shape', int_array.shape)
pretty_print('size', int_array.size)
pretty_print('dsize', int_array.dtype)




int_array1 = np.array([['a', 'b'],['c', 'd'],[3, 3]])
pretty_print('ndim', int_array1.ndim)
pretty_print('shape', int_array1.shape)
pretty_print('size', int_array1.size)
pretty_print('dsize', int_array1.dtype)

a = np.arange(13)
b = np.random.rand(23)

