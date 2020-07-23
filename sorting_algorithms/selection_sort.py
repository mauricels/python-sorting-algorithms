def selection_sort(container):
    """
    O notation: O(n²)
    :param container: Mutable container whose elements are comparable
    :return: Sorted container with ascending order
    """
    length = len(container)
    for i in range(length - 1):
        minimum = i
        for k in range(i + 1, length):
            if container[minimum] > container[k]:
                minimum = k
        if minimum != i:
            container[i], container[minimum] = container[minimum], container[i]
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
    print(selection_sort(unsorted_list))
    print(f'Done. Processing time: {time.process_time() - start}')
