class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

#Creating new node
new_node = Node(50)

#Inserting new node after second node

current = node1
while current is not None and current.data != 20:
    current = current.next

new_node.next = current.next
current.next = new_node

head = node1
current = head


while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
