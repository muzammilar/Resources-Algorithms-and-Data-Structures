Pyhton classes:
https://docs.python.org/2.7/tutorial/classes.html

Details:
https://docs.python.org/2.7/reference/introduction.html
https://docs.python.org/2.7/genindex-all.html

Arguments are passed neither by value and nor by reference in Python - instead they are passed by assignment.

"call-by-object," or "call-by-object-reference" is a more accurate way of describing it

Java is universally described as pass-by-value only.

# strip removes the trailing characters(usually \n but you can strip the trailing any other character too)
# format can format a number to string as binary or something else.
len(max(format(N, 'b').strip('0').split('1'))) # gets the longest binary gap

reverse_A = A[::-1]
temperatures = [0] * 365
#################################################
# Permuation and Combinations
#################################################

https://docs.python.org/2/library/itertools.html

Infinite Iterators:
Iterator 	Arguments 	Results 	Example
count() 	start, [step] 	start, start+step, start+2*step, ... 	count(10) --> 10 11 12 13 14 ...
cycle() 	p 	p0, p1, ... plast, p0, p1, ... 	cycle('ABCD') --> A B C D A B C D ...
repeat() 	elem [,n] 	elem, elem, elem, ... endlessly or up to n times 	repeat(10, 3) --> 10 10 10

Iterators terminating on the shortest input sequence:
Iterator 	        Arguments 	        Results 	                                        Example
chain() 	        p, q, ... 	        p0, p1, ... plast, q0, q1, ... 	                    chain('ABC', 'DEF') --> A B C D E F
compress() 	        data, selectors 	(d[0] if s[0]), (d[1] if s[1]), ... 	            compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
dropwhile() 	    pred, seq 	        seq[n], seq[n+1], starting when pred fails 	        dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
groupby() 	        iterable[, keyfunc] 	                                                sub-iterators grouped by value of keyfunc(v)
ifilter() 	pred, seq 	elements of seq where pred(elem) is true 	ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
ifilterfalse() 	pred, seq 	elements of seq where pred(elem) is false 	ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
islice() 	seq, [start,] stop [, step] 	elements from seq[start:stop:step] 	islice('ABCDEFG', 2, None) --> C D E F G
imap() 	func, p, q, ... 	func(p0, q0), func(p1, q1), ... 	imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
starmap() 	func, seq 	func(*seq[0]), func(*seq[1]), ... 	starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
tee() 	it, n 	it1, it2, ... itn splits one iterator into n
takewhile() 	pred, seq 	seq[0], seq[1], until pred fails 	takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
izip() 	p, q, ... 	(p[0], q[0]), (p[1], q[1]), ... 	izip('ABCD', 'xy') --> Ax By
izip_longest() 	p, q, ... 	(p[0], q[0]), (p[1], q[1]), ... 	izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

Combinatoric generators:
Iterator 	Arguments 	Results
product() 	p, q, ... [repeat=1] 	cartesian product, equivalent to a nested for-loop
permutations() 	p[, r] 	r-length tuples, all possible orderings, no repeated elements
combinations() 	p, r 	r-length tuples, in sorted order, no repeated elements
combinations_with_replacement() 	p, r 	r-length tuples, in sorted order, with repeated elements
product('ABCD', repeat=2) 	  	AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2) 	  	AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2) 	  	AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2) 	  	AA AB AC AD BB BC BD CC CD DD


#################################################
# Format
#################################################

The sign option is only valid for number types, and can be one of the following:

    Option 	Meaning
    '+' 	indicates that a sign should be used for both positive as well as negative numbers.
    '-' 	indicates that a sign should be used only for negative numbers (this is the default behavior).
    space 	indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.

The '#' option is only valid for integers, and only for binary, octal, or hexadecimal output. If present, it specifies that the output will be prefixed by '0b', '0o', or '0x', respectively.

The ',' option signals the use of a comma for a thousands separator. For a locale aware separator, use the 'n' integer presentation type instead.

Changed in version 2.7: Added the ',' option (see also PEP 378).

width is a decimal integer defining the minimum field width. If not specified, then the field width will be determined by the content.

When no explicit alignment is given, preceding the width field by a zero ('0') character enables sign-aware zero-padding for numeric types. This is equivalent to a fill character of '0' with an alignment type of '='.

The precision is a decimal number indicating how many digits should be displayed after the decimal point for a floating point value formatted with 'f' and 'F', or before and after the decimal point for a floating point value formatted with 'g' or 'G'. For non-number types the field indicates the maximum field size - in other words, how many characters will be used from the field content. The precision is not allowed for integer values.

Finally, the type determines how the data should be presented.

The available string presentation types are:

    Type 	Meaning
    's' 	String format. This is the default type for strings and may be omitted.
    None 	The same as 's'.

The available integer presentation types are:

    Type 	Meaning
    'b' 	Binary format. Outputs the number in base 2.
    'c' 	Character. Converts the integer to the corresponding unicode character before printing.
    'd' 	Decimal Integer. Outputs the number in base 10.
    'o' 	Octal format. Outputs the number in base 8.
    'x' 	Hex format. Outputs the number in base 16, using lower- case letters for the digits above 9.
    'X' 	Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.
    'n' 	Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.
    None 	The same as 'd'.

In addition to the above presentation types, integers can be formatted with the floating point presentation types listed below (except 'n' and None). When doing so, float() is used to convert the integer to a floating point number before formatting.

The available presentation types for floating point and decimal values are:

    Type 	Meaning
    'e' 	Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. The default precision is 6.
    'E' 	Exponent notation. Same as 'e' except it uses an upper case ‘E’ as the separator character.
    'f' 	Fixed point. Displays the number as a fixed-point number. The default precision is 6.
    'F' 	Fixed point. Same as 'f'.
    'g'

    General format. For a given precision p >= 1, this rounds the number to p significant digits and then formats the result in either fixed-point format or in scientific notation, depending on its magnitude.

    The precise rules are as follows: suppose that the result formatted with presentation type 'e' and precision p-1 would have exponent exp. Then if -4 <= exp < p, the number is formatted with presentation type 'f' and precision p-1-exp. Otherwise, the number is formatted with presentation type 'e' and precision p-1. In both cases insignificant trailing zeros are removed from the significand, and the decimal point is also removed if there are no remaining digits following it.

    Positive and negative infinity, positive and negative zero, and nans, are formatted as inf, -inf, 0, -0 and nan respectively, regardless of the precision.

    A precision of 0 is treated as equivalent to a precision of 1. The default precision is 6.
    'G' 	General format. Same as 'g' except switches to 'E' if the number gets too large. The representations of infinity and NaN are uppercased, too.
    'n' 	Number. This is the same as 'g', except that it uses the current locale setting to insert the appropriate number separator characters.
    '%' 	Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.
    None 	The same as 'g'.

#################################################
#################################################



def reassign(list):
  # doesn't change anything, creates a new list
  list = [0, 1]

def append(list):
  # appends
  list.append(1)

list = [0]
reassign(list)
append(list)

The variable is not the object

# for-else loops :P
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print n, 'equals', x, '*', n/x
...             break
...     else:
...         # loop fell through without finding a factor
...         print n, 'is a prime number'
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

The pass statement does nothing.

lambda a, b: a+b

>>> def make_incrementor(n):
...     return lambda x: x + n

>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43

Documentation
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print my_function.__doc__
Do nothing, but document it.

    No, really, it doesn't do anything.


Bitwise operations on Python ints work much like in C. The &, | and ^ operators in Python work just like in C. The ~ operator works as for a signed integer in C; that is, ~x computes -x-1.

You have to be somewhat careful with left shifts, since Python integers aren't fixed-width. Use bit masks to obtain the low order bits. For example, to do the equivalent of shift of a 32-bit integer do (x << 5) & 0xffffffff.
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

Lists:
append, pop, extend(length), insert(i, x), pop([i]), sort, reverse, count(X)
pop by default pops last element
count(X) no of times X appears.
extend: Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
Stacks(append and pop)

Queues(append and popleft)
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()

Namespaces: The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods).

Python strings cannot be changed — they are immutable

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
>>> print 'C:\some\name'  # here \n means newline!
C:\some
ame
>>> print r'C:\some\name'  # note the r before the quote
C:\some\name

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

Unicode Strings.
u'Hello\u0020World !'

To convert a Unicode string into an 8-bit string using a specific encoding, Unicode objects provide an encode() method that takes one argument, the name of the encoding. Lowercase names for encodings are preferred.
>>> u"äöü".encode('utf-8')
'\xc3\xa4\xc3\xb6\xc3\xbc'

Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
>>> squares[:]
[1, 4, 9, 16, 25]

Lists also supports operations like concatenation:
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Unlike strings, which are immutable, lists are a mutable type,

Let A and B be objects of class Foo. Which methods and in which order are called
when print(A + B) is executed?

Ans: __add__(), __str__()

What method should be added to a class Foo to make it print user-friendly object information
instead of some internal object data? In case there are several possible solutions,
choose the most Pythonic one.

Ans. __str__


For with an else statement

def foo(my_list):
    for i in my_list:
        if i % 2:
            print i
        else:
            break
    else:
        print float('inf')


Consider a class in Python with a single field. You want to make sure it's impossible to access it directly as object's attribute outside of the class. How can you do that?
Start field's name with two underscores; it will be still possible to access it from object's __dict__ attribute though.

Python Map function

filter(), map(), and reduce() return copies.

The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice).
del can delete variables

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> fruit = set(basket)               # create a set without duplicates
>>> fruit
set(['orange', 'pear', 'apple', 'banana'])
>>> 'orange' in fruit                 # fast membership testing
True
>>> 'crabgrass' in fruit
False

#################################################
>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])
#################################################

>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
set(['r', 'd'])

#################################################
ENUMERATE
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print i, v
...
0 tic
1 tac
2 toe

#################################################
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

#################################################
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.

>>>
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.iteritems():
...     print k, v
...
gallahad the pure
robin the brave
#################################################
It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
#################################################

The conditions used in while and if statements can contain any operators, not just comparisons.

The comparison operators in and not in check whether a value occurs (does not occur) in a sequence. The operators is and is not compare whether two objects are really the same object; this only matters for mutable objects like lists. All comparison operators have the same priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

>>>
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
Note that in Python, unlike C, assignment cannot occur inside expressions. C programmers may grumble about this, but it avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

5.8. Comparing Sequences and Other Types
Sequence objects may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the ASCII ordering for individual characters. Some examples of comparisons between sequences of the same type:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
#################################################
xrange is a sequence object that evaluates lazily. range creates a list, so if you do range(1, 10000000) it creates a list in memory with 10000000 elements. xrange is a generator, so it is a sequence object is a that evaluates lazily.
#################################################
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print hellos
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"


#################################################
>>> f = open('workfile', 'r+')
>>> f.write('0123456789abcdef')
>>> f.seek(5)      # Go to the 6th byte in the file
>>> f.read(1)
'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
>>> f.read(1)
'd'
#################################################
>>> with open('workfile', 'r') as f:
...     read_data = f.read()
>>> f.closed
True
#################################################
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
#################################################

A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future. Examples of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

By the way, I use the word attribute for any name following a dot — for example, in the expression z.real, real is an attribute of the object z. Strictly speaking, references to names in modules are attribute references: in the expression modname.funcname, modname is a module object and funcname is an attribute of it. In this case there happens to be a straightforward mapping between the module’s attributes and the global names defined in the module: they share the same namespace! [1]

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are writable: you can write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer from the object named by modname.

Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called __builtin__.)

The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. (Actually, forgetting would be a better way to describe what actually happens.) Of course, recursive invocations each have their own local namespace.

A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:

the innermost scope, which is searched first, contains the local names
the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
the next-to-last scope contains the current module’s global names
the outermost scope (searched last) is the namespace containing built-in names
If a name is declared global, then all references and assignments go directly to the middle scope containing the module’s global names. Otherwise, all variables found outside of the innermost scope are read-only (an attempt to write to such a variable will simply create a new local variable in the innermost scope, leaving the identically named outer variable unchanged).

Usually, the local scope references the local names of the (textually) current function. Outside functions, the local scope references the same namespace as the global scope: the module’s namespace. Class definitions place yet another namespace in the local scope.

It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module’s namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time — however, the language definition is evolving towards static name resolution, at “compile” time, so don’t rely on dynamic name resolution! (In fact, local variables are already determined statically.)

#################################################
Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created. So, if the class definition looked like this:

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment. __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".
#################################################
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

#################################################

data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. For example, if x is the instance of MyClass created above, the following piece of code will print the value 16, without leaving a trace:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print x.counter
del x.counter
#################################################
https://docs.python.org/2.7/tutorial/classes.html
#################################################
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
For old-style classes, the only rule is depth-first, left-to-right

Thus, if an attribute is not found in DerivedClassName, it is searched in Base1, then (recursively) in the base classes of Base1, and only if it is not found there, it is searched in Base2, and so on.
#################################################

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.
#################################################

 using the @wrapper syntax. Common examples for decorators are classmethod() and staticmethod().

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
    ...

# Transpose list of lists
>>> theArray = [['a','b','c'],['d','e','f'],['g','h','i']]
>>> zip(*theArray)
[('a', 'd', 'g'), ('b', 'e', 'h'), ('c', 'f', 'i')]



#################################################
Futures module:A pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter.
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)


#################################################
generator
A function which returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements).
#################################################
global interpreter lock
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as dict) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

#################################################
Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run.

#################################################
The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. Most object oriented programming languages provide a default implementation. What makes Python special is that it is possible to create custom metaclasses
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
#################################################
