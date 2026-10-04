class LinkList():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):

    currentl1 = l1
    currentl2 = l2
    
    values = []
    returnNode = LinkList()
    carry = 0
    while currentl1 != None:
        currentl1.val = currentl1.val + currentl2.val + carry
        if currentl1.val >= 10:
            carry = 1
            currentl1.val -= 10
        else:
            carry = 0

        print(currentl1.val)

        currentl1 = currentl1.next
        currentl2 = currentl2.next

    
    #     values.append(dummyNode.val)
    #     dummyNode.val = 0
    # for value in values:
    #     if value == values[0]:
    #         returnNode = value
    #         returnNode.next = dummyNode
    #     else:
    #         dummyNode.val = value
        


l1 = LinkList(1)
l12 = LinkList(2)
l13 = LinkList(3)

l1.next = l12
l12.next = l13

l2 = LinkList(4)
l22 = LinkList(5)
l23 = LinkList(6)

l2.next = l22
l22.next = l23

addTwoNumbers(l1,l2)