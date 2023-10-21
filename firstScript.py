# erster Schritt
print("hello world")

# if-Schleife
x = 50

if x < 50:
    print("x ist kleiner als 50")
elif x == 50:
    print("x ist gleich 50")
else:
    print("x ist größer 50")

y = True
if y:
    print("y ist wahr")

w = False
if w:
    print("w ist wahr")

# while-Schleife
x = 0

while x < 42:
    print(x)
    x = x + 5
print("fertig")

# for-Schleife
liste = ["Python", "Java", "Haskell"]

for w in liste:
    print(w)
print("finish")

# Schleifen staffeln
x = [42, 5, 10]

for w in x:
    if w >= 10:
        print(w)
    if w <= 10:
        print("w is small")
print("finish")