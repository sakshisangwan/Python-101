#In this one, we will discuss about strings in python
#Strings are called lists because they are lists...
#Since python variables dont exactly have an explicit datatype, the same list can hold various types of data.
#for example:
l = [1 , 'hello' , 2.342, [42,' is the answer to the ultimate question of life, the universe and everything']]
#yeah, there can be a list within a list.

#printing is as easy as cake. Eating cake. Although it has those cryptic brackets.
print l

#But you always have loops.
for i in l:
    print i

#length of a list
print len(l)

#Lets talk about indexing now
# the indexes in a list start from 0 to one shy of the length (that means, length-1).
# also we can use negative indexes to index from the end.
l=["Hello,", " you", " should" , " die."]
print "l[len(l)-1] = %s is the same as l[-1] = %s" %(l[len(l)-1],l[-1])
