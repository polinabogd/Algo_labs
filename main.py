length, inner_length = 6, 7
matrix = [
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"]
        ]


def go_through(out, inn, counter):
    while out < length and inn < inner_length - 1:
        p = matrix[out][inn+2:]
        l = len(p)
        for el in range(len(p)-1):
            if p[el] == matrix[out][inn]:
                k = el+inn+2
                counter += 1
                go_through(out, k, counter)


        if out != 0:
            if matrix[out][inn] == matrix[out-1][inn+1]:
                counter += 1
                go_through(out-1, inn+1, counter)
        if out < length-1:
            if matrix[out][inn] == matrix[out+1][inn+1]:
                counter += 1
                go_through(out+1, inn+1, counter)
        return counter


def result():
    if length == 1:
        counter = 1
        result = go_through(0, 0, counter)
    else:
        counter = 2
        result = go_through(length-1, 0, counter) + go_through(0, 0, counter)
    return result


if __name__ == '__main__':
    print(result())
