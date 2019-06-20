
class Node:
    def __init__(self, val=0):
        self.value = val
        self.next = None

obj = Node(5)
one = Node(1)
two = Node(2)
three = Node(3)
# one.next = two
# two.next = three
# two.next = one.next.next
# print(obj)
# print(obj.next, obj.value)
arr = [1, 2, 3]
head = None
tmp = None
for i in arr:
    if head == None:
        head = Node(i)
        tmp = head
    else:
        tmp.next = Node(i)
        tmp = tmp.next
print(head.value, head.next.value, head.next.next.value, head.next.next.next)


