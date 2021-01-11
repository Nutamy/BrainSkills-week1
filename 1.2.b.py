# 1.2.b Для каждого числа х выведите значение sign(x)
# С использованием каскадных инструкций
#
x = int(input("To calculate sgn(x) type integer x = "))
if x > 0:
    y = 1
elif x == 0:
    y = 0
else:
    y = -1
print("x = ",x,"\nsgn(x) = ",y)