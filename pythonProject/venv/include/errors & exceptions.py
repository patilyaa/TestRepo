a = int(input())
b = str(a)
b1 = b+b
b2 = b+b+b
print(a+int(b1)+int(b2))


num = int(input())
d = num % 10
c = (num // 10) % 10
b = (num // 100) % 10
a = num // 1000
print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)