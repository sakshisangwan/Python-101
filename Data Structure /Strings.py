#In this one, we will discuss about strings in python
#Strings are called so because they are a string of characters attached together.
#strings are defined by a series of characters or symbols enclosed in single/double inverted commas

#this here is a string being assigned to variable s
s = 'hello'

#characters in a string can be accesed like the elements of a list. See the list tutorial for more.
print s[1]          ## the char at the index 1
print len(s)        ## the length of s, that is, the number of symbols in s

#the '+' in strings in the concatination operator.
#This means it can be used to connect two or more stings in the order they occour in the operation into a single string.
print s + ' beautiful'  ## 'hello beautiful'

# What happens when we use the '+' operator with a string and an integer?
print s + 23 ## error

#Then how do we concatinate an integer or a float or an other data type for god's sake?
print s + str(23.5)

# % operator is used for outputting formatted text.
s = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print s + ' the house'


#escape characters :
#               \newline	Ignored
#               \\	     Backslash (\)
#               \'	     Single quote (')
#               \"	     Double quote (")
#               \a	     ASCII Bell (BEL)
#               \b	     ASCII Backspace (BS)
#               \f	     ASCII Formfeed (FF)
#               \n	     ASCII Linefeed (LF)
#               \r	     ASCII Carriage Return (CR)
#               \t	     ASCII Horizontal Tab (TAB)
#               \v	     ASCII Vertical Tab (VT)
#               \ooo	 ASCII character with octal value ooo
#               \xhh...	 ASCII character with hex value hh...
