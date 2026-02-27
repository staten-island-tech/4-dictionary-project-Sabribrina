""" n = 5
y = "CC..C"
t = ".CC.."
def occupy (n, y, t):
    occupied = 0
    for i in range (n): """


def occupied (n, y, t):
    found = 0
    for i in range (n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5, "CC..C", ".CC..")

""" def add(x,y):
    return x +y
result = add(5,6)
print(result) """