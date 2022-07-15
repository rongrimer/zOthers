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

	Methods are functions that are associated with a particular class

	Class essentially is a way of grouping functions (as methods) and data (as properties) 
	into a logical unit revolving around a certain kind of thing withing the class.
	- *If you don't need that grouping, there's no need to make a class (just make a function). 
	"""

# Example:
# function
def double(x):
	return x * 2
# class
class MyClass(object):
# method
	def myMethod(self):
		print "Hello, World"
myObject = MyClass()
myObject.myMethod()  # will print "Hello, World"


""" Alternative on using classes;
	
	 using less or no class if you're doing something a project that isn't big. 


	"""

def 