#create a 2d array to store some random data

import numpy as np

twoDarray = np.array([[1,3,4,5,5],[3,6,7,5,7],[3,5,6,6,3]])
print(twoDarray)

twoDarray1 = np.insert(twoDarray,1,[[13,2,3]], axis=1)
print(twoDarray1)