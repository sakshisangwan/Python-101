#OK kids, today we are gonna play reduction.
#In this game we will take an array and perform a repetitive action on a pair of elements
#and then replace the pair with the solution 
#and repeat this by pairing the solution and the next element till we are left with only one element. 

#Step 0 : take a dummy array, dummy!
arr = [1,2,3,4,5,6,7,8,9]

#comment above and uncomment below for user input.
#arr = map(int,raw_input().split())

print "The initial array arr = ", arr

#Step 1: define a solution array.
sol = []

#Step 2 : run a friggin' loop. 
for i in arr:
	
	#Step 3 : do the do.
	sol.append(i**3)

#Step 4 :  print that hard work down
print "sol = ",sol

#All set and done in 5 lines of code, huh? Easy, right?

#WRONG.

#Now lets do that using the reduce fuctionality provided by python

#Step 1: Do Everything.
print "map(lambda x:x**3,arr) = ",map(lambda x:x**3,arr)

#Again, the reduce and lambda is simple and consise. It's a, per se, more python-y approach.
#try applyting this to more problems.
