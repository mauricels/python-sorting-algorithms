def insertion_sort(container):
    """
    O notation: O(n²)
    :param container: Mutable container whose elements are comparable
    :return: Sorted container with ascending order
    """
    length = len(container)
    for i in range(1, length):
        value_to_sort = container[i]
        k = i
        while k > 0 and container[k - 1] > value_to_sort:
            container[k] = container[k - 1]
            k -= 1
        container[k] = value_to_sort
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
    print(insertion_sort(unsorted_list))
    print(f'Done. Processing time: {time.process_time() - start}')
