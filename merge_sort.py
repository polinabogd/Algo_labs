import time


def cmp(a, d):
    if a >= d:
        return 1
    else:
        return -1


comparisons_counter=0


def merge_sort(input_array, sort_order="asc"):
    global comparisons_counter
    if len(input_array) > 1:
        comparisons_counter += 1
        middle = int(len(input_array) // 2)
        left_part_array = input_array[:middle]
        right_part_array = input_array[middle:]
        merge_sort(left_part_array, sort_order)
        merge_sort(right_part_array, sort_order)
        index_left = 0
        index_right = 0
        element_position = 0
        while index_left < len(left_part_array) and index_right < len(right_part_array):
            comparisons_counter += 2
            if cmp(left_part_array[index_left], right_part_array[index_right]) == cmp(sort_order, "desc"):
                comparisons_counter += 2
                input_array[element_position] = left_part_array[index_left]
                index_left += 1
            else:
                comparisons_counter += 2
                input_array[element_position] = right_part_array[index_right]
                index_right += 1
            element_position += 1
        while index_left < len(left_part_array):
            comparisons_counter += 1
            input_array[element_position] = left_part_array[index_left]
            index_left += 1
            element_position += 1
        while index_right < len(right_part_array):
            comparisons_counter += 1
            input_array[element_position] = right_part_array[index_right]
            index_right += 1
            element_position += 1
    return input_array


if __name__ == '__main__':
    input_array = [int(item) for item in input("Enter the array items : ").split(",")]
    print("Merge sort")
    time_start = time.perf_counter()
    print('Result: ',merge_sort(input_array, "desc"))
    end_time = (time.perf_counter() - time_start) * 1000
    print('Execution time: {} ms'.format(end_time))
    print('Comparisons: ', comparisons_counter)
    print('There are no swaps')
