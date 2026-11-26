
name = "Vehbi"
surname = "Çetinkaya"
age = 19

print("My name is {} {}".format(name, surname))
print("My name is: {1} {0}".format(name, surname))
print("Beni Adım: {s} {n}".format(n=name, s=surname))
print("Beni Adım: {s} {n} Yaşım İse {y}".format(n=name, s=surname, y=age))
print("Beni Adım: {0} {1} Yaşım İse {2}. {2}".format(name,surname,age))

number = 5/3
print("Sonuç {n:1.2}".format(n= number))
print(f"Merhaba ben: {name} {surname} benim yaşım {age} 5'in 3'e bölümü {number:1.8}")