A = set(["Jake", "John", "Eric"])
B = set(["John", "Jill"])
C = set(["Tomek", "Andrzej"])
# Aby dowiedzieć się, które osoby brały udział w obu wydarzeniach, użyj metody intersection (część wspólna):

print(A.intersection(B)) # set(['John'])
print(B.intersection(A)) # set(['John'])
# Aby ustalić, którzy brali udział tylko w jednym z wydarzeń, użyj metody symmetric_difference (różnica symetryczna):

print (A.symmetric_difference(B)) # set(['Jill', 'Jake', 'Eric'])
print (B.symmetric_difference(A)) # set(['Jill', 'Jake', 'Eric'])
# Wyodrębnieniu osób, które brały udział w A i nie brały w B, służy różnica zbiorów difference:

print (A.difference(B)) # set(['Jake', 'Eric']
print (B.difference(A)) # set(['Jill'])
# Z kolei union (suma zbiorów) da nam listę wszyskich osób:

print(A.union(B, C)) # set(['Jill', 'Jake', 'John', 'Eric'])