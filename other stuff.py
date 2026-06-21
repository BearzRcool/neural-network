import numpy as np
import sys
import matplotlib
#input * weight + bias


inputs = [1.1, 1.5, 1.2]
weights = [0.5, 0.8, 0.2]
bias = 2
# parameters = # of neurons + # of weights
output = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + (inputs[2] * weights[2]) + bias
print(output)

inputs = np.array([1.1, 1.5, 1.2])
weights = np.array([0.5, 0.8, 0.2])

output = np.dot(inputs, weights) + bias
#print(output)

#weights = number parameters that determine the strength of connections between neurons (influences the inputs.)
#dot product: vectors, matrices
#numpy array: can look through 50x faster than reg lists

#challenge:
inputs = np.array([1.8, 1.7, 3.6])
weights1 = np.array([0.1, 0.5, 0.3])
weights2 = np.array([0.2, 0.8, 0.2])
weights3 = np.array([0.4 , 1])
bias = np.array([2,3,1])

output1 = np.dot(inputs, weights1)+ bias[0]
output2 = np.dot(inputs, weights2)+ bias[1]
inputs2 = np.array([output1, output2])
output3 = np.dot(inputs2, weights3)+ bias[2]

print(output3)
#2d array:
array_2d = np.array([[5,6,8], [1,2,3]])
print(array_2d)

# next time: gradient descent (loss algorithm/correction)
# how to setup weights automatically
# apply to find a pattern in linear equation