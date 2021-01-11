# Даны три целых числа. 
# Выведите значение наименьшего из них

# First solution from Python with LOVE
a = 1
b = 2
c = 3
print(min(a,b,c))

# Second solution if we use other programming language
x = int(input())
y = int(input())
z = int(input())
if x < y:
    if x < z:
        print(x)
    else:
        print(z)

else:
    if y < z:
        print(y)
    else:
        print(z)
