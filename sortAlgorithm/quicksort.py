def quicksort(arr):
    if len(arr)<=1:
        return arr
    left,mid,right=[],[],[]
    pivot=arr[len(arr)//2]
    for num in arr:
        if(num<pivot):
            left.append(num)
        elif(num>pivot):
            right.append(num)
        else:
            mid.append(num)
    return quicksort(left)+mid+quicksort(right)