def bubble_sort(container):
    """
    O notation: O(n²)
    :param container: Mutable container whose elements are comparable
    :return: Sorted container with ascending order
    """
    length = len(container)
    for i in range(length - 1):
        made_changes = False
        for k in range(length - 1 - i):
            if container[k] > container[k + 1]:
                container[k], container[k + 1] = container[k + 1], container[k]
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
    print(bubble_sort(unsorted_list))
    print(f'Done. Processing time: {time.process_time() - start}')
