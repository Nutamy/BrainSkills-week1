print("The celles of field from 1 to 8")
x1 = int(input("Type the first coordinate of current position (1-8) "))
x2 = int(input("Type the second coordinate of current position (1-8) "))
y1 = int(input("Type the first coordinate where the horse would be (1-8) "))
y2 = int(input("Type the second coordinate where the horse would be (1-8) "))

if 0 < x1 < 9 and 0 < x2 <9 and 0 < y1 <9 and 0 < y2 <9:
    x = abs(x1 - y1)
    y = abs(x2 - y2)
    if x + y == 3 and x != 0 and y != 0:
        print("Yes! It is possible step!")
    else:
        print("No! It is impossible!")
else:
    print("Coordinates aren't existed")

print("A"*121)