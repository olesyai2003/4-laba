a = input("Введите слово: ")
b = input("Введите букву: ")
r = ''
k = 0

for i, x in enumerate(a):
    print(i, x)
    if k == 0 and x == str('и'):
        k += 1
        r += x
    elif k == 1:
        r += b
        k += 1
    else:
        r += x
print(r)
