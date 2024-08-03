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


#Deleting the particular

current = head

while current.next.data!=30:
    current = current.next
current.next = current.next.next
# Traverse and print the linked list

current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
