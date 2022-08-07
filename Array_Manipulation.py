from collections import Counter

def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum

#Driver Code
new = arrayManipulation(10, [[1,2,3], [3,4,5], [4,5,6]])
print(new)