print("------------- Logical operator not! --------------")

a = not 5==5
print (a)
b = not 4==5
print(b)

c = not None and "Hello world!"
print(c)

d = not None or "I love you"
print(d)

e = not(not True) or 10 and 20
print(c)

f = not not (not True) or 10 and not 20
print ( f)