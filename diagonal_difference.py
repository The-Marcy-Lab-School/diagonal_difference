"""
Problem: Given a matrix calculate the absolute difference of the sum of the left and right diagonals
input: An list of list
output: a number
Examples: 
diagonal_difference([[2, 3, 4, 5],
                     [5, 5, 5, 10],
                     [0, 7, 13,10],
                     [9, 9, 9, 9]]) == 3
diagonal_difference([[1,2,3],
                     [4,5,6],
                     [9,8,9]]) == 2
                     
Data Structure: lists 
Algorithm: 
0: loop through list and add first num in the first list to a variable starting at a = 0, the second num in second list and so on...
1: loop through the list and and the last num in first list to a new variable starting at b = 0, the second to last num  in the second list and so on...
2: subtract b from a 
    I: if total is negative, then multiply by -1
    II: if total is positive then return total
"""

def diagonal_difference(lst):
    a = 0
    b = 0
    counter = 0
    backwardsCounter = len(lst) - 1
    for arr in lst:
        arr[counter] + a
        arr[backwardsCounter] + b
        counter += 1
        backwardsCounter -= 1
    difference = a - b
    if difference < 0:
        return difference * -1
    return difference
        
print(diagonal_difference([[1,2,3],[4,5,6],[9,8,9]]))
                     
print(diagonal_difference([[2, 3, 4, 5],[5, 5, 5, 10],[0, 7, 13,10],[9, 9, 9, 9]]))