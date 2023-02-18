import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dict_={'a':[11,12,13],'b':[14,15,16]}
df=pd.DataFrame(dict_)
print(df)
print(type(df))
print(df.head())
print(df.mean())
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(A)
print(A.ndim,A.size,A.shape)
print(np.dot(A,B))