total=0
n=0
count=0
while n>=0:       # while loop
  total+=n        # total of all the integers 
  count+=1        # for no of integers added
  n=int(input())  # taking input in integer type
avg=total/(count-1)    # average formula
print(avg)
