def search_ways(start_indexes: list, matrix: [[]]):
    idx_amount = len(start_indexes)
    for indexes in start_indexes:
        left_idx = find_left_indexes(indexes, matrix)
        if len(left_idx) > 0:
            idx_amount += search_ways(left_idx, matrix) - 1
    return idx_amount


def find_left_indexes(right_idx: tuple, matrix: list):
    value = matrix[right_idx[0]][right_idx[1]]
    left_indexes = []
    for outer_idx in range(len(matrix)):
        for inner_idx in range(right_idx[1]):
            if matrix[outer_idx][inner_idx] == value:
                left_indexes.append((outer_idx, inner_idx))
    if right_idx[1] != 0 and matrix[right_idx[0]][right_idx[1] - 1] != value:
        left_indexes.append((right_idx[0], right_idx[1] - 1))
    return left_indexes


def result(matrix, length, inner_length):
    counter = 0
    if len(matrix) == 1:
        counter = search_ways([(0, inner_length - 1)], matrix)
    elif len(matrix) > 1:
        counter = search_ways([(0, inner_length - 1), (length - 1, width - 1)], matrix)

    return counter


if __name__ == '__main__':
    ijones_matrix = open("ijones.in", 'r').read().split('\n')[1:]
    width = len(ijones_matrix[0])
    height = len(ijones_matrix)
    print(result(ijones_matrix,height, width))
