# A set comprehension works almost exactly like list comprehension, except it creates a set.
#{expression for item in iterable}

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
s={n for n in nums}
print(s)

s1={n*n for n in nums if n%2==0}
print(s1)
