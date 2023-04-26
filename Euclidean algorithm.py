a,b=map(int,input().split()) # Input two number
x,y=min(a,b),max(a,b)        # Store small numbers in x and large numbers in y

while(x!=0):                 # Eculidean algorithm
    x,y=y%x,x
print(a*b/y)