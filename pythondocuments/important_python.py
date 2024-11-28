There are 33 reserved words available in Python.
 True,False,None
 and, or ,not,is
 if,elif,else
 while,for,break,continue,return,in,yield
 try,except,finally,raise,assert
 import,from,as,class,def,pass,global,nonlocal,lambda,del,with

False, None, True, and, as, assert, async, await, 
break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

Python contains the following inbuilt data types
1. int 2. float 3. complex 4. bool 5. str 6. bytes 7. bytearray 8. range 9. list 10. tuple 11. set 12. frozenset 13. dict 14. None

Note: Python contains several inbuilt functions
1. type()  to check the type of variable
2. id() to get address of object
3. print() to print the value

The following are various inbuilt functions for type casting.
1. int()
2. float()
3. complex()
4. bool()
5. str()

Fundamental Data Types vs Immutability:
All Fundamental Data types are immutable. i.e once we creates an object,we cannot perform any changes in that object. If we are trying to change then with those changes a new object will be created. This non-chageable behaviour is called immutability.

In Python if a new object is required, then PVM wont create object immediately. First it will check is any object available with the required content or not. If available then existing object will be reused. If it is not available then only a new object will be created. 
The advantage of this approach is memory utilization and performance will be improved.

list data type:
If we want to represent a group of values as a single entity where insertion order required to preserve and duplicates are allowed then we should go for list data type.
1. insertion order is preserved
2. heterogeneous objects are allowed
3. duplicates are allowed
4. Growable in nature
5. values should be enclosed within square brackets.

Note: An ordered, mutable, heterogenous collection of elemnts is nothing but list, where duplicates also allowed.

list=[10,10.5,'durga',True,10] 
    print(list) # [10,10.5,'durga',True,10] 
    
tuple data type:
tuple data type is exactly same as list data type except that it is immutable.i.e we cannot chage values.
Tuple elements can be represented within parenthesis. example:- t=(10,20,30,40)

range Data Type: example:- range(10)
range Data Type represents a sequence of numbers.The elements present in range Data type are not modifiable. i.e range Data type is immutable

set Data Type:
If we want to represent a group of values without duplicates where order is not important then we should go for set Data Type.

1. insertion order is not preserved
2. duplicates are not allowed
3. heterogeneous objects are allowed
4. index concept is not applicable
5. It is mutable collection
6. Growable in nature Example:- s={100,0,10,200,10,'durga'}

frozenset DataType:
It is exactly same as set except that it is immutable.Hence we cannot use add or remove functions.s={10,20,30,40}  fs=frozenset(s)

dict Data Type:
If we want to represent a group of values as key-value pairs then we should go for dict data type.Eg:d={101:'durga',102:'ravi',103:'shiva'}
Duplicate keys are not allowed but values can be duplicated. If we are trying to insert an entry with duplicate key then old value will be replaced with new value.Note: dict is mutable and the order wont be preserved.

None Data Type:None means Nothing or No value associated.
If the value is not available,then to handle such type of cases None introduced.It is something like null value in Java.

The following are various important escape characters in Python
1) \n==>New Line 2) \t===>Horizontal tab 3) \r ==>Carriage Return 4) \b===>Back space 5) \f===>Form Feed 6) \v==>Vertical tab 7) \'===>Single quote 8) \"===>Double quote 9) \\===>back slash symbol

Constants: Constants concept is not applicable in Python.
But it is convention to use only uppercase characters if we don’t want to change value.MAX_VALUE=10
It is just convention but we can change the value

Operators:-
Operator is a symbol that performs certain operations.Python provides the following set of operators
1. Arithmetic Operators
2. Relational Operators or Comparison Operators
3. Logical operators
4. Bitwise oeprators
5. Assignment operators
6. Special operators

1. Arithmetic Operators:
    + ==>Addition
    - ==>Subtraction
    * ==>Multiplication
    / ==>Division operator
    % ===>Modulo operator
    // ==>Floor Division operator
    ** ==>Exponent operator or power operator

2.Relational Operators:   >,>=,<,<=

3.equality operators: == , !=    We can apply these operators for any type even for incompatible types also

4.Logical Operators:   and, or ,not   We can apply for all types.
    x and y:      ==>if x is evaluates to false return x otherwise return y
    Eg:    10 and 20     0 and 20
    If first argument is zero then result is zero otherwise result is y
    x or y:
    If x evaluates to True then result is x otherwise result is y
    10 or 20 ==> 10
    0 or 20 ==> 20
    not x:
    If x is evalutates to False then result is True otherwise False
    not 10 ==>False
    not 0 ==>True
5.Bitwise Operators:   
We can apply these operators bitwise.These operators are applicable only for int and boolean types.
    By mistake if we are trying to apply for any other type then we will get Error. &,|,^,~,<<,>>
    & ==> If both bits are 1 then only result is 1 otherwise result is 0
    | ==> If atleast one bit is 1 then result is 1 otherwise result is 0
    ^ ==>If bits are different then only result is 1 otherwise result is 0
    ~ ==>bitwise complement operator
     1==>0 & 0==>1
    << ==>Bitwise Left shift
    >> ==>Bitwise Right Shift
6.Assignment Operators:    We can use assignment operator to assign value to the variable. Eg:  x=10     x+=1(X will be 11) x+=10 ====> x = x+10
    The following is the list of all possible compound assignment operators in Python
    +=  -=  *=  /=  %=  //=  **= &= |= ^= >>= <<=
7.Ternary Operator:    If condition is True then firstValue will be considered else secondValue will be considered.
    Syntax:    x = firstValue if condition else secondValue
    1) a,b=10,20 
    2) x=30 if a<b else 40 
    3) print(x) #30 
8.Special operators:
    Python defines the following 2 special operators   1. Identity Operators    2. Membership operators
    1. Identity Operators:-   We can use identity operators for address comparison.
        2 identity operators are available
        1. is 
        2. is not
        r1 is r2 returns True if both r1 and r2 are pointing to the same object.r1 is not r2 returns True if both r1 and r2 are not pointing to the same object
        Note: We can use is operator for address comparison where as == operator for content comparison.
    2.Membership operators:-We can use Membership operators to check whether the given object present in the given collection.(It may be String,List,Set,Tuple or Dict).in  Returns True if the given object present in the specified Collection.not in  Retruns True if the given object not present in the specified Collection
        
Flow Control:-
Control Flow
    Conditional Statements
        1) if
        2) if-elif
        3) if-elif-else
    Transfer Statements
        1) break
        2) continue
        3) pass
    Iterative Statements:- If we want to execute a group of statements multiple times then we should go for Iterative statements.
        Python supports 2 types of iterative statements.
        1. for loop
        2. while loop
Strings:-
    Any sequence of characters within either single quotes or double quotes is considered as a String.
    Syntax:   s='durga'  s="durga"
    we can define multi-line String literals by using triple single or double quotes
    s='''durga
        software
        solutions'''
    We can access characters of a string by using the following ways.
    1. By using index
        Python supports both +ve and -ve index.
        +ve index means left to right(Forward direction)
        -ve index means right to left(Backward direction)
    2. By using slice operator
        Syntax: s[bEginindex:endindex:step]
        bEginindex:From where we have to consider slice(substring)
        endindex: We have to terminate the slice(substring) at endindex-1 
        step: incremented value
        Note: If we are not specifying bEgin index then it will consider from bEginning of the string.  If we are not specifying end index then it will consider up to end of the string. The default value for step is 1.s[bEgin:end:step]
        step value can be either +ve or –ve
        if +ve then it should be forward direction(left to right) and we have to consider bEgin to end-1
        if -ve then it should be backward direction(right to left) and we have to consider bEgin to end+1
    Checking Membership: We can check whether the character or string is the member of another string or not by using in and not in operators
        s='durga'
        print('d' in s) #True
        print('z' in s) #False
    Comparison of Strings:
        We can use comparison operators (<,<=,>,>=) and equality operators(==,!=) for strings.
        Comparison will be performed based on alphabetical order.
    Removing spaces from the string:
        We can use the following 3 methods
        1. rstrip()===>To remove spaces at right hand side.
        2. lstrip()===>To remove spaces at left hand side.
        3. strip() ==>To remove spaces both sides.
    Finding Substrings position:We can use the following 4 methods
        For forward direction: find()  index()
            index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.
        For backward direction: rfind() rindex()

    Replacing a string with another string: s.replace(oldstring,newstring).inside s, every occurrence of oldstring will be replaced with newstring.
    
    Counting substring in the given String:We can find the number of occurrences of substring present in the given string by using count()  method.
        1. s.count(substring) ==> It will search through out the string
        2. s.count(substring, bEgin, end) ===> It will search from bEgin index to end-1 index
    
    Splitting of Strings:  We can split the given string according to specified seperator by using split() method.
        l=s.split(seperator)
        The default seperator is space. The return type of split() method is List
        Eg1: 1) s="durga software solutions" 
                l=s.split() for x in l:  print(x) 
    Joining of Strings:  We can join a group of strings(list or tuple) wrt the given seperator.
        s=seperator.join(group of strings)
        Eg: t=('sunny','bunny','chinny')
        s='-'.join(t)
        print(s)
        Output: sunny-bunny-chinny
    Changing case of a String: We can change case of a string by using the following 4 methods.
        1. upper()===>To convert all characters to upper case
        2. lower() ===>To convert all characters to lower case
        3. swapcase()===>converts all lower case characters to upper case and all upper case characters to lower case
        4. title() ===>To convert all character to title case. i.e first character in every word should be upper case and all remaining characters should be in lower case.
        5. capitalize() ==>Only first character will be converted to upper case and all remaining characters can be converted to lower case
    Checking starting and ending part of the string:  Python contains the following methods for this purpose
        1. s.startswith(substring)
        2. s.endswith(substring)
        Eg: s='learning Python is very easy'
        print(s.startswith('learning'))   print(s.endswith('learning'))   print(s.endswith('easy'))
        
    To check type of characters present in a string:   Python contains the following methods for this purpose.
        1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
        2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
        3) isdigit(): Returns True if all characters are digits only( 0 to 9)
        4) islower(): Returns True if all characters are lower case alphabet symbols
        5) isupper(): Returns True if all characters are upper case aplhabet symbols
        6) istitle(): Returns True if string is in title case
        7) isspace(): Returns True if string contains only spaces
        
List Data Structure:-    List vs mutability:
        Once we creates a List object,we can modify its content. Hence List objects are mutable.
    Traversing the elements of List: The sequential access of each element in the list is called traversal.
    Important functions of List:
    I. To get information about list:
        1. len():Returns the number of elements present in the list  Eg: n=[10,20,30,40] print(len(n))==>4
        2. count():It returns the number of occurrences of specified item in the list
            n=[1,1,2,3,2,3,2,1]   print(n.count(2))  print(n.count(1)) print(n.count(3))
        3. index() function: Returns the index of first occurrence of the specified item.
       Eg: n=[1,2,2,2,2,3,3] print(n.index(1)) ==>0  print(n.index(2)) ==>1  print(n.index(3)) ==>5 print(n.index(4)) ==>ValueError: 4 is not in list
    II. Manipulating elements of List:
        1. append() function: We can use append() function to add item at the end of the list.
            Eg: list=[]  list.append("A")   list.append("B") list.append("C")   print(list)
        2. insert() function:   To insert item at specified index position
            1) n=[1,2,3,4,5]             2) n.insert(1,888)             3) print(n) 
        3. extend() function: To add all items of one list to another list
            l1.extend(l2)  all items present in l2 will be added to l1
        4. remove() function: We can use this function to remove specified item from the list.If the item present multiple times then only first occurrence will be removed.
        5. pop() function: It removes and returns the last element of the list.This is only function which manipulates list and returns some element
            Note:1. pop() is the only function which manipulates the list and returns some value
            2. In general we can use append() and pop() functions to implement stack datastructure .by using list,which follows LIFO(Last In First Out) order.In general we can use pop() function to remove last element of the list. But we can use to remove elements based on index
            
            n.pop(index)===>To remove and return element present at specified index.
            n.pop()==>To remove and return last element of the list

            Differences between remove() and pop()
                        remove():-                                                   pop()
            1) We can use to remove special element from the List.            1) We can use to remove last element from the List.
            2) It can’t return any value.                                     2) It returned removed element.
            3) If special element not available then we get VALUE ERROR.      3) If List is empty then we get Error
                
            Note:List objects are dynamic. i.e based on our requirement we can increase and decrease the  size.
            append(),insert() ,extend() ===>for increasing the size/growable nature
            remove(), pop() ======>for decreasing the size /shrinking natur
    III. Ordering elements of List:
        1. reverse(): We can use to reverse() order of elements of list
        2. sort() function:In list by default insertion order is preserved. If want to sort the elements of list according to default natural sorting order then we should go for sort() method.
            For numbers ==>default natural sorting order is Ascending Order
            For Strings ==> default natural sorting order is Alphabetical Order
    Aliasing and Cloning of List objects:
        The process of giving another reference variable to the existing list is called aliasin
        To overcome this problem we should go for cloning. The process of creating exactly duplicate independent object is called cloning.
        We can implement cloning by using slice operator or by using copy() function
    Q. Difference between = operator and copy() function
        = operator meant for aliasing
        copy() function meant for cloning
    Using Mathematical operators for List Objects:
        We can use + and * operators for List objects.
        1. Concatenation operator(+):
            We can use + to concatenate 2 lists into a single list
            Note: To use + operator compulsory both arguments should be list objects,otherwise we will get TypeError.
        2. Repetition Operator(*):
            We can use repetition operator * to repeat elements of list specified number of times
    Comparing List objects :  We can use comparison operators for List objects.
    Membership operators:
        We can check whether element is a member of the list or not by using memebership 
        operators.
        in operator
        not in operator
    clear() function:   We can use clear() function to remove all elements of List.
    List Comprehensions: It is very easy and compact way of creating list objects from any iterable objects(like list,tuple,dictionary,range etc) based on some condition.
        Syntax:list=[expression for item in list if condition]
        Eg: s=[ x*x for x in range(1,11)]   print(s)  v=[2**x for x in range(1,6)]   print(v)
        
Tuple Data Structure:-
    1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple object,we cannot perform any changes in that object.
    Hence Tuple is Read Only version of List.
    2. If our data is fixed and never changes then we should go for Tuple.
    3. Insertion Order is preserved
    4. Duplicates are allowed.
    5. Heterogeneous objects are allowed.
    6. We can preserve insertion order and can differentiate duplicate objects by using ndex.Hence index will play very important role in Tuple also.
    Tuple support both +ve and -ve index. +ve index means forward direction(from left to 
    right) and -ve index means backward direction(from right to left)
    7. We can represent Tuple elements within Parenthesis and with comma seperator.Parenethesis are optional but recommended to use.
    Eg:1. t=10,20,30,40
    Note: We have to take special care about single valued tuple.compulsary the value should ends with comma,otherwise it is not treated as tuple.
    Accessing elements of tuple:    We can access either by index or by slice operator
        1. By using index:
            t=(10,20,30,40,50,60)   print(t[0]) #10             print(t[-1]) #60             print(t[100]) IndexError: tuple index out of range 
        2. By using slice operator:
            t=(10,20,30,40,50,60) 
            print(t[2:5]) 
            print(t[2:100]) 
            print(t[::2]) 
    Important functions of Tuple:
        1. len():- To return number of elements present in the tuple
             Eg:              t=(10,20,30,40)              print(len(t)) #4
        2. count()  To return number of occurrences of given element in the tuple
             Eg:              t=(10,20,10,10,20)              print(t.count(10)) #3
        3. index():-  returns index of first occurrence of the given element.If the specified element is not available then we will get ValueError.
             Eg:
             t=(10,20,10,10,20)
             print(t.index(10)) #0
             print(t.index(30)) ValueError: tuple.index(x): x not in tuple
        4. sorted()
             To sort elements based on default natural sorting order
            1. t=(40,10,30,20) 
            2. t1=sorted(t) 
        5. min() and max() functions:
            These functions return min and max values according to default natural sorting order.
    Tuple Comprehension:
        Tuple Comprehension is not supported by Python.
         t= ( x**2 for x in range(1,6))    Here we are not getting tuple object and we are getting generator object.
        t= ( x**2 for x in range(1,6)) 
        print(type(t)) 
        for x in t: 
        print(x) 
        Output         D:\Python_classes>py test.py          <class 'generator'> 
        
Set Data Structure:- 
    If we want to represent a group of unique values as a single entity then we should go for set.
    Duplicates are not allowed.
    Insertion order is not preserved.But we can sort the elements.
    Indexing and slicing not allowed for the set.
    Heterogeneous elements are allowed.
    Set objects are mutable i.e once we creates set object we can perform any changes in that object based on our requirement.
    We can represent set elements within curly braces and with comma seperation.
    We can apply mathematical operations like union,intersection,difference etc on set objects.
    Eg:s={10,20,30,40}   print(s)  print(type(s)) 
    s={} ==>It is treated as dictionary but not empty set. We have to use set() to create empty set 
    Important functions of set:
        1. add(x):
            Adds item x to the set
            Eg: s={10,20,30}   s.add(40);   print(s) #{40, 10, 20, 30} 
        2. update(x,y,z): To add multiple items to the set.Arguments are not individual elements and these are Iterable objects like List,range etc.
            All elements present in the given Iterable objects will be added to the set.
            Eg:s={10,20,30}   l=[40,50,60,10]  s.update(l,range(5))     print(s)
        Q. What is the difference between add() and update() functions in set?
            We can use add() to add individual item to the Set,where as we can use update() function to add multiple items to Set.
            add() function can take only one argument where as update() function can take any number of arguments but all arguments should be iterable objects.
        Q. Which of the following are valid for set s?
            s.add(10)
            s.add(10,20,30) TypeError: add() takes exactly one argument (3 given)
            s.update(10) TypeError: 'int' object is not iterable
            s.update(range(1,10,2),range(0,10,2))
        3. copy(): Returns copy of the set.   It is cloned object. s={10,20,30} s1=s.copy() print(s1)
        4. pop():  It removes and returns some random element from the set.
        5. remove(x): It removes specified element from the set.  If the specified element not present in the Set then we will get KeyError
            s={40,10,30,20}  s.remove(30)  print(s) # {40, 10, 20} 
            s.remove(50) ==>KeyError: 50
        6. discard(x): It removes the specified element from the set.If the specified element not present in the set then we won't get any error.
            s={10,20,30}             s.discard(10)             print(s) ===>{20, 30}             s.discard(50)             print(s) ==>{20, 30}
        7.clear(): To remove all elements from the Set.
            
    Mathematical operations on the Set:
        1.union():
            x.union(y) ==>We can use this function to return all elements present in both sets
            x.union(y) or x|y
            Eg:x={10,20,30,40}   y={30,40,50,60}
            print(x.union(y)) #{10, 20, 30, 40, 50, 60}
            print(x|y) #{10, 20, 30, 40, 50, 60}
        2. intersection():  x.intersection(y) or x&y    Returns common elements present in both x and y
            Eg: x={10,20,30,40}    y={30,40,50,60}
            print(x.intersection(y)) #{40, 30}
            print(x&y) #{40, 30}
        3. difference(): x.difference(y) or x-y  returns the elements present in x but not in y
            Eg: x={10,20,30,40}  y={30,40,50,60}
            print(x.difference(y)) #{10, 20}
            print(x-y) #{10, 20}
            print(y-x) #{50, 60
        4.symmetric_difference(): x.symmetric_difference(y) or x^y   ,   Returns elements present in either x or y but not in both
            Eg: x={10,20,30,40}   y={30,40,50,60}
            print(x.symmetric_difference(y)) #{10, 50, 20, 60}
            print(x^y) #{10, 50, 20, 60
    Membership operators: (in , not in)
    Set Comprehension: Set comprehension is possible.
        s={x*x for x in range(5)}
        print(s) #{0, 1, 4, 9, 16}
        s={2**x for x in range(2,10,2)}
        print(s) #{16, 256, 64, 4}
    set objects won't support indexing and slicing:
    
Dictionary Data Structure:-
    We can use List,Tuple and Set to represent a group of individual objects as a single entity.If we want to represent a group of objects as key-value pairs then we should go for Dictionary.
     Eg:rollno----name
     phone number--address
     ipaddress---domain name
    Duplicate keys are not allowed but values can be duplicated.
    Hetrogeneous objects are allowed for both key and values.
    insertion order is not preserved.Dictionaries are mutable.Dictionaries are dynamic
    indexing and slicing concepts are not applicable    
    How to update dictionaries?
        d[key]=value
        If the key is not available then a new entry will be added to the dictionary with the Specified key-value pair
        If the key is already available then old value will be replaced with new value.
    How to delete elements from dictionary?
        del d[key]  It deletes entry associated with the specified key.
         If the key is not available then we will get KeyError
    d.clear() To remove all entries from the dictionary
    del d To delete total dictionary.Now we cannot access d
    2. len():-   Returns the number of items in the dictionary
    3. clear():- To remove all elements from the dictionary
    4. get():-   To get the value associated with the key
        d.get(key):-If the key is available then returns the corresponding value otherwise returns None.It wont raise any error.
        d.get(key,defaultvalue):-If the key is available then returns the corresponding value otherwise returns default value.
    4. popitem(): It removes an arbitrary item(key-value) from the dictionaty and returns it.
        If the dictionary is empty then we will get KeyError d={}
        print(d.popitem()) ==>KeyError: 'popitem(): dictionary is empty'
    5. keys(): It returns all keys associated eith dictionary
    6. values():It returns all values associated with the dictionary 
    7. items(): It returns list of tuples representing key-value pairs.  [(k,v),(k,v),(k,v)]
    8. copy(): To create exactly duplicate dictionary(cloned copy).  d1=d.copy();
    9. setdefault(): d.setdefault(k,v)
         If the key is already available then this function returns the corresponding value.
         If the key is not available then the specified key-value will be added as new item to the dictionary
    10. update(): d.update(x)
         All items present in the dictionary x will be added to dictionary .
    Dictionary Comprehension: Comprehension concept applicable for dictionaries also.
        squares={x:x*x for x in range(1,6)} 
        print(squares) 
        doubles={x:2*x for x in range(1,6)} 
        print(doubles) 

FUNCTIONS:-
    If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.We have to define these statements as a single unit and we can call that unit any number of times based on our requirement without rewriting. 
    This unit is nothing but function.The main advantage of functions is code Reusability.
    Note: In other languages functions are known as methods,procedures,subroutines etc
    Python supports 2 types of functions
        1. Built in Functions         2. User Defined Functions
    1. Built in Functions:-  The functions which are coming along with Python software automatically,are called built in functions or pre defined functions. Eg: id()     type()     input()     eval()
    
    2. User Defined Functions:-The functions which are developed by programmer explicitly according to business requirements ,are called user defined functions.  Syntax to create user defined functions:
        def function_name(parameters) :
         """ doc string"""
         return value
        Note: While creating functions we can use 2 keywords
        1. def (mandatory)  2. return (optional
        Parameters:- Parameters are inputs to the function. If a function contains parameters,then at the time of calling,compulsory we should provide values otherwise,otherwise we will get error.
        Return Statement:Function can take input values as parameters and executes business logic, and returns output to the caller with return statement. There are 4 types are actual arguments are allowed in Python.
            1. positional arguments    2. keyword arguments        3. default arguments      4. Variable length arguments
            
            1. positional arguments:
                These are the arguments passed to function in correct positional order.The number of arguments and position of arguments must be matched. If we change the order then result may be changed.If we change the number of arguments then we will get error.
            2. keyword arguments:
                We can pass argument values by keyword i.e by parameter name.
                Eg:def wish(name,msg): 
                    print("Hello",name,msg) 
                    wish(name="Durga",msg="Good Morning") 
                    wish(msg="Good Morning",name="Durga")
                Here the order of arguments is not important but number of arguments must be matched.
                Note: We can use both positional and keyword arguments simultaneously. But first we have to take positional arguments and then keyword arguments,otherwise we will get syntaxerror.
                def wish(name,msg):
                print("Hello",name,msg)
                wish("Durga","GoodMorning") ==>valid
                wish("Durga",msg="GoodMorning") ==>valid
                wish(name="Durga","GoodMorning") ==>invalid 
                SyntaxError: positional argument follows keyword argument
            3. Default Arguments:
                Sometimes we can provide default values for our positional arguments.
                Eg:
                def wish(name="Guest"): 
                print("Hello",name,"Good Morning"
                *Note:After default arguments we should not take non default arguments
            4. Variable length arguments:
                Sometimes we can pass variable number of arguments to our function,such type of  arguments are called variable length arguments.
                We can declare a variable length argument with * symbol as follows.def f1(*n):
                We can call this function by passing any number of arguments including zero number.Internally all these values represented in the form of tuple.
                Note:We can mix variable length arguments with positional arguments.
                Note: After variable length argument,if we are taking any other arguments then we should provide values as keyword arguments.
                Note: We can declare key word variable length arguments also.For this we have to use **.
                def f1(**n):We can call this function by passing any number of keyword arguments. Internally these keyword arguments will be stored inside a dictionary.
               
                Note: Function vs Module vs Library:
                    1. A group of lines with some name is called a function
                    2. A group of functions saved to a file , is called Module
                    3. A group of Modules is nothing but Library
        
    Types of Variables:-        Python supports 2 types of variables.
        1. Global Variables         2. Local Variables
        
        1. Global Variables:-
            The variables which are declared outside of function are called global variables.These variables can be accessed in all functions of that module.
        2. Local Variables:-
            The variables which are declared inside a function are called local variables.Local variables are available only for the function in which we declared it.i.e from outside of function we cannot access.
    
    Global keyword:
        We can use global keyword for the following 2 purposes:
        1. To declare global variable inside function
        2. To make global variable available to the function so that we can perform required modifications
        Note: If global variable and local variable having the same name then we can access global variable inside a function as follows.
        def f1():
            a=111
            print(a)
            print(globals()['a'])
    Recursive Functions:-   A function that calls itself is known as Recursive Function.
        Eg:
        factorial(3)=3*factorial(2)
         =3*2*factorial(1)
         =3*2*1*factorial(0)
         =3*2*1*1
         =6
        factorial(n)= n*factorial(n-1)
        The main advantages of recursive functions are:
        1. We can reduce length of the code and improves readability
        2. We can solve complex problems very easily.
    Anonymous Functions:
        Sometimes we can declare a function without any name,such type of nameless functions are called anonymous functions or lambda functions.
        The main purpose of anonymous function is just for instant use(i.e for one time usage)
        lambda Function: We can define by using lambda keyword.  lambda n:n*n
            Syntax of lambda Function:    lambda argument_list : expression
            Note: By using Lambda Functions we can write very concise code so that readability of the program will be improved.
            Note:Lambda Function internally returns expression value and we are not required to write return statement explicitly.
            Note: Sometimes we can pass function as argument to another function. In such cases lambda functions are best choice.
            We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z  these functions expect function as argument.
    filter() function:
        We can use filter() function to filter values from the given sequence based on some condition.
        filter(function,sequence):- where function argument is responsible to perform conditional check sequence can be list or tuple or string.
         l=[0,5,10,15,20,25,30] 
         l1=list(filter(lambda x:x%2==0,l)) 
         print(l1) #[0,10,20,30] 
         l2=list(filter(lambda x:x%2!=0,l)) 
         print(l2) #[5,15,25]
    map() function:
        For every element present in the given sequence,apply some functionality and generate new element with the required modification. For this requirement we should go for map() function.
        Eg: For every element present in the list perform double and generate new list of doubles.
        Syntax:map(function,sequence)
        The function can be applied on each element of sequence and generates new sequence.
        l=[1,2,3,4,5] 
        l1=list(map(lambda x:2*x,l)) 
        print(l1) #[2, 4, 6, 8, 10] 
        We can apply map() function on multiple lists also.But make sure all list should have same length.
            Syntax: map(lambda x,y:x*y,l1,l2))
             x is from l1 and y is from l2
    reduce() function: reduce() function reduces sequence of elements into a single element by applying the specified function.
        reduce(function,sequence).reduce() function present in functools module and hence we should write import statement.
        Eg: from functools import * 
        l=[10,20,30,40,50] 
        result=reduce(lambda x,y:x+y,l) 
        print(result) # 150
    Function Aliasing: For the existing function we can give another name, which is nothing but function aliasing. 
        Eg:def wish(name):  print("Good Morning:",name) 
        greeting=wish         print(id(wish))         print(id(greeting))         
        greeting('Durga')  wish('Durga')
        Note: In the above example only one function is available but we can call that function by using either wish name or greeting name.
        If we delete one name still we can access that function by using alias name
    
    Nested Functions:We can declare a function inside another function, such type of functions are called Nested functions.
    Note: A function can return another function.
    
    Q. What is the differenece between the following lines?
         f1 = outer
         f1 = outer()
         In the first case for the outer() function we are providing another name f1(function aliasing).
         But in the second case we calling outer() function,which returns inner function.For that inner function() we are providing another name f1
        Note: We can pass function as argument to another function.
    Function Decorators:Decorator is a function which can take a function as argument and extend its functionality and returns modified function with extendedm functionality.The main objective of decorator functions is we can extend the functionality of existing  functions without modifies that function.
    Generators:-   Generator is a function which is responsible to generate a sequence of values.
        We can write generator functions just like ordinary functions, but it uses yield keyword to return values.
    The Special variable __name__:
        For every Python program , a special variable __name__ will be added internally.
        This variable stores information regarding whether the program is executed as an individual program or as a module.
        If the program executed as an individual program then the value of this variable is __main__
        If the program executed as a module from some other program then the value of this variable is the name of module where it is defined.
        Hence by using this __name__ variable we can identify whether the program executed directly or as a module.

Exception Handling:-
    In any programming language there are 2 types of errors are possible.
     1. Syntax Errors
     2. Runtime Errors
    1. Syntax Errors:  The errors which occurs because of invalid syntax are called syntax errors.
    2. Runtime Errors: Also known as exceptions.While executing the program if something goes wrong because of end user input or 
        programming logic or memory problems etc then we will get Runtime Errors
    Note: Exception Handling concept applicable for Runtime Errors but not for syntax errors.
    
    What is Exception: An unwanted and unexpected event that disturbs normal flow of program is called exception.
        Eg: ZeroDivisionError         TypeError         ValueError         FileNotFoundError         EOFError         SleepingError         TyrePuncturedError
        
        It is highly recommended to handle exceptions. The main objective of exception handling is Graceful Termination of the program(i.e we should not block our resources and we should not miss anything)
        Exception handling does not mean repairing exception. We have to define alternative way to continue rest of the program normally.
        
        Every Exception in Python is a class. All exception classes are child classes of BaseException.i.e every exception class extends 
        BaseException either directly or indirectly. 
        Hence BaseException acts as root for Python Exception Hierarchy.
        Most of the times being a programmer we have to concentrate Exception and its child  classes.
        try:  except:
        finally block:
        1. It is not recommended to maintain clean up code(Resource Deallocating Code or Resource Releasing code) inside try block because there is no guarentee for the execution of every statement inside try block always.
        2. It is not recommended to maintain clean up code inside except block, because if there is no exception then except block won't be executed.
         
        Hence we required some place to maintain clean up code which should be executed always irrespective of whether exception raised or not raised and whether exception  handled or not handled. Such type of best place is nothing but finally block.Hence the main purpose of finally block is to maintain clean up code
        
        try:          Risky Code         except:          Handling Code         finally:          Cleanup code
         
        *** Note: There is only one situation where finally block won't be executed ie whenever we are using os._exit(0) function.
        Whenever wee are using os._exit(0) function then Python Virtual Machine itself will be shutdown.In this particular case finally won't be executed.
        
    else block with try-except-finally:
        We can use else block with try-except-finally blocks.else block will be executed if and only if there are no exceptions inside try block.
        try:
        Risky Code
        except:
        will be executed if exception inside try
        else:
        will be executed if there is no exception inside try
        finally:
        will be executed whether exception raised or not raised and handled or not handled
    Various possible combinations of try-except-else-finally:
        1. Whenever we are writing try block, compulsory we should write except or finally block.i.e without except or finally block we cannot write try block.
        2. Wheneever we are writing except block, compulsory we should write try block. i.e except without try is always invalid.
        3. Whenever we are writing finally block, compulsory we should write try block. i.e finally without try is always invalid.
        4. We can write multiple except blocks for the same try,but we cannot write multiple finally blocks for the same try
        5. Whenever we are writing else block compulsory except block should be there. i.e without except we cannot write else block.
        6. In try-except-else-finally order is important.
        7. We can define try-except-else-finally inside try,except,else and finally blocks. i.e nesting of try-except-else-finally is always possible.
    Types of Exceptions:
        In Python there are 2 types of exceptions are possible.
        1. Predefined Exceptions
        2. User Definded Exceptions
        
        1. Predefined Exceptions-: Also known as in-built exceptions. The exceptions which are raised automatically by Python virtual machine         whenver a particular event occurs, are called pre defined exceptions.
        
        2. User Defined Exceptions:Also known as Customized Exceptions or Programatic Exceptions
            Some time we have to define and raise exceptions explicitly to indicate that something  goes wrong ,such type of exceptions are called User Defined Exceptions or Customized Exceptions
            Programmer is responsible to define these exceptions and Python not having any idea about these. Hence we have to raise explicitly based on our requirement by using "raise" keyword.
        How to Define and Raise Customized Exceptions:
        Every exception in Python is a class that extends Exception class either directly or indirectly.
        Syntax: class classname(predefined exception class name):
         def __init__(self,arg):
         self.msg=arg
        Eg:  class TooYoungException(Exception): 
        def __init__(self,arg): 
        self.msg=arg
File Operations:
    The with statement:The with statement can be used while opening a file.We can use this to group file  operation statements within a block.
        The advantage of with statement is it will take care closing of file,after completing all operations automatically even in the case of exceptions also, and we are not required to close explicitly.
        Eg:with open("abc.txt","w") as f: 
            f.write("Durga\n") 
            f.write("Software\n") 
            f.write("Solutions\n") 
            print("Is File Closed: ",f.closed) 
            print("Is File Closed: ",f.closed) 
What is Class: 
    ⚽ In Python every thing is an object. To create objects we required some Model or Plan or Blue print, which is nothing but class.
    ⚽ We can write a class to represent properties (attributes) and actions (behaviour) of object.
    ⚽ Properties can be represented by variables.
    ⚽ Actions can be represented by Methods.
    ⚽ Hence class contains both variables and methods.
    Syntax:
    class className:
     ''' documenttation string '''
    Documentation string represents description of the class. Within the class doc string is always optional. 
    We can get doc string by using the following 2 ways.
    1. print(classname.__doc__)
    2. help(classname)
    
    Within the Python class we can represent data by using variables.There are 3 types of variables are allowed. 
    1. Instance Variables (Object Level Variables)     2. Static Variables (Class Level Variables)     3. Local variables (Method Level Variables
    Within the Python class, we can represent operations by using methods. The following are various types of allowed methods.
    1. Instance Methods     2. Class Methods     3. Static Methods
    
    What is Object:
    Pysical existence of a class is nothing but object. We can create any number of objects for a class.
    Syntax to create object: referencevariable = classname()
    Example: s = Student()
    What is Reference Variable: The variable which can be used to refer object is called reference variable.By using reference variable, we can access properties and methods of object.
    Self variable:self is the default variable which is always pointing to current object (like this keyword in Java).By using self we can access instance variables and instance methods of object.
    
    1. self should be first parameter inside constructor .  def __init__(self):
    2. self should be first parameter inside instance methods. def talk(self):
    Constructor Concept:
        ☕ Constructor is a special method in python.
        ☕ The name of the constructor should be __init__(self)
        ☕ Constructor will be executed automatically at the time of object creation.
        ☕ The main purpose of constructor is to declare and initialize instance variables.
        ☕ Per object constructor will be exeucted only once.
        ☕ Constructor can take atleast one argument(atleast self)
        ☕ Constructor is optional and if we are not providing any constructor then python will provide default constructor.
    Differences between Methods and Constructors:
    Method :-                                                               Constructor:-
    1. Name of method can be any name                            1. Constructor name should be always __init__
    2. Method will be executed if we call that method.           2. Constructor will be executed automatically at the time of object creation.
    3. Per object, method can be called any number of times.     3. Per object, Constructor will be executed only once
    4. Inside method we can write business logic                 4. Inside Constructor we have to declare and initialize instance variables
    Types of Variables: Inside Python class 3 types of variables are allowed.
    1. Instance Variables (Object Level Variables)
    2. Static Variables (Class Level Variables)
    3. Local variables (Method Level Variables)
    
    1. Instance Variables:- If the value of a variable is varied from object to object, then such type of variables are called instance variables.
        For every object a separate copy of instance variables will be created. Where we can declare Instance variables:
        1. Inside Constructor by using self variable
        2. Inside Instance Method by using self variable
        3. Outside of the class by using object reference variable
        
        1. Inside Constructor by using self variable:-  We can declare instance variables inside a constructor by using self keyword. Once we creates object, automatically these variables will be added to the object.
        2.Inside Instance Method by using self variable:- can also declare instance variables inside instance method by using self variable. If any 
        instance variable declared inside instance method, that instance variable will be added once we call taht method.
        3. Outside of the class by using object reference variable:We can also add instance variables outside of a class to a particular object.   
    How to access Instance variables:
    We can access instance variables with in the class by using self variable and outside of the class by using object reference.
    How to delete instance variable from the object:- 1. Within a class we can delete instance variable as follows.del self.variableName
        2. From outside of class we can delete instance variables as follows.  del objectreference.variableName
    Note: The instance variables which are deleted from one object,will not be deleted from other objects.
    
    If we change the values of instance variables of one object then those changes won't be reflected to the remaining objects, because for every object we are separate copy of instance variables are available.    
    1. Static variables:
        If the value of a variable is not varied from object to object, such type of variables we have to declare with in the class directly but outside of methods. Such type of variables are called Static variables.For total class only one copy of static variable will be created and shared by all objects of that class. We can access static variables either by class name or by object reference. But recommended to use class name.
    Instance Variable vs Static Variable:
        Note: In the case of instance variables for every object a seperate copy will be created,but in the case of static variables for total class only one copy will be created and shared by every object of that class.
     
    Various places to declare static variables:
        1. In general we can declare within the class directly but from out side of any method
        2. Inside constructor by using class name
        3. Inside instance method by using class name
        4. Inside classmethod by using either class name or cls variable
        5. Inside static method by using class name
    How to access static variables:
        1. inside constructor: by using either self or classname
        2. inside instance method: by using either self or classname
        3. inside class method: by using either cls variable or classname
        4. inside static method: by using classname
        5. From outside of class: by using either object reference or classnma
    Where we can modify the value of static variable:
            Anywhere either with in the class or outside of class we can modify by using classname.But inside class method, by using cls variable.
    If we change the value of static variable by using either self or object reference variable:
        If we change the value of static variable by using either self or object reference variable, then the value of static variable won't be changed,just a new instance variable with that name will be added to that particular object.
    How to delete static variables of a class:
        We can delete static variables from anywhere by using the following syntax:-   del classname.variablename
        But inside classmethod we can also use cls variable:-   del cls.variablename
        Note: By using object reference variable/self we can read static variables, but we cannot modify or delete.
        If we are trying to modify, then a new instance variable will be added to that particular object.
        t1.a = 70 ,If we are trying to delete then we will get error.
    Local variables:
        Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.Local variables will be created at the time of method execution and destroyed once method completes.
        Local variables of a method cannot be accessed from outside of method
        
Types of Methods:
    Inside Python class 3 types of methods are allowed
    1. Instance Methods     2. Class Methods     3. Static Methods
    1. Instance Methods:
        Inside method implementation if we are using instance variables then such type of methods are called instance methods. 
        Inside instance method declaration,we have to pass self variable.  def m1(self):
        By using self variable inside method we can able to access instance variables.Within the class we can call instance method by using self variable and from outside of the class we can call by using object reference.
        
    Setter and Getter Methods:- We can set and get the values of instance variables by using getter and setter methods.
        Setter Method:  setter methods can be used to set values to the instance variables. setter methods also known as mutator methods.
        syntax: def setVariable(self,variable):  self.variable=variable
        Example:
        def setName(self,name):
         self.name=name
        Getter Method:Getter methods can be used to get values of the instance variables. Getter methods also known as accessor methods.
        syntax:
        def getVariable(self):
         return self.variable
        Example:
        def getName(self):
         return self.name
    
    2. Class Methods:-Inside method implementation if we are using only class variables (static variables), then such type of methods we should declare as class method.We can declare class method explicitly by using @classmethod decorator. For class method we should provide cls variable at the time of declaration. We can call classmethod by using classname or object reference variable.
    3. Static Methods:-In general these methods are general utility methods.Inside these methods we won't use any instance or class variables.
        Here we won't provide self or cls arguments at the time of declaration. We can declare static method explicitly by using @staticmethod decorator.We can access static methods by using classname or object reference.
        
        Note: In general we can use only instance and static methods.Inside static method we can access class level variables by using class name.class methods are most rarely used methods in python.
    Passing members of one class to another class:-  We can access members of one class inside another class.
        
    Inner classes:-  Sometimes we can declare a class inside another class,such type of classes are called inner classes.
        Without existing one type of object if there is no chance of existing another type of object,then we should go for inner classes.
        Example: Without existing Car object there is no chance of existing Engine object. Hence Engine class should be part of Car class.
        class Car:
         .....
         class Engine:
         ......
        Example: Without existing university object there is no chance of existing Department object
        class University:
         .....
         class Department:
         ......
        eg3:
        Without existing Human there is no chance of existin Head. Hence Head should be part of Human.
        class Human:
         class Head:
        Note: Without existing outer class object there is no chance of existing inner class object. Hence inner class object is always associated with outer class object.
