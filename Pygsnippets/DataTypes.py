a = 2  # integer
b = 2.0  # float
c = "3.0"  # string
d = [1, 2, "three"]  # list
e = "1"
print(a*b)  # valid, upcasting
print(a*c)  # valid, but probably not desired: '3.03.0'
print(b*c)  # invalid
print(d[1])  # prints 2
for item in d:  # lists are "iterable"
    print(item)
for character in c:  # strings are iterable
    print(character)  # prints 3\n.\n0
f = e + c  # + joins strings: f = '13.0'
g = d + [someObj, "foobar"]  # + joins lists
