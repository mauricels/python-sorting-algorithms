def quick_sort(container):
    """
    O notation: O(n * log(n))
    :param container: Mutable container whose elements are comparable
    :return: Sorted container with ascending order
    """
    _quick_sort(container, 0, len(container) - 1)
    return container


def _quick_sort(container, left_index, right_index):
    if left_index >= right_index:
        return

    i = left_index
    k = right_index - 1
    pivot = container[right_index]

    while True:
        while container[i] <= pivot and i < right_index:
            i += 1
        while container[k] >= pivot and k > left_index:
            k -= 1
        if i < k:
            container[k], container[i] = container[i], container[k]
        else:
            break

    if container[i] > pivot:
        container[i], container[right_index] = container[right_index], container[i]

    _quick_sort(container, left_index, i - 1)
    _quick_sort(container, i + 1, right_index)


if __name__ == '__main__':
    import time
    import random
    unsorted_list = [
        random.randint(-1000, 1000) for _ in range(0, 1000)
    ]
    print('Unsorted container:')
    print(unsorted_list, sep=', ')
    print('Sorting container...')
    start = time.process_time()
    print(quick_sort(unsorted_list))
    print(f'Done. Processing time: {time.process_time() - start}')
