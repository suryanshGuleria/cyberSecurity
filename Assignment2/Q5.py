def mult(list):
    x=1
    for j in list:
        x=x*j
    print(x)

    
list=[]
a=0
for i in range(0,3,1):
    a = int(input("Enter the values to be multiplied: "))
    list.insert(i,a)
print(list)

mult(list)
