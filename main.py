def kmp_find(pattern, search_list):
    pattern_len = len(pattern)
    list_len = len(search_list)
    lps = [0] * pattern_len
    j = 0
    compute_array(pattern, pattern_len, lps)
    i = 0
    while i < list_len:
        if pattern[j] == search_list[i]:
            i += 1
            j += 1
        if j == pattern_len:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]
        elif i < list_len and pattern[j] != search_list[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_array(pattern, pattern_len, lps):
    len = 0
    i = 1
    while i < pattern_len:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    search_list = "ABABDABACDABABCABAB"
    pattern = "DA"
    kmp_find(pattern, search_list)
