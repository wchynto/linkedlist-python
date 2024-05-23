from Node import Node
from LinkedList import LinkedList

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linkedList = LinkedList()
linkedList.addFront(node1)
linkedList.addFront(node2)
linkedList.addRear(node3)

# linkedList.removeFront()
# linkedList.removeRear()

linkedList.show()