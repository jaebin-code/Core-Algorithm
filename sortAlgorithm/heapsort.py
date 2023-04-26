def heapsort(arr,left,right):
    temp=arr[left]

    parent = left
    while(parent<(right+1)//2):
        cl=parent*2+1
        cr=cl+1
        child = cr if cr <= right and arr[cr]>arr[cl] else cl
        if temp >= arr[child]:
            break
        arr[parent]=arr[child]
        parent = child
    arr[parent]=temp
arr=[3,6,9,4,5,1,4]

n=len(arr)

for i in range((n-1)//2,-1,-1):
    heapsort(arr,i,n-1)
for i in range(n-1,0,-1):
    arr[0],arr[i]=arr[i],arr[0]
    heapsort(arr,0,i-1)
print(arr)



