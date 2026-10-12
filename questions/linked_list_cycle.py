from data_structures.linked_list import LinkedList


def has_cycle[T](l: LinkedList[T]) -> bool:
    slow = l.head
    fast = l.head

    while fast is not None and fast.next is not None:
        if slow is None:
            return False

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
