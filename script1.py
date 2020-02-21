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

c = np.zeros((3, 3))
d = np.random.rand((3, 3))

e = np.ones(20) * 7

f = (np.ones(20) * 7).reshape(4,5)

g = np.ones((6, 6))*36
print(g[0,0])

print(g[:,4])
print(g[:,5])
for i in range(2,3):
    print(g[i,2])
    print(g[i,3])

for i in range(0,5):
    print(np.sum(g[:;i]))