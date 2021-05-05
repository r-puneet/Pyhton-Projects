a=[]
n=int(input("\nEnter Size:"))
for i in range(0,n):
    element=int(input("\nEnter Elements:"))
    a.append(element)
print("\nIndex and its Value:")
for index, value in enumerate(a):
    print(index, value)