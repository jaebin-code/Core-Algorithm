def dividearr(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=dividearr(left)
    right=dividearr(right)
    return mergearr(left,right)

def mergearr(left,right):
    result=[]
    i,j=0,0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
