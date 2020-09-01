print("The new list with unique elements is:")
def unique_list(list):
    unique=[]
    n=len(list)

    for i in list:
        if(i not in unique):
            unique.append(i)
    print(unique)

list=[0,1,2,3,2,1,0]
unique_list(list)
