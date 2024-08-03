class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes
head.next = node2
node2.next = node3
node3.next = node4

#Deleting the node from beginning
if head is not None:
    head = head.next
# Traverse and print the linked list


current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
