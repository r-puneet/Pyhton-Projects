def binarySearch(a, key):
    s=0
    e=len(a)
    mid=0
    while s<=e:
        # to get integer result
        mid=(s+e)//2

        # checking if key is present at mid 
        if a[mid]>key:
            e=mid-1
        
        # checking if key is greater than mid 
        elif a[mid]<key:
            s=mid+1
        
        # if key is mid return it 
        else:
            return mid
    
    # if key is not found 
    return -1



a=[]

n=int(input("Enter Size:"))

# inserting the elements
for i in range(0,n):
    element=int(input("\nEnter elements:"))
    a.append(element)


key=int(input("\nSearch Number:"))

# calling function
result= binarySearch(a, key)
print("\nArray:{}".format(a))
# printing the result
if result != -1:
    print("\nNumber found at index:",str(result))
else:
    print("\nNumber is not present in the Array")