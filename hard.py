Power gain max Wins greedy
a = [2,6,8,1]
b = [1,7,9,2]
a.sort()
b.sort()
i=0
j=0
win=0

while i<len(a) and j<len(b):
    if a[i]>b[j]:
        win+=1
        i+=1
        j+=1
    else:
        i+=1
print(win)
