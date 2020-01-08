'''
PEDAC Process

P - Given an list of lists of numbers, find the absolute difference of the sum of all numbers going diagonally one way. List must have numbers. Doesn't matter how many numbers in the list there are, whatever is diagonal will be added.

E - lists = [[5,6,7,8],
             [2,3,4,5],
             [7,8,1,4],
             [5,6,2,7]
            ]

    diagonal_difference(lists) == 9

    lists = [[5,6,7,8,16],
             [2,3,4,5],
             [7,8,1,4,5,8],
             [5,6,2,7]
            ]

    diagonal_difference(lists) == 9

D - Lists

A: 1 - Create variable holders for sums of both diagonals
   2 - Loop through list
   2a - Create second loop in a range that iterates, then grab indices of those specific numbers by length and store values in variable holders
   3 - Subtract the absolutes of the sums, return answer
'''

def diagonal_difference(lst):
    sum1 = 0
    sum2 = 0

    for lists in lst:
        for i in lists:
            print(i)


diagonal_difference([[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]])