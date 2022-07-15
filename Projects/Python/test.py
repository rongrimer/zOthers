import sys
print(sys.version)

randomvar = 5
for i in range (1, 1000): #1 to 1000 lines of output
	if randomvar>i:
		print (i)
	elif randomvar<i:
		print ('Bruh')



# for later* (not even working yet lol)
x = 5 # example of global variable - can be access anywhere in the program
		# these variables can be mentioned at the start of the program or by using global
		# keyword

def function():
	if 1==1:
		print('Hello')
	else:
		print(10)

""" Difference between class and funtion:
	Class is basically a definition of an Object, where as a function is just a piece of code
	in other words, class is like another instance of a program inside a program which
	- can be defined as a set or categorized on things to have some property or 
		attribute in common or differentiated from others by kind, type, or quality. 
	- is like an encapsulation of data under a single entity and the data can be variable 
		(also called attributes) and functions (also called methods)
	(I hope
	this make sense, just make sure to think about this phrase thoroughly.). CLass is mostly
	used on bigger projects. 
	
	Function can be included in a class while class can't be a part of a function.
		Function inside a class = yes (funtion --> class = yes, function under class = yes)
		class inside a function = no (class --> function = no, class under a function = no)
	"""