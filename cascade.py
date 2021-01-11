abc = "abcdefgh"

for a in range(8,0,-1):
    line = ""
    for b in abc:
        line = line + " " + b + str(a)
    print(line)