#P Given a nested list as input, output the difference of sum of nums diagonally
#E 
#D Arrays/Lists, variables
#A 
# loop over each array 
# loop again and add the index to their correspnding variables until finished with array
# subtract at end
#C


def diagonalDiffernce(matrixArr):
    leftDiagonal = 0
    rightDiagonal = 0
    
    for (arr in nestedArr) {
        for(i == 0; i > len(nestedArr); i++) {
            leftDiagonal += arr[i];
            rightDiagonal += arr[len(arr) - 1]
        }
    }
    return leftDiagonal - rightDiagonal