def linearSearch(a, key):
    for i in range(len(a)):
        if a[i]==key:
            return i
    return -1

a = []
n = int(input("Enter Size:"))
for i in range(0,n):
    element = int(input("\nEnter element:"))
    a.append(element)
key = int(input("\nSearch Number:"))
print("\nElement found at Index:", linearSearch(a, key))