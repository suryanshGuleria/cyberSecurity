#we are assuming here that list is of 7 numbers
d=dict([(2,'Prime'),(3,'Prime'),(4,'Non-Prime'),(5,'Prime'),(6,'Non-Prime'),(7,'Prime')])
lower=2
upper=7
c=0
for num in range(lower ,upper+1):
    if (num >1):
        for i in range(2,num):
            if(num%i==0):
                print((num,d.get(num)))
                del d[num]
                c=c+1
                break
        else:
            print((num,d.get(num)))
print("COUNT OF NON PRIMES : {c}")
print("NEW DICTIONARY : {d}")
