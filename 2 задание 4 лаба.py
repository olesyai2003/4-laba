a = input("Введите слово: ")
r = 0

for i in range(len(a)-1):
    if a[i:i+2] == str('жы') or a[i:i+2] == str('шы'):
        r += 1
if r > 0:
    print ("Словосочитание жи/ши написанно не правильно")
if r == 0:
    print("все верно")