# Singly linked list
class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Doubly liked list
class DoublylinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None