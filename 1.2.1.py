# Даны два целых числа. 
# Выведите значение наименьшего из них.

x = input()
y = input()
if x > y:
    print(y)
elif y > x:
    print(x)
else:
    print(x,"=",y)