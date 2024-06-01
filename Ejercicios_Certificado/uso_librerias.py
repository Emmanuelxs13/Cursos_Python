#Uso de librerías:

import time

print (dir(time))

time.time_ns()

import time as tm

tm.time_ns()

from time import time_ns as tns

a = tns()

tns()

import sklearn

from sklearn.datasets import load_iris

display(load_iris())