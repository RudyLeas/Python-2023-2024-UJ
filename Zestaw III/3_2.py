# issue with this code is that the list.sort() method sorts the list in place and returns None.
# L = [3, 5, 4] ; L = L.sort()
# Solution:
L = [3, 5, 4]
L.sort()
print(L)
# Code below results in "Value Error"
# x, y = 1, 2, 3
# Solution:
x, y = 1, 2
# code below creates a tuple, not a list,which is immutable
# X = 1, 2, 3 ; X[1] = 4
# Solution:
X = [1, 2, 3]
X[1] = 4
print(X)
#Code below tries to assign avalue to an index tghat is out of range
# X = [1, 2, 3] ; X[3] = 4
# Solution:
X = [1, 2, 3]
X.append(4)
print(X)
#Code below will raise atribute error, because strings do not have append method
# X = "abc" ; X.append("d")
# Solution:
X = "abc"
X += "d"
# Code below will raise an error because pow misses an argument
# L = list(map(pow, range(8)))
L = [i**2 for i in range(9)]
print(L)