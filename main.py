
class Node():
    def __init__(self,bias=0,weight=0,input=0):
        self.bias = bias
        self.weight = weight
        self.input = input
    def __repr__(self):
        return f"this neuron has a bias of {self.bias} and a weight of {self.weight} and the input is {self.input}."
        
    def output(self):
        return self.weight*self.input
#first layer:

l1bias = 0.5

NodeA = Node()
NodeB = Node()
NodeC = Node()
NodeD = Node()


NodeA.weight = 1
NodeA.input = 5


NodeB.weight = 3
NodeB.input = 2

NodeC.weight = 2
NodeC.input = 7

NodeD.weight = 6
NodeD.input = 1

#second layer:

l2bias = 1

NodeE = Node()
NodeF = Node()
NodeG = Node()

NodeE.bias = 0.5
NodeE.weight = 5
NodeE.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeE.bias

NodeF.bias = 1
NodeF.weight = 4
NodeF.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeF.bias

NodeG.bias = 5
NodeG.weight = 7
NodeG.input = NodeA.output()+NodeB.output()+NodeC.output()+NodeD.output()+NodeG.bias


#print(NodeG, NodeF, NodeE)