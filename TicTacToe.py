a = [[],[],[]]
b = [[],[],[]]
c = [[],[],[]]

a[][] = 


def playerX():
    row = input("player X! choose row a, b or c: ").lower()
    index = int(input("choose column 1, 2 or 3: "))

    if row[index-1] is None:
        if row == "a":
            a[index-1].append("x")
        elif row == "b":
            b[index-1].append("x")
        elif row == "c":
            c[index-1].append("x")
        else:
            print()
    else:
        print("choose else")
        playerX()


    print(a)
    print(b)
    print(c)

def player0():
    row = input("player 0! choose row a, b or c: ").lower()
    index = int(input("choose column 1, 2 or 3: "))

    if row == "a":
        a[index-1].append("0")
    elif row == "b":
        b[index-1].append("0")
    elif row == "c":
        c[index-1].append("0")

    print(a)
    print(b)
    print(c)


def game():
    while True:
        player0()
        if (a[0] and a[1] and a[2]) or (b[0] and b[1] and b[2]) or (c[0] and c[1] and c[2]) or \
           (a[0] and b[0] and c[0]) or (a[1] and b[1] and c[1]) or (a[2] and b[2] and c[2]) or \
           (a[0] and b[1] and c[2]) or (a[2] and b[1] and c[0]) == "0":
              print("0 wins")
              break

        playerX()
        if (a[0] and a[1] and a[2]) or (b[0] and b[1] and b[2]) or (c[0] and c[1] and c[2]) or \
           (a[0] and b[0] and c[0]) or (a[1] and b[1] and c[1]) or (a[2] and b[2] and c[2]) or \
           (a[0] and b[1] and c[2]) or (a[2] and b[1] and c[0]) == "x":
              print("x wins")
              break

        else:
            continue


game()