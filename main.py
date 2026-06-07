class Node():
    def __init__(self,bias=0.0,weight=[],input=0.0):
        self.bias = bias
        self.weight = weight
        self.input = input
    def __repr__(self):
        return f"this neuron has a bias of {self.bias} and a weight of {self.weight} and the input is {self.input}.\n"
        
    def output(self,i):
        return self.weight[i]*self.input
#first layer:

NodeA = Node()
NodeB = Node()
NodeC = Node()
NodeD = Node()


NodeA.weight = [0.1,0.8]
NodeA.input = 2


NodeB.weight = [0.2,0.2]
NodeB.input = 5

NodeC.weight = [0.3,0.7]
NodeC.input = 7

# NodeD.weight = 6
# NodeD.input = 1

# #second layer:


# NodeE = Node()
# NodeF = Node()
# NodeG = Node()

# NodeE.bias = 0.5
# NodeE.weight = 5
# NodeE.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeE.bias

# NodeF.bias = 1
# NodeF.weight = 4
# NodeF.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeF.bias

# NodeG.bias = 5
# NodeG.weight = 7
# NodeG.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeG.bias

# #third layer:
# NodeH = Node()
# NodeI = Node()

# NodeH.bias = 3
# NodeH.weight = 3
# NodeH.input = NodeE.output()+NodeF.output()+NodeG.output()+NodeH.bias

# NodeI.bias = 0.7
# NodeI.weight = 9
# NodeI.input = NodeE.output()+NodeF.output()+NodeG.output()+NodeI.bias

# #fourth layer:
# NodeJ = Node()

# NodeH.bias = 3.2
# NodeH.weight = 5
# NodeH.input = NodeE.output()+NodeF.output()+NodeG.output()+NodeJ.bias

def ForwardProp(layer1, layer2):
    output = 0
    count = 0
    for neuron in layer1:
        output += neuron.output(count)
        test = layer2[count]
        test.input = output
    test.input+= test.bias #not working, multiple weights
NodeZ = Node()
NodeZ.bias = 1
NodeZ.weight = [0.4]

NodeX = Node()
NodeX.bias = 3
NodeX.weight = [0.5]

NodeY = Node()
NodeY.bias = 0.2

layer1 = [NodeA,NodeB,NodeC]
layer2 = [NodeZ,NodeX]
layer3 = [NodeY]
ForwardProp(layer1,layer2)
ForwardProp(layer2,layer3)