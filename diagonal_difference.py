# P:
#     input- square matrix
#     output- diagonal difference 
# E:
    
# D: 
#     lists
    
# A: 
#     take in square matrix
#     start at first position in the first element of the array 
#     go to the second position of second element 
#     third position of third and so on until there are no more elements in the orginal array.
#     do the same but starting from last element and keep reducing position as list keeps going

def diagonal_difference (matrix):
    lToR = 0
    rToL = 0
    for arr in matrix: 
       print (matrix[arr[0]])
       
diagonal_difference([[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]])