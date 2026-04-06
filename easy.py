ARMSTRONG NUMBER
s=9474
n=len(str(s))
print(n)
summ=0
for digit in str(s):
    cs=int(digit)**n
    summ+=cs
if summ==s:
    print(True)
else:
    print(False)

MAJORITY ELEMENT  
nums =[3,2,3,2]
freq={}
for n in nums:
    freq[n]=freq.get(n,0)+1
for i in freq:
    if freq[i]>len(nums)//2:
        print(i)
    else:
        pass

ROTATE LIST BY K
nums = [1, 2, 3, 4, 5]
k = 2  
k=k%len(nums)
nums.reverse()
nums[:k]=reversed(nums[:k])
nums[k:]=reversed(nums[k:])
print(nums)

SECOND LARGEST ELEMENT
nums = [10, 20, 4, 45, 99]
fir=float('-inf')
sec=float('-inf')
for num in nums:
    if num>fir:
        sec=fir
        fir=num
    elif num>sec and num!=fir:
        sec=num
print(sec)

SALARY DISTRIBUTION
s=80000
tax=(s//100)*10
insurance=(s//100)*5
net_salary=s-(tax+insurance)
print(net_salary)
if net_salary>=50000:
    print("Higher")
else:
    print("standard")

RICHEST CUSTOMER WEALTH
accounts = [[1,5],[7,3],[3,5]]
maxx_wealth=0
for i in accounts:
    wealth=sum(i)
    maxx_wealth=max(wealth,maxx_wealth)
print(maxx_wealth)
 
PERFECT NUMBER
n=6
if n<1:
     print(False)
else:
    summ=0
    for i in range(1,n):
        if n%i==0:
            summ+=i
        else:
            pass
    if summ==n:
        print(True)
    else:
        print(False)
   
MERGE DICTIONARIES
d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}
res={}

for i in d1:
    res[i]=d1[i]
    
for i in d2:
     if i in res:
         res[i]+=d2[i]
     else:
         res[i]=d2[i]
print(res)
