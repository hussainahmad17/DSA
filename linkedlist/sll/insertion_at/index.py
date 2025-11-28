class Node:
    def __init__(self,val):
        self.val=val
        self.head=None

class Singli:
    def __init__(self):
        self.head=None

    def insertat(self,value,position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count<position:
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node
            new_node.next = current


sll = Singli()
sll.insertat(100,3)

        