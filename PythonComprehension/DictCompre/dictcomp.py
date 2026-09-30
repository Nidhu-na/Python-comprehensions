#Dictionary comprehension is used to create dictionaries in a compact way.
#{key: value for item in iterable}
nums=[1,2,3,4,5,6,7,8,9]
d={k:k*k for k in nums if k%2!=0}
print(d)

