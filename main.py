length, inner_length = 5, 5
matrix = [[0, 0, 0, -1, 0],
           [-1, 0, 0, -1, -1],
           [0, 0, 0, -1, 0],
           [-1, 0, -1, 0, -1],
           [0, 0, -1, 0, 0]]


def go_through():
    counter = 0
    for n in range(length):
        counter += 1

    n, m = 0, 0
    while m < inner_length and n < length:
        counter += find_ways_right(m, n)
        counter += find_ways_cross(m, n)
        m += 1
        n += 1



def find_ways_right(m, n):
    c = 0
    for t in matrix[n]:
        if t == matrix[n][m]:
            c += 1
    return c


def find_ways_cross(m, n):
    c = 0
    if matrix[n][m] == matrix[n + 1][m + 1]:
        c += 1
    elif matrix[n][m] == matrix[n - 1][m + 1]:
        c += 1
    return c


if __name__ == '__main__':
    print(go_through())
