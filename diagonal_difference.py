# P - Add the the right and left diagonals in a matrix then return the absolute value of the | left diagonal - right diagonal | 

# E - squarematrix = [[2, 3, 4, 5],
#                 [5, 5, 5,10],
#                 [0, 7, 13, 10],
#                 [9, 9, 9, 9]]

#     diagonal_matrix(squarematrix) == 3
    
#     squarematrix = []
    
# D - For loops

# A - For the left diagonal start at index 0 and then in go onto the next array and increment the index by 1 and continue adding the values until the last value of the last array is reached. 
#   For the right diagonal start from the last index of the first array and go through each array and decrement by 1 until the last value is reached 
#   return the abs value of the left diagonal - right diagonal


def diagonal_difference(squarematrix):
    left_total = 0
    right_total = 0 
    for row in squarematrix:
        for number in row:
            left_total += number
            row[number + 1]
        