siema = "siemkaaa"
imie = "Szymon"
print(siema)
# elo elo 3200

print(siema + " " + imie)

#ternary operator
date = 27
print('Teraz') if date > 30 else print('nie')

pizza = "Peperoni"
print(type(pizza) == str)

sentence = "ola ma kota"

print(sentence.replace("ola","ala"))
print(len(sentence))

white = "  aleele   "
print(len(white.strip()))
print(len(white.lstrip()))
print(len(white.rstrip()))

#build a menu
title = "menu".upper()
print(title.center(20,"=")) #ale dzikie ale ussles
print("Coffie".ljust(16,".") + "$1".rjust(4))

# string operators
print("----")
print(pizza[0])
print(pizza[-1])
print(pizza[0:3])
print(pizza[::-1]) #odwrocenie stringu
print(pizza.startswith("O"))