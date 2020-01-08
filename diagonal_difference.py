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
 


#C
def diagonal_difference(squarematrix):
    count = 0
    for arr in squarematrix.split():
        print(arr)
       




square = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]
                
diagonal_difference(square)
