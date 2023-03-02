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
    """tortoise = lst.head
    hare = lst.head.next.next
    x = 0
    while tortoise:"""



if __name__ == "__main__":

    llprint(lst, 10)
