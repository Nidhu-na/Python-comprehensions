# 🐍 Python Comprehensions
# Comprehensions are one of the most useful Python features because they let you create collections cleanly and compactly.
# We'll start with List Comprehension.

l=[x for x in range(1,5)]
print(l)


#squares
l1=[x*x for x in range(1,6)]
print(l1)

#every number
#List comprehension with condition
l2=[x for x in range(1,21) if x%2==0]
print(l2)

# Expression = what you want to put into the new list.

# Condition = which elements are allowed.

marks = [35, 78, 42, 91, 28, 65, 88]

l=[m for m in marks if m>=40]
print(l)