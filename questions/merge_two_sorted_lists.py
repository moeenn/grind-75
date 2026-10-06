from ds.linked_list import LinkedList


def merge_sorted_linked_lists(
    one: LinkedList[int], two: LinkedList[int]
) -> LinkedList[int]:
    result = LinkedList[int]()
    one_current = one.head
    two_current = two.head

    while one_current is not None and two_current is not None:
        if one_current.data <= two_current.data:
            result.append(one_current.data)
            one_current = one_current.next
        else:
            result.append(two_current.data)
            two_current = two_current.next

    # append remaining on both.
    while one_current is not None:
        result.append(one_current.data)
        one_current = one_current.next

    while two_current is not None:
        result.append(two_current.data)
        two_current = two_current.next

    return result


def merge_sorted_lists(one: list[int], two: list[int]) -> list[int]:
    result: list[int] = []
    a = b = 0

    while a < len(one) and b < len(two):
        if one[a] <= two[b]:
            result.append(one[a])
            a += 1
        else:
            result.append(two[b])
            b += 1

    result.extend(one[a:])
    result.extend(two[b:])
    return result


def merge_sorted_lists_simple(one: list[int], two: list[int]) -> list[int]:
    return sorted(one + two)
