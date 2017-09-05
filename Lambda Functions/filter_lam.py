#OK kids, today we are gonna play filter.
#In this game we will take an array and execute a boolean returning action on every element one by one
#and then remove all those who end up returning false when passed to that action.
#This is used in cases you want to only keep the elements that satisfy a particualar condition 

#Step 0 : take a dummy array, dummy!
arr = [1,2,3,4,5,6,7,8,9]
al=arr
#comment above and uncomment below for user input.
#arr = map(int,raw_input().split())

print "The initial array arr = ", arr

#Step 1: define a condition FUNKtion (we return whether x is even(true) or not(false))
def funk(x):
	return (x%2!=1)

#Step 2 : run a friggin' loop.
lim= len(arr)
i=0
while i<lim:
	
	#Step 3 :
	if not funk(arr[i]):
		del arr[i];
	i+=1
	lim=len(arr)
#Step 4 :  print that hard work down
print "arr = ", arr

#All set and done in 5 lines of code, huh? Easy, right?

#WRONG.

#Now lets do that using the filter fuctionality provided by python

#Step 1: Do Everything.
print "filter(lambda x:x%2!=1,al) = ",filter(lambda x:x%2!=1,al)

#Again, the filter and lambda method is simple and consise. It's a, per se, more python-y approach.
#try to use them in some programs.
