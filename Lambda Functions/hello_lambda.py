#Consider this function.
def f(x,y):
	return x>y
#Creating functions like this for small purposes can be a pain.
#That's why we use lambda functions (totally not the real reason, though)
#Instead we can do this.

l = lambda x,y:x>y

#Which is consise and simple.
#It has a similar useage.

print ("Using f(x,y)") , (f(100,200)) , (f(12234234241,4))
print ("Using lambda x,y"),(l(100,200)),(l(12234234241,4))

#This was a brutally short tutorial on lmbda functions
# Q : But Why use Lambda Functions?
# A : Because all the cool kids are doing it.
