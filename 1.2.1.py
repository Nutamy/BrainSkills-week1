# Даны два целых числа. 
# Выведите значение наименьшего из них.

x = input("Type first integer pls ")
y = input("Type second integer pls ")
if x > y:
    print("min=",y)
elif y > x:
    print("min=",x)
else:
    print(x,"=",y)