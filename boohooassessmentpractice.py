""" def occupied (n, y, t):
    found = 0
    for i in range (n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5, "CC..C", ".CC..") """

""" def languages (sen):
    T = 0
    t = 0
    S = 0
    s = 0
    for i in range (len(sen)):
        if sen[i] == "t":
            t += 1
        if sen[i] == "T":
            T += 1
        if sen[i] == "s":
            s += 1
        if sen[i] == "S":
            S += 1
    print(s,S,t,T)
    if t+T >= s+S:
        print("Prolly Eng")
    if t+T < s+S:
        print("Prolly French")
languages("The red cat sat on the mat. Why are you so sad cat? Don't ask that.")
languages("Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre")
languages("Si je discernais ta voix encore Connaissant ce coeur qui doute, Tu me dirais de tirer un trait Quoi que partir me coute.") """

def lang (sent):
    s = 0
    t = 0
    for i in sent:
        if i == "s" or i == "S":
            s += 1
        elif i == "t" or i == "T":
            t += 1
    if s >= t:
        print("French")
    else:
        print("English")
lang("blah bekjsdh euooi")

def honi (line):
    H = 0
    O = 0
    N = 0
    I = 0
    for i in range (line):
        if line[i] == "H":
            H += 1
        if line[i] == "O":
            O += 1
        if line[i] == "N":
            N += 1
        if line[i] == "I":
            I += 1
    print(H,O,N,I)
    if 
honi("MAGNUS")
honi("HHHHOOOONNNNIIII")
honi("PROHODNIHODNIK")