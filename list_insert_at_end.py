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


#Creating a new node
new_node = Node(50)


head = node1
current = head

while current.next is not None:
    current = current.next

current.next = new_node


# Traverse and print the linked list
head = node1
current = head



while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
