a = input("Введите слово")
r = ''
for i in a:
    if i != str('м') or i != str('М') or i != str('н') or i != str('Н'):
        r += str('')
    if i == str('м'):
        r += i
    if i == str('М'):
        r += i
    if i == str('н'):
        r += i
    if i == str('Н'):
        r += i
print(r)