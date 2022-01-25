
#! Arrays
a= ["a",1,2,4,"b"]

#!['a', 1, 2, 4, 'b']
print(a)

#! a
print(a[0])

#! ['a', 1, 2]
print(a[0:3])

a = a + ["test"]

#! ['a', 1, 2, 4, 'b', 'test']
print(a)

#! Dictionary
b= {"oguhpereira":"gustavo","old":21}

#!{'oguhpereira': 'gustavo', 'old': 21}
print(b)

#! gustavo
print(b["oguhpereira"])

b["new"]="new item"

#!{'oguhpereira': 'gustavo', 'old': 21, 'new': 'new item'}
print(b)

#!String is Array
stringText = "test string"

#! e
print(stringText[1])

#! est s
print(stringText[1:6])

#! Tuple
c = (1,2,3)

#!  (1,2,3)
print(c)

#! 2
print(c[1])

#(1,)
print(c[0:1])

#! error add c[4] =3