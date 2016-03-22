import math

N = int(input("Enter the N, please: "))
lst = list(range(0,N))
#temp array
for i in lst:
    lst[i] = 1

for i in range(2, int(math.sqrt(N))+1):
    for j in range (i*i, N, i):
        lst[j] = 0

primeNumbers = list()
k = 0

for x in lst:
    k += 1
    if (x == 1):
        primeNumbers.append(k-1)
primeNumbers.pop(0)
#array for Prime numbers
factors = list()
#temp value
temp = 0
#append 1
factors.append(1)
print("Prime numbers: ")
print(primeNumbers)

#length of array with the Prime numbers
l = len(primeNumbers)

for i in range ( 1, N+1 ):
    print( i )
    temp = i
    j = 1
    while ( j < l ):
        if temp%primeNumbers[j] == 0 and temp != 1:
            factors.append(primeNumbers[j])
            temp = int(temp/primeNumbers[j])
            j = 1
            continue
        if temp == 1:
            #prime factors for each number
            print(factors)
            factors.clear()
            break
        j += 1





