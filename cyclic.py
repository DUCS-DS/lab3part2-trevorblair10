from llist import *
from gencyclic import lst

def llprint(lst, num):
    """print the first num terms of linked list lst"""
    node = lst.head
    while node.next and num >= 0:
        print(node.val, end = ", ")
        node = node.next
        num -= 1
    print(node.val)

def find_cycle(lst):
    """return the start index and length of the cycle"""
    tortoise = lst.head
    hare = lst.head.next.next
    x = 0
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next
        x += 1
    tortoise = tortoise.next
    z = 0
    while tortoise != hare:
        tortoise = tortoise.next
        z += 1
    return x, z

if __name__ == "__main__":

    tup = find_cycle(lst)
    print(f"cycle start: {tup[0]}")
    print(f"length: {tup[1]}")
