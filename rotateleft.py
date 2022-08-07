def rotateleft(arr, d):
    #d shows how many times to rotate
    #[d:] will print numbers left after rotation
    listarr = list(arr) #store in list to iterate
    rotated = listarr[d:] + listarr[:d]
    #[:d] will print rotated numbers
    return rotated

#driver code

new = rotateleft([1,2,3,4,5,6], 4)
print(new)
    
