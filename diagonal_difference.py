"""
P - Add the the right and left diagonals in a matrix then return the absolute value of the | left diagonal - right diagonal | 

E - squarematrix = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]

    diagonal_matrix(squarematrix) == 3
    
    squarematrix = []
    
D - List Integers

A - 1. Declare two variables `ltr` - left to right, `rtl` - right to left 
For the left diagonal start at index 0 and then in go onto the next array and increment the index by 1 and continue adding the values until the last value of the last array is reached. 
  For the right diagonal start from the last index of the first array and go through each array and decrement by 1 until the last value is reached 
  return the abs value of the left diagonal - right diagonal
"""

def diagonal_difference(matrix):
    ltr, rtl = 0, 0
    for i in range(len(matrix)):
        ltr += matrix[i][i]
        rtl += matrix[i][(len(matrix) - 1 )-  i]
        
    return abs(ltr - rtl)
    
matrix = [[2, 3, 4, 5],
        [5, 5, 5,10],
        [0, 7, 13, 10],
        [9, 9, 9, 9]]

print(diagonal_difference(matrix));
                