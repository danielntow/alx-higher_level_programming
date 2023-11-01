#!/usr/bin/python3
import sys

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)


l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)


def increment(n):
    n += 1


a = 1
increment(a)
print(a)


def increment(n):
    n.append(4)


l = [1, 2, 3]
increment(l)
print(l)


def assign_value(n, v):
    n = v
    print("n local", n)
    print("v local", v)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


a = ()
a = (1,)
print(type(a))
print(id(a))

a = (1, 2, 'e')
b = (1, 2, 'e')
print(a is b)
print(a == b)
a = [1, 2, 'e']
b = [1, 2, 'e']
print(a is b)
print(a == b)


a = (1, 2)
b = (1, 2)
print(a is b)
print(a == b)


a = [1, 2, 3]
print(id(a))
a = [1, 2, 3]
a += [4]
print(id(a))


a = ()
b = ()
print(a is b)
print(a == b)

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
print(s1 == s2)
print(sys.intern(s1) is sys.intern(s2))
