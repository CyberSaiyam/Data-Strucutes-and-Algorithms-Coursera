import numpy


def edit_distance(s1, s2):
    len_1 = len(s1)
    len_2 = len(s2)

    dpresult = numpy.zeros((len_1+1, len_2+1))
    for i in range(len_2+1):
        dpresult[0][i] = i

    for i in range(len_1+1):
        dpresult[i][0] = i

    for i in range(1, len_1+1):
        for j in range(1, len_2+1):
            insertion = dpresult[i][j-1] + 1
            deletion = dpresult[i-1][j] + 1
            mismatch = dpresult[i-1][j-1] + 1
            match = dpresult[i-1][j-1]
            if s1[i-1] == s2[j-1]:
                dpresult[i][j] = min(insertion, deletion, match)
            if s1[i-1] != s2[j-1]:
                dpresult[i][j] = min(insertion, deletion, mismatch)

    return (int(dpresult[len_1][len_2]))


if __name__ == "__main__":
    print(edit_distance(input(), input()))
