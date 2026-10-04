import PIL
import numpy as np
from RealDogOrCatNetwork import ProcessImage

def relu(x): # return extreme differences, ex: dark vs light values
    return np.maximum(0,x)

def relu_derivative(x): #rate of change
    return (x>0).astype(float)

def relu_sigmoid(x): # making x 1 or 0
    return 1/(1+np.exp(-x))

def forwardProp(X):
    zeroRows = np.zeros((60450-59400,3))
    X = np.hstack((X,zeroRows))
    H1 = np.dot(X*weights1) + biases1
    A1 = relu(H1)
    O1 = np.dot(A1,weights2) + biases2

    A2 = relu_sigmoid(O1)
    Cache = {"H1":H1,
            "A1":A1,
            "O1":O1,
            "A2":A2
            }
    return Cache



cat = f"PetImages/Cat/{101+0}.jpg"
Proc_Image, width, height = ProcessImage(cat)
print(Proc_Image)
print(Proc_Image.size)
print(Proc_Image.shape)

zeroRows = np.zeros((45600, 3))
zeroCol = np.zeros((14850, 2))


for i in range(1):
    

    inputSize = height/2*width/2

    hiddenSize = inputSize*0.75

    outputSize = 1

    print(f"{width} * {height} = {inputSize}, hiddenSize = {hiddenSize}")


    np.random.seed(42)

    weights1 = np.random.randn(int(inputSize), outputSize)*0.01
    print(weights1.shape)
    weights1 = np.hstack((weights1,zeroCol))
    weights1 = np.vstack((weights1,zeroRows))

    biases1 = np.zeros((1,outputSize))

    weights2 = np.random.randn(int(inputSize), int(hiddenSize))*0.01

    biases2 = np.zeros((1,int(hiddenSize)))

    #print(f"weights1 = {weights1}, weights 2 = {weights2} biases1 = {biases1}, biases2 = {biases2}")

    # activation functions
    # able to tell similarities in the picture
    
    print(forwardProp(Proc_Image))


