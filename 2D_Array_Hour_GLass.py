#define size of the matrix i-e:6
row = 5
column = 5

# Function to find the maximum sum of hour glass
def Maximum(arr):
    maximum_sum = 0
    if(row < 3 or column < 3):
        print("Not possible")
        exit()
    for i in range(0, row-2):
        for j in range(0, column-2):
                     
            # Considering arr[i][j] as top
            # left cell of hour glass.
            SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) +       (arr[i + 2][j] +
                    arr[i + 2][j + 1] + arr[i + 2][j + 2])
 
            # If previous sum is less
            # then current sum then
            # update new sum in max_sum
            if(SUM > maximum_sum):
                maximum_sum = SUM
            else:
                continue
 
    return maximum_sum

# Driver Code
arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
result = Maximum(arr)
print(result)