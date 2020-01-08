"""
PEDAC
Problem: Given a square matrix, calculate the absolute difference between the sums of its diagonals.
Input: nested arrays
Output: number

Example: [[2,3,4,5], 
          [5,5,5,10],
          [0,7,13,9]
          [9,9,9,9]]  

So 2 + 5 + 13 + 9 =  29
and 5 + 5 + 7 + 9 = 26

the absolute difference is 3

Data: Array
Algorithms:
1: Loop through the first list and just get the nested lists
2: since it is a square matrix i'm assuming only 4 numbers are given 
3: find the [0] list first index
4: find the [1] list second index
5: find the [2] list third index
6: find the [3] list 4 index and store this in left-side variable
7: do the same going backwards and store it in right-side variable
8: subtract the difference and return the value
"""

squarematrix = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]

def diagonal_difference(list):
  for list in squarematrix:
    for nested_l in list:
      left_side = 


diagonal_difference(squarematrix)