#P Given an array of numbers, determine the difference between the sum of each individual diagonal.


#E [[2, 3, 4, 5],
#  [5, 5, 5,10],
#  [0, 7, 13, 10],
#  [9, 9, 9, 9]]    3
#     [1 2 3]
#     [4 5 6]
#     [9 8 9]  2

#D Array,numbers


#A Given array of numbers determine the length of each array, 
#get last number in first row and the index - 1 in each subsequent row
# add first diagonal to get number
# get first index in first row and index + 1 after in each subsequent row
#add numbers to get second row num
#subtract and get difference



# New A
#  1 Declare 2 variables,'ltr' for left-to-right diagonal 'rtl' for right to left diagonal
#  2 Loop over matrix 
#       a.for each row in the matrix,increment ltr by row[loop_count].
#  3 Loop over matrix
#       a.for each row in the matrix,increment rtl by row[len(row)-1- loop_count].
#  4 abs(ltr -rtl)
#
#

 


#C
def diagonal_difference(squarematrix):
    count = 0
    for arr in squarematrix[count]:
        print(arr)
       

matrix = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]
                
#diagonal_difference(square)

# New C

def diagonal_difference2(matrix):
    ltr,rtl = 0, 0
    for i in range(len(matrix)):
        ltr += matrix[i][i]
        rtl += matrix[i][(len(matrix)- 1 ) - i]
    return abs(ltr - rtl)
print(diagonal_difference2(matrix))
