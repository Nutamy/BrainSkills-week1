abc = "abcdefjh"
while True:
    coordinateFinish = input("Type the starting coordinateFinish of the horse. example: e4 ")
    try:
        firstcoordinateFinishX = coordinateFinish[0]
        if firstcoordinateFinishX in abc and len(coordinateFinish) == 2 and 0 < int(coordinateFinish[1]) < 9:
            print(firstcoordinateFinishX)
            x1 = abc.index(firstcoordinateFinishX) + 1
            print("x1 =",x1)
            y1 = int(coordinateFinish[1])
            print("y1 =",y1)
            print("Start place is ",coordinateFinish)
            break
        else:
            print("Something wrong")
    except:
        print("Something wrong. Try again")
while True:
    coordinateFinish = input("Type the starting coordinateFinish of the horse. example: e4 ")
    try:
        firstcoordinateFinishX = coordinateFinish[0]
        if firstcoordinateFinishX in abc and len(coordinateFinish) == 2 and 0 < int(coordinateFinish[1]) < 9:
            print(firstcoordinateFinishX)
            x2 = abc.index(firstcoordinateFinishX) + 1
            print("x2 =",x2)
            y2 = int(coordinateFinish[1])
            print("y2 =",y2)
            print("Finish place is ",coordinateFinish)
            break
        else:
            print("Something wrong")
    except:
        print("Something wrong. Try again")
devX = abs(x1 - x2)
devY = abs(y1 - y2)
if devX + devY == 3 and devX != 0 and devY != 0:
    print("Yes! It is possible step!")
else:
    print("No! It is impossible!")