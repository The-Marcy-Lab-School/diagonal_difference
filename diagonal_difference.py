'''
P: input: list of lists (rows), forming matrix
   output: integer - absolute difference of diagonal sums
E: [[0, 1, 2], [3, 4, 5], [6, 7, 8]] ==>
    0 1 2
    3 4 5
    6 7 8
    ==> 0 + 4 + 8 = 12
    ==> 2 + 4 + 6 = 12
    ==> 12 - 12 == 0
D: Need to store two sums, variables should work
Arrays are my input

A:
- for every row, at the first element, grab first value
at second element, grab second value
at third element, grab third value
-- counter up to this number?
- repeat in reverse, first third, second second, third first

--- two loops -- can be brought down to one with better way to store
meaningful data

C:
'''
def diagonal_difference(lst):
    rtl_diagonal, ltr_diagonal = 0, 0

    for i in range(len(lst)):
        rtl_diagonal += lst[i][i]
        ltr_diagonal += lst[i][len(lst) - 1 - i]
    return abs(rtl_diagonal - ltr_diagonal)

print(diagonal_difference([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
print(diagonal_difference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonal_difference([[2, 3, 4, 5], [5, 5, 5,10], [0, 7, 13, 10], [9, 9, 9, 9]]))