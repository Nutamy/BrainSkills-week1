# 1.2.а Шахматный конь ходит буквой "Г". 
# Определить может ли конь сделать ход с одной на другую клетку
# за один ход.
#
# Create chess board
abc = "abcdefjh"
print("\n    Chess board \n")
for a in range(8,0,-1):
    line = ""
    for b in abc:
        line = line + " " + b + str(a)
    print(line)

# Try to get the first position from user
while True:
    placeStart = input("\nType the start place of the horse. example: e4 ")
    try:
        letterStr = placeStart[0]
        #Check that input is correct
        if letterStr in abc and len(placeStart) == 2 and 0 < int(placeStart[1]) < 9:
            x1 = abc.index(letterStr) + 1
            y1 = int(placeStart[1])
            break
        else:
            print("\nSomething wrong")
    except:
        print("\nSomething wrong. Try again")

# Try to get the last position from user
while True:
    placeFinish = input("\nType the target place of the horse. example: d2 ")
    try:
        letterFinish = placeFinish[0]
        #Check that input is correct
        if letterFinish in abc and len(placeFinish) == 2 and 0 < int(placeFinish[1]) < 9:
            x2 = abc.index(letterFinish) + 1
            y2 = int(placeFinish[1])
            break
        else:
            print("\nSomething wrong")
    except:
        print("\nSomething wrong. Try again")

#Check that step is possible
devX = abs(x1 - x2)
devY = abs(y1 - y2)
if devX + devY == 3 and devX != 0 and devY != 0:
    print("\nYes! It is possible step!")
else:
    print("\nNo! It is impossible!")