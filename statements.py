>>> # string
>>> a="python string"
>>> print(a)
python string
>>> b=a[:2]
>>> print(b)
py
>>> b=a[2:]
>>> print(b)
thon string
>>> print(a[0])
p
>>> b=a[2+9]
>>> print(b)
n
>>> # negative indices
>>> a[-2]
'n'
>>> a[-:]
SyntaxError: invalid syntax
>>> a[-1]
'g'
>>> a[-5]
't'
>>> a="python"+"string"
>>> print(a)
pythonstring
>>> a="java" + "script"
>>> print(a)
javascript
>>> print(a*3)
javascriptjavascriptjavascript
>>> print("(" + a*3 + ")")
(javascriptjavascriptjavascript)
>>> 
>>> print("this is a backslash (\) mark.")
this is a backslash (\) mark.
>>> print("this is a tab \t key")
this is a tab 	 key
>>> print("this is tab    key")
this is tab    key
>>> print("these are 'single quotes'")
these are 'single quotes'
>>> print("this is a new line")
this is a new line
>>> print("this is a new line\nnew line")
this is a new line
new line
>>> print("this is a \n'single quotes'")
this is a 
'single quotes'
>>> a="PYTHON TUTORIAL"
>>> 'Z IN A'
'Z IN A'
>>> 'Z' IN A
SyntaxError: invalid syntax
>>> 'p' in a
False
>>> a="python tutorial"
>>> 'p' in a
True
>>> print(a.find('p'))
0
>>> 'tut' in a
True
>>> a=('red','black',2000,12.12)
>>> type(a)
<class 'tuple'>
>>> print(a[0])
red
>>> print(a[3])
12.12
>>> print(a[0:3])
('red', 'black', 2000)
>>> a="python"
>>> print(len(a))
6
>>> print(a[::-1])
nohtyp
>>> print(a[4:])
on
>>> 
>>> '{1}{0}'.format('python','format')
'formatpython'
>>> 
>>> '{:>15}'.format('python')
'         python'
>>> '{:*<15}'.format('python')
'python*********'
>>> subjects=['physics','chemistry','maths',2]
>>> print(subjects)
['physics', 'chemistry', 'maths', 2]
>>> numbers=[10,20,30,40,50]
>>> names=["sara","david","warnes","sandy"]
>>> student_info=["sara",1,"chemistry"]
>>> subjects[0]
'physics'
>>> subjects[0:2]
['physics', 'chemistry']
>>> subkects[3]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    subkects[3]
NameError: name 'subkects' is not defined
>>> subjects[3]
2
>>> subjects[3]
2
>>> print(subjects[3])
2
>>> del subjects[2]
>>> print(subjects)
['physics', 'chemistry', 2]
>>> print(len(subjects))
3
>>> len(subjects)
3
>>> subjects*2
['physics', 'chemistry', 2, 'physics', 'chemistry', 2]
>>> subjects[::-1]
[2, 'chemistry', 'physics']
>>> a=set([0,1,2,3,4,5])
>>> for n in a:
	print(n)

	
0
1
2
3
4
5
>>> a="red"
>>> print(a.update(["blue","green"]))
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(a.update(["blue","green"]))
AttributeError: 'str' object has no attribute 'update'
>>> a=set([0,1,2,3,4,5])
>>> print(a.pop())
0
>>> print(a)
{1, 2, 3, 4, 5}
>>> print(a.remove(2))
None
>>> print(a)
{1, 3, 4, 5}
>>> print(a.discard(4))
None
>>> print(a)
{1, 3, 5}
>>> print(a.copy())
{1, 3, 5}
>>> print(a.clear())
None
>>> print(a)
set()
>>> a=set([1,2,3,4,5])
>>> print(a)
{1, 2, 3, 4, 5}
>>> # sets
>>> a={1,2,3,4}
>>> b={3,4,5,6}
>>> print(a|b)
{1, 2, 3, 4, 5, 6}
>>> print(a&b)
{3, 4}
>>> print(a-b)
{1, 2}
>>> 
>>> 
>>> # flows
>>> # conditions
>>> a=10
>>> if a==10:
	print("welcome to ipec")

	
welcome to ipec
>>> year=2020
>>> if year%4==0:
	print("2020 is a leap year")
else:
	print("2020 is not a leap year")

	
2020 is a leap year
>>> age=int(input("enter your age"))
enter your age18
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter your 19
eligible for vote
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter your age 17
not eligible for vote
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter your number:99
number is odd
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
it is a consonent
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
it is a consonent
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
it is not a vowel
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    ch=raw_input("enter your character:")
NameError: name 'raw_input' is not defined
>>> a="t"
>>> print(type(a))
<class 'str'>
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    ch=raw_input("enter your character:")
NameError: name 'raw_input' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
it is not a vowel.
>>> 
>>> 
>>> 
>>> 
>>> # if elif statements
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter first number:7
enter second number:54
enter third number:4
b is the largest number
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
>>> aus
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    aus
NameError: name 'aus' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
0
1
2
3
4
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 2, in <module>
    while(true):
NameError: name 'true' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
the sum of first nine integer is: 
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
the sum of first nine integer is:  45
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
the sum of first 9 numbers is :  0
the sum of first 9 numbers is :  1
the sum of first 9 numbers is :  3
the sum of first 9 numbers is :  6
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
even: 0
odd: 1
even: 2
odd: 3
even: 4
odd: 5
even: 6
odd: 7
even: 8
odd: 9
even: 10
>>> 
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
0
1
2
3
4
5
6
7
8
9
10
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    n-int(input("enter any no. for print table:"))
NameError: name 'n' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any no. for print table:5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5 x 1 = 5
5Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 4, in <module>
    print(n,"x",i,"=",n*i)
KeyboardInterrupt
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any no. for print table:3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any no. for print table:19
19 x 1 = 19
19 x 2 = 38
19 x 3 = 57
19 x 4 = 76
19 x 5 = 95
19 x 6 = 114
19 x 7 = 133
19 x 8 = 152
19 x 9 = 171
19 x 10 = 190
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    n=int("enter number :")
ValueError: invalid literal for int() with base 10: 'enter number :'
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any number=>5
the number is prime.
>>> color_list=["red", "blue", "greem", "black"]
>>> for c in color_list:
	print(c)

	
red
blue
greem
black
>>> range(a)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    range(a)
NameError: name 'a' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number of even numbers : 7
number of odd numbers : 8
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number of even numbers : 0
number of even numbers : 1
number of even numbers : 2
number of even numbers : 3
number of even numbers : 4
number of even numbers : 5
number of even numbers : 6
number of even numbers : 7
number of odd numbers : 8
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
0
1
2
3
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    datalist = [1452,11.23,1+2j, true,'w3resource',(0, -1), [5, 12], {"class":"v", "section":"a"}]
NameError: name 'true' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
type of  1452  is  <class 'int'>
type of  11.23  is  <class 'float'>
type of  (1+2j)  is  <class 'complex'>
type of  w3resource  is  <class 'str'>
type of  (0, -1)  is  <class 'tuple'>
type of  [5, 12]  is  <class 'list'>
type of  {'class': 'v', 'section': 'a'}  is  <class 'dict'>
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
c1
c2
c3
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
c1
c2
c3
c1
c2
c3
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
c1
c2
c3
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 2, in <module>
    for value in color.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
red
green
orange
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
2
3
4
5
6
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
2
7
12
17
 
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
number is even
number is odd
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number is odd 0
number is even 1
number is odd 1
number is even 2
number is odd 2
number is even 3
number is odd 3
number is even 4
number is odd 4
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
number of even numbers:  4
number of odd numbers:  5
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    x=range(start,stop,step)
NameError: name 'start' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    x=range(start,stop,step)
NameError: name 'start' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
range(0, 20, 2)
>>> 
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
Traceback (most recent call last):
  File "C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py", line 1, in <module>
    num=int(raw_input("enter any no. for print table: "))
NameError: name 'raw_input' is not defined
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any no. for print table: 3
3 x i 3
3 x i 6
3 x i 9
3 x i 12
3 x i 15
3 x i 18
3 x i 21
3 x i 24
3 x i 27
3 x i 30
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter any no. for print table: 3
3 x i 6
3 x i 9
3 x i 12
3 x i 15
3 x i 18
3 x i 21
3 x i 24
3 x i 27
3 x i 30
3 x i 33
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
1
2
2
3
3
3
4
4
4
4
5
5
5
5
5
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
1
1
2
1
2
3
1
2
3
4
1
2
3
4
5
>>> 
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
2
3
3
4
4
4
5
5
5
5
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter the number: 58
factorial is :,2350561331282878571829474910515074683828862318181142924420699914240000000000000
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
enter the number: 5
factorial is :,120
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
sum of first  1 integers is:  1
sum of first  2 integers is:  3
sum of first  3 integers is:  6
sum of first  4 integers is:  10
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
0
1
2
4
5
>>> 
 RESTART: C:/Users/TUSHAR ARORA/AppData/Local/Programs/Python/Python37-32/hands.py 
pass when value is  1
1
pass when value is  2
2
pass when value is  3
3
pass when value is  4
4
pass when value is  5
5
>>> 
