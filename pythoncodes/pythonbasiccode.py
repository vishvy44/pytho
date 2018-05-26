import math
# degree to radian
n=input()
r=math.radians(n)
print(r)

# differnce b/w squared sum and sum of square of natural numbers
su=0
summ=0
print("enter the value upto which u want to calculate")
n1=input()
for i in range(1,n1+1):
	su=su+i
	summ=summ+(i*i)
su=su*su
print("the squared sum is {}".format(su))
print("the sum of squares is {}".format(summ))
di=su-summ
print("the differnce is {}".format(di))

# unique elements of first list
mylist=[1,2,1,3,3,1,4,5,2]
newset=set(mylist)
newlist=list(newset)
print("the unique list is {}".format(newlist))
