class LinkList():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    
    dummyNode = LinkList()

    while l1.next != None:
        