# given the head of singly linked list,
# return the value of the tail

def find_tail(head):
    if head.right is None:
        return head.value
    else:
        return find_tail(head.right)
