import numpy as np
import scipy as sp
import matplotlib as mlt

f = open("ch00_B0833-45_20150612_191438_010_1")
#g = np.array(f.read(60), dtype=int)
garray = np.loadtxt(f)
print(garray)
f.close()

