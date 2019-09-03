# -*- coding: utf-8 -*-


def Find(a, number):
    if not a:
        return False
    row, col = len(a), len(a[0])
    row_i, col_j = row - 1, 0

    while row_i >= 0 and col_j < col:
        if a[row_i][col_j] == number:
            return True
        elif a[row_i][col_j] > number:
            row_i -= 1
        else:
            col_j += 1


if __name__ == '__main__':
    a = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

    number = 16
    print(Find(a,number))