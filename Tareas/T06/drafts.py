a = [(1,2,3), (4,5,6), (7,8,9)]

for i in range(len(a)):
    if a[i][1] == 8:
        del a[i]
        break
print(a)