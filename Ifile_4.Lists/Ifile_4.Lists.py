lst = list(range(1, 9))
print(lst)

t = len(lst)
k = lst[t-1]
for i in range(0, t, 2):
    lst.insert(1+i,lst[t-1])
    del lst[len(lst)-1]
print(lst)


