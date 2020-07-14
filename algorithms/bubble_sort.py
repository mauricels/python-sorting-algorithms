def bubble_sort(container):
    """
    O notation: O(n²)
    :param container: Mutable container whose elements are comparable
    :return: Sorted container with ascending order
    """
    length = len(container)
    for i in range(length - 1):
        made_changes = False
        for p in range(length - 1 - i):
            if container[p] > container[p + 1]:
                container[p], container[p + 1] = container[p + 1], container[p]
                made_changes = True
        if not made_changes:
            break
    return container


if __name__ == '__main__':
    import time
    import random
    unsorted_list = [
        random.randint(-100, 100) for _ in range(0, 10)
    ]
    print('Unsorted container:')
    print(unsorted_list, sep=', ')
    print('Sorting container...')
    start = time.process_time()
    sorted_list = bubble_sort(unsorted_list)
    print(f'Done. Processing time: {time.process_time() - start}')
    print('Sorted container: ')
    print(sorted_list, sep=', ')
